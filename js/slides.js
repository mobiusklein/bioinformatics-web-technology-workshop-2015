hljs.configure({useBR: false})
hljs.initHighlightingOnLoad();
$(function(){
    $(document).on("keypress", function(evt){
        if(evt.charCode == 13){
            runDemo()
        }
    })
    $('title').text("Web Technology Workshop Series")
})

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

function runDemo(){
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
