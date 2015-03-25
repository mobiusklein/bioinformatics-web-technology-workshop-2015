hljs.configure({useBR: false})
hljs.initHighlightingOnLoad();

function runDemo(){
    console.log("A demo")
};


function demoRunner(){
    runDemo()
}


$(function(){
    $(window).on("keypress", function(evt){
        if(evt.charCode == 13){
            demoRunner()
        }
    })
    $('title').text("Web Technology Workshop Series")
})

function registerRunDemo(){
    $(window).on("keypress", function(evt){
        if(evt.charCode == 13){
            demoRunner()
        }
    })
}


function ConsoleAPIStub(){
    this.buffer = "";
    this.console = console
}

ConsoleAPIStub.prototype.log = function(vararg) {
    var results = []
    for(var i = 0; i < arguments.length; i++){
        var argI = arguments[i]
        if (argI === undefined){
            argI = "undefined"
        } else {
            argI = JSON.stringify(argI)
        }
        results.push(argI);
    }
    results = results.join("\n")
    this.buffer += "O: " + results + (results.trim().length > 0 ? '\n' : "");
};

ConsoleAPIStub.prototype.flush = function(){
    if(this.buffer === ""){
        return
    }
    this.console.log(this.buffer)
    this.buffer = ""
}

function runDemoBlock(){
    var _console = console
    console = new ConsoleAPIStub()
    var codeString = $(".present pre code").text()
    var codeLines = codeString.split("\n");
    var currentChunk = ""
    var res = null;
    for(var i = 0; i < codeLines.length; i++){
        try {
            currentChunk += currentChunk.length == 0 ? codeLines[i] : "\n" + codeLines[i];
            res = eval(currentChunk);
            if(res !== undefined){
                console.log(res)
            }
            if(currentChunk.trim() != ""){
                _console.info("I: ", currentChunk)
            }
            console.flush()
            currentChunk = ""
        } catch(err) {
            //no-op
        }
    }
    console = _console
}


function DOMDemo(){
    var out = renderDemoBlock();
    if(out == -1){
        runDemoBlockOnTargetWindow();
    }
}


function runDemoBlockOnTargetWindow(){
    if(window.targetWindow === undefined){
        alert("No target window. Render a demo block of HTML code first");
        return
    }
    var content = $(".present pre code").text()
    console.log(content)
    targetWindow.eval(content)
}

function renderDemoBlock(){
    var demoLink = $(".present a:contains('Demo')")
    if(demoLink.attr('href') !== undefined){
        demoWindow = window.open(demoLink.attr('href'), "_blank", "height=600,width=600")
        window.targetWindow = demoWindow
        return demoWindow
    }
    
    var content = $(".present pre code.lang-html").text()
    console.log(content, $(".present pre code.lang-html"))
    if(content.length == ""){
        return -1 
    }
    var demoWindow = window.open(null, "_blank", "height=600,width=600")
    $(demoWindow.document.body).html(content)
    var stripScripts = demoWindow.document.getElementsByTagName("script")
    var scripts = []

    for(var i = 0; i < stripScripts.length; i++){
        scripts.push(stripScripts[i])
    }

    for(var i = 0; i < scripts.length; i++){
        var tag = demoWindow.document.createElement("script");
        tag.text = scripts[i].text
        console.log(tag)
        demoWindow.document.body.appendChild(tag)
    }
    window.targetWindow = demoWindow
    return demoWindow
}
