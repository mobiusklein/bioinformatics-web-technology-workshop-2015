<script src='https://code.jquery.com/jquery-2.1.3.min.js'></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/highlight.min.js" type="text/javascript" charset="utf-8"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/languages/javascript.min.js" type="text/javascript" charset="utf-8"></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/styles/monokai_sublime.min.css">
<link rel="stylesheet" type="text/css" href="../css/slides.css">
<script src='../js/slides.js'></script>
<script>runDemo=DOMDemo</script>
## JavaScript and Web Technology Workshop
##### Joshua Klein 


### Lecture 2 - HTML and the DOM


### What does a web page look like?
A web page is an XML file
```html
<!DOCTYPE html5> <!-- Treat this as an HTML5 document  -->
<html> <!-- Top level tag -->
<head> <!-- Head tag contains most non-visual tags -->
    <title>Page Title</title>
    <script type="text/javascript">
    var appData;
    function appLogic(){ console.log("Ping!"); }
    </script>
</head>
<body>
<h2 id='page-header'>Page Header</h2>
<p class='content'> Things in this paragraph </p>
<p class='content'> Things in another paragraph </p>
<div> Footer </div>
</body>
</html>
```


### What is the DOM?
**D**ocument **O**bject **M**odel
The computational representation of a web page. Want to operate on a part of the web page? You need to find it first!
```javascript
htmlCollection = document.getElementsByTagName("div")
htmlCollection = document.getElementsByClassName("content")
singleTag = document.getElementById("page-header")
//Select by CSS path
htmlCollection = document.querySelectorAll(".content")
singletag = document.querySelector("#page-header")
```

<small>`htmlCollection` is an array of `DOM objects`, while `singleTag` is just one `DOM object`. `DOM objects` are just JavaScript wrappers around the host's representation of that rendered content.</small>

You change the properties of the page by modifying the `DOM`.


### Changing Text and Color
```javascript
var headerTag = document.getElementById("page-header")
headerTag.style.color = "red"
var footerDiv = document.getElementsByTagName("div")[0]
footerDiv.innerHTML = "<p>Now a paragraph</p>"
```
The built-in DOM API for changing style options that are settable by CSS use *camelCase* names instead of *kebab-case*.


### Adding New Tag Trees Programmatically
```javascript
var contentTags = document.getElementsByClassName("content");
for(var i = 0; i < contentTags.length; i++){
    var tag = contentTags[i]
    var newContent = document.createElement("p")
    newContent.textContent = "I'm content at position " + i;
    tag.appendChild(newContent)
}
```


### textContent vs. innerHTML
`textContent` is for writing plain text. It will automatically escape markup passed through it. `innerHTML` will parse markup and render it within the containing node.


### Adding Actions and Reactions
Most websites we visit are highly interactive, with things to click, hover over, and act on. Let's add that to our example.

```html
<!DOCTYPE html5> <!-- Treat this as an HTML5 document  -->
<html> <!-- Top level tag -->
<head> <!-- Head tag contains most non-visual tags -->
    <title>Page Title</title>
    <script type="text/javascript">
    function appLogic(){ alert("Ping " + this + "!"); }
    </script>
</head>
<body>
<h2 id='page-header'>Page Header</h2>
<p class='content' onclick="appLogic()"> Things in this paragraph </p>
<p class='content'> Things in another paragraph </p>
<div> Footer </div>
</body>
<script>
function initPage(){
    var header = document.getElementById("page-header")
    console.log(header)
    header.addEventListener("mouseover", function(){(this.innerHTML = "Mouse over!")})
    header.addEventListener("mouseout", function(){(this.innerHTML = "Mouse out!")})
}
document.onreadystatechange = function(){
    if(document.readyState == "complete"){
        initPage();
    }
}
</script>
</html>
```
<a href="7.html" target='_blank'>Demo</a>


### Functional Programming, The Revenge Of
Notice how event handlers are passed functions. They can be functions declared with names, or anonymous functions declared on the spot.


### Why do `onreadystatechange`?
Often, the DOM isn't fully parsed and ready to be acted on with JavaScript when the script would be parsed and executed. 

 The `Window` and/or `Document` objects will dispatch events for when the DOM are ready to be used.

<small class='fragment'>Yes, and/or. There are many different ways to check, each being slightly different and only available in some browsers. Seems like an aweful lot of stuff to check if you want to support older browsers.</small>


### jQuery, the unifying API
[`jQuery`](https://jquery.com/) is a library that provides many, many cross-browser, backwards compatible functions for event handling DOM manipulation, iterator functions, `AJAX`, and more.

Instead of handling each individual browser ourselves, let's use jQuery.


### Convenience Dispatch Function
```javascript
//jQuery assumes control over $ for convenience
jQuery === $
//Passing a function assigns it to the page's onready handler
jQuery(function(){/*...*/})
//Query the DOM, wrapping it in a convenience object
$(".css-selector #string")
//Create a new DOM object detached from the DOM
$("<div></div>")
//Wraps an existing DOM object in the same type of convenience object
$(document.getElementById("string"))
```


### Querying the DOM by CSS Selector
Where we had three (or more) functions available through `document` for querying the `DOM`, `jQuery` uses just one, the behavior of `$()` when passed a string or `DOM` object.

`$("...")` selects elements from the `DOM` with CSS Selector syntax, the same scheme used by style sheets. This is a succinct way to fetch one or more elements

```css
.class-name
#id-name
tag-name
[attribute-name="value"]
.class-name tag-name #chain
//
```



### DOM Wrapper Conveniences
```javascript
tag = $(".css-selector")
tag.html()   //Get or set HTML content
tag.text()   //Get or set Text content
tag.css({})  //Get or set element's inline CSS style
tag.attr({}) //Get or set element's attributes ()
tag.data({}) //Associate application data with element
```
Functions with `{}` arguments can be parameterized with a key-value pair of arguments, or passed a single `Object` to set multiple values at once


### One more time, with jQuery
```html
<!DOCTYPE html5>
<html>
<head>
    <title>Page Title</title>
    <!-- Include jQuery Script -->
    <script src='https://code.jquery.com/jquery-2.1.3.min.js'></script> 
    <script type="text/javascript">
    $(function(){ //jQuery assigns itself to the variables "$" and "jQuery"
        $("#page-header").mouseover(function(){$(this).html("Mouseover!")})
        .mouseout(function(){$(this).html("Mouseout!")})
    })
    appLogic = function(){alert("Ping!" + this)}
    </script>
</head>
<body>
<h2 id='page-header'>Page Header</h2>
<p class='content' onclick="appLogic()"> Things in this paragraph </p>
<p class='content'> Things in another paragraph </p>
<div> Footer </div>
</body>
</html>
```
<a href="9.html" target='_blank'>Demo</a>


### Binding and `this`
Did you notice the inline call to `appLogic`'s reference to `this` referred to `Window` while the event handler attached by jQuery and `addEventListener` bound `this` to the DOM element the event was caused by?



### Less typing through chaining
```javascript
$("#page-header").mouseover(function(){$(this).html("Mouseover!")})
        .mouseout(function(){$(this).html("Mouseout!")})
```
We're selecting the element with id `page-header` first, returning a `DOM` element wrapped by `jQuery`, then binding a function to its `mouseover` event handler. This binding function call *returns* the `DOM` object wrapped by `jQuery`, and then binding another function to the element's `mouseout` event handler.



### Now, let's be serious again
```html
<!DOCTYPE html>
<html>
<head>
    <script src='https://code.jquery.com/jquery-2.1.3.min.js'></script> 
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">

    <title></title>
    <script>
    $(function(){
        $("#options").change(function(){
            loadData(this.value)
        })
        loadData($("#options").children()[0].value)
    })
    function loadData(name){
        var gene = DataStore[name]
        var container = $("#contents")
        container.find("#header h3").html(gene.geneName)
        container.find("#header i").html(gene.symbol)
        container.find("#organism").html(gene.organism)
        container.find("#summary").html(gene.summary)
    }
    var DataStore = {
        "TP53": {
            "symbol": "TP53",
            "geneName": "tumor protein p53 ",
            "organism": "Human",
            "summary": "This gene encodes a tumor suppressor protein containing transcriptional activation, DNA binding, and oligomerization domains. The encoded protein responds to diverse cellular stresses to regulate expression of target genes, thereby inducing cell cycle arrest, apoptosis, senescence, DNA repair, or changes in metabolism. Mutations in this gene are associated with a variety of human cancers, including hereditary cancers such as Li-Fraumeni syndrome. Alternative splicing of this gene and the use of alternate promoters result in multiple transcript variants and isoforms. Additional isoforms have also been shown to result from the use of alternate translation initiation codons."
        },
        "APOE": {
            "symbol": "APOE",
            "geneName": "apolipoprotein E",
            "organism": "Human",
            "summary": "The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hyperlipoproteinemia (HLP III), in which increased plasma cholesterol and triglycerides are the consequence of impaired clearance of chylomicron and VLDL remnants. Alternative splicing results in multiple transcript variants."
        },
        "SLC6A4": {
            "symbol": "SLC6A4",
            "geneName": "solute carrier family 6 (neurotransmitter transporter), member 4",
            "organism": "Human",
            "summary": "This gene encodes an integral membrane protein that transports the neurotransmitter serotonin from synaptic spaces into presynaptic neurons. The encoded protein terminates the action of serotonin and recycles it in a sodium-dependent manner. This protein is a target of psychomotor stimulants, such as amphetamines and cocaine, and is a member of the sodium:neurotransmitter symporter family. A repeat length polymorphism in the promoter of this gene has been shown to affect the rate of serotonin uptake and may play a role in sudden infant death syndrome, aggressive behavior in Alzheimer disease patients, and depression-susceptibility in people experiencing emotional trauma."
        }
    }
    </script>
</head>
<body class='container'>
<h2>Protein Annotations</h2>
<select id='options'>
    <option value="TP53">TP53</option>
    <option value="APOE">APOE</option>
    <option value="SLC6A4">SLC6A4</option>
</select>
<div id='contents'>
    <header id="header" >
        <h3></h3>
        Symbol: <i></i>
    </header>
    <br>
    <div id='organism'></div>
    <div id='summary'>
        
    </div>
</div>
</body>
</html>
```
<a href="13.html" target='_blank'>Demo</a>


### Taking a closer look
```javascript
function loadData(name){
    var gene = DataStore[name]
    //Find the id=content tag
    var container = $("#contents")
    //Find h3 under id=header under id=contents and set HTML conents
    container.find("#header h3").html(gene.geneName)
    //Find i under id=header under id=contents and set HTML conents
    container.find("#header i").html(gene.symbol)
    //Find id=organism under id=contents and set HTML conents
    container.find("#organism").html(gene.organism)
    //Find id=summary under id=contents and set HTML conents
    container.find("#summary").html(gene.summary)
}
```


### On-Ready Function
```javascript
$(function(){
        $("#options").change(function(){
            loadData(this.value)
        })
        loadData($("#options").children()[0].value)
})
```


### Adding more dynamic content
```html
<!DOCTYPE html>
<html>
<head>
    <script src='https://code.jquery.com/jquery-2.1.3.min.js'></script> 
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">
    <script>
    $(function(){
        $("#options").change(function(){
            loadData(this.value)
        })
        var geneSymbols = Object.keys(DataStore)
        for(var i = 0; i < geneSymbols.length; i++){
            var gene = geneSymbols[i]
            $("#options").append($("<option></option>").attr("value", gene).text(gene))
        }
        loadData($("#options").children()[0].value)
    })
    function loadData(name){
        var gene = DataStore[name]
        var container = $("#contents")
        container.find("#header h3").html(gene.geneName)
        container.find("#header i").html(gene.symbol)
        container.find("#organism").html(gene.organism)
        container.find("#summary").html(gene.summary)
    }
    var DataStore = {
        "TP53": {
            "symbol": "TP53",
            "geneName": "tumor protein p53 ",
            "organism": "Human",
            "summary": "This gene encodes a tumor suppressor protein containing transcriptional activation, DNA binding, and oligomerization domains. The encoded protein responds to diverse cellular stresses to regulate expression of target genes, thereby inducing cell cycle arrest, apoptosis, senescence, DNA repair, or changes in metabolism. Mutations in this gene are associated with a variety of human cancers, including hereditary cancers such as Li-Fraumeni syndrome. Alternative splicing of this gene and the use of alternate promoters result in multiple transcript variants and isoforms. Additional isoforms have also been shown to result from the use of alternate translation initiation codons."
        },
        "APOE": {
            "symbol": "APOE",
            "geneName": "apolipoprotein E",
            "organism": "Human",
            "summary": "The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hyperlipoproteinemia (HLP III), in which increased plasma cholesterol and triglycerides are the consequence of impaired clearance of chylomicron and VLDL remnants. Alternative splicing results in multiple transcript variants."
        },
        "SLC6A4": {
            "symbol": "SLC6A4",
            "geneName": "solute carrier family 6 (neurotransmitter transporter), member 4",
            "organism": "Human",
            "summary": "This gene encodes an integral membrane protein that transports the neurotransmitter serotonin from synaptic spaces into presynaptic neurons. The encoded protein terminates the action of serotonin and recycles it in a sodium-dependent manner. This protein is a target of psychomotor stimulants, such as amphetamines and cocaine, and is a member of the sodium:neurotransmitter symporter family. A repeat length polymorphism in the promoter of this gene has been shown to affect the rate of serotonin uptake and may play a role in sudden infant death syndrome, aggressive behavior in Alzheimer disease patients, and depression-susceptibility in people experiencing emotional trauma."
        }
    }
    </script>
</head>
<body class='container'>
<h2>Protein Annotations</h2>
<select id='options'>
</select>
<div id='contents'>
    <header id="header" >
        <h3></h3>
        Symbol: <i></i>
    </header>
    <br>
    <div id='organism'></div>
    <div id='summary'>
    </div>
</div>
</body>
</html>
```
<a href="14.html" target='_blank'>Demo</a>


### Building a dynamic list
```javascript
//On-Ready Function
$(function(){
    //Setting up the change event handler
    $("#options").change(function(){
        loadData(this.value) // Notice the presence of `this`
    })
    //Get the list of keys of DataStore
    var geneSymbols = Object.keys(DataStore)
    //For each gene in the data
    for(var i = 0; i < geneSymbols.length; i++){
        var gene = geneSymbols[i]
        /*
         * Create <option></option> tag, set it's "value" attribute to the 
         * value of the current gene symbol, and the text to the same value
         */
        $("#options").append($("<option></option>").attr("value", gene).text(gene))
    }
    //Load the first entry
    loadData($("#options").children()[0].value)
})
```


### Another Example
This example is too big to place in a slide. Open the Demo below:

<a href="20.html" target='_blank'>Demo</a>


### What does the data look like?
```json
{
    "CAS Number": "83712-60-1",
    "ChEBI ID": "",
    "RxList Link": "",
    "Drug Type": "BiotechDrug",
    "BindingDB ID": "",
    "PubChem Substance ID": "",
    "UniProt ID": "",
    "Name": "Defibrotide",
    "KEGG Drug ID": "",
    "UniProt Title": "",
    "Pdrhealth Link": "",
    "HET ID": "",
    "Drugs.com link": "",
    "TTD ID": "",
    "ChemSpider ID": "",
    "DPD ID": "",
    "NDC ID": "",
    "KEGG Compound ID": "",
    "GenBank ID": "",
    "PubChem Compound ID": "",
    "DrugBank ID": "DB04932",
    "PharmGKB ID": "PA164749105",
    "Wikipedia Link": "http://en.wikipedia.org/wiki/Defibrotide"
}
```


### Digging Deeper: List Generation
```javascript
/*
Convert the list of Entry objects into a clickable list in #drug-list
*/
function renderList(listEntries){
    var container = $("#drug-list")
    //Clear old contents
    container.html("")
    for(var i = 0; i < listEntries.length; i++){
        //An Entry object, with some attributes including
        //a `Name`
        var entry = listEntries[i];
        var entryElement = $("<a></a>")
        entryElement.text(entry.Name)
        //Associate the current Entry object
        //with this `<a></a>` tag
        entryElement.data("entry", entry)
        
        //Bind an event handler to the `<a>` tag's click event
        //to render the associated Entry
        entryElement.click(function(){
            //Retrieve the associated Entry through $.data
            var clicked = $(this).data('entry')
            renderEntry(clicked)
        })
        //Add the current `<a></a>` to the DOM list
        container.append(entryElement)
    }
}
```


### Digging Deeper: Detailed View

```javascript
/*
Translate an Entry object into content in #entry-contents
*/
function renderEntry(entry){
    var container = $("#entry-contents")
    var name = entry.Name
    var links = {}
    var ids = {}
    var keys = Object.keys(entry)
    var linkPattern = /(.*)\sLink/
    var idPattern = /(.*)\sID/i
    //Pull out all of the URLs and Identifiers
    for(var i = 0; i < keys.length; i++){
        var key = keys[i]
        if(linkPattern.test(key)){
            var sourceName = linkPattern.exec(key)[1]
            links[sourceName] = entry[key]
        } 
        else if(idPattern.test(key)){
            var sourceName = idPattern.exec(key)[1]
            ids[sourceName] = entry[key]
        }
    }
    //Render the Entry's data in HTML
    container.find('#drug-name').text(name)
    //Render links
    var linkContainer = container.find("#link-box")
    //Clears previous contents and writes the new header
    linkContainer.html("<h4>Links</h4>")
    var linkNames = Object.keys(links)
    for(var i = 0; i < linkNames.length; i++){
        var linkName = linkNames[i]
        var linkURL = links[linkName]
        var linkTag = $("<a></a>").attr("href", linkURL).text(linkName).attr("target", "_blank")
        linkContainer.append($("<div></div>").append(linkTag))
    }
    //Render identifiers
    var idContainer = container.find("#id-box")
    //Clears the previous contents and writes the new header
    idContainer.html("<h4>External IDs</h4>")
    var idNames = Object.keys(ids)
    for(var i = 0; i < idNames.length; i++){
        var idName = idNames[i]
        var idString = ids[idName]
        //Skip this entry if the text is empty
        if(idString === ""){
            continue
        }
        var idTag = $("<div></div>").text(idName + ": " + idString)
        idContainer.append(idTag)
    }
}

```


### While we're at, CSS
```css
#drug-list{
    float: left;
    border: 1px solid grey;
    border-radius: 3px;
    padding: 5px;
    width: 30%;
    height: 800px;
    overflow-y: scroll;
}

#drug-list a{
    cursor: pointer;
    display: block;
    padding: 2px;
}

#entry-contents{
    float: left;
    border: 1px solid grey;
    border-radius: 3px;
    padding: 5px;
    width: 70%;
    height: 800px;
}

/* Put the next element in-line to the left*/
.float-box{
    float: left;
    padding: 10px;
}
/* Put the next element on the next line */
.outer-box{
    clear: both;
}
```


### The Associated HTML
```html
<body class='container'>
<h2>Drug Listing</h2>
<div id='drug-list'>
    
</div>
<div id='entry-contents'>
    <h3 id='drug-name'></h3>
    <div class='outer-box'>
        <div id='link-box' class='float-box'>
            
        </div>
        <div id='id-box' class='float-box'>
            
        </div>
    </div>
</div>
</body>
```


### Adding Some Filtering
```javascript
function filterList(pattern){
    var container = $("#drug-list")
    var listEntries = container.children()
    var pattern = new RegExp(pattern + '.*', "ig");
    for(var i = 0; i < listEntries.length; i++){
        var entry = $(listEntries[i]);
        if(!pattern.test(entry.text())){
            entry.hide()
        } else {
            entry.show()
        }
    }
}
```

<a href="24.html" target='_blank'>Demo</a>


### Binding Search Functions
```html
<input id='search-box' type='text' placeholder='Search Drug Name'/>
```
```javascript
$(function(){
    renderList(DrugSource)
    renderEntry(DrugSource[0])

    $("#search-box").keyup(function(){
        var pattern = $(this).val()
        filterList(pattern)
    })
})
```


### Reusing An Old Example
```html
<!DOCTYPE html5>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title></title>
    <script src='https://code.jquery.com/jquery-2.1.3.min.js'></script>
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">
    <script>
codonTable = { "CTT": "L", "ATG": "M", "ACA": "T", "ACG": "T", "ATC": "I", "ATA": "I", "AGG": "R", "CCT": "P", "AGC": "S", "AGA": "R", "ATT": "I", "CTG": "L", "CTA": "L", "ACT": "T", "CCG": "P", "AGT": "S", "CCA": "P", "CCC": "P", "TAT": "Y", "GGT": "G", "CGA": "R", "CGC": "R", "CGG": "R", "GGG": "G", "GGA": "G", "GGC": "G", "TAC": "Y", "CGT": "R", "GTA": "V", "GTC": "V", "GTG": "V", "GAG": "E", "GTT": "V", "GAC": "D", "GAA": "E", "AAG": "K", "AAA": "K", "AAC": "N", "CTC": "L", "CAT": "H", "AAT": "N", "CAC": "H", "CAA": "Q", "CAG": "Q", "TGT": "C", "TCT": "S", "GAT": "D", "TTT": "F", "TGC": "C", "TGG": "W", "TTC": "F", "TCG": "S", "TTA": "L", "TTG": "L", "TCC": "S", "ACC": "T", "TCA": "S", "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A" }

DNASequence = function(sequence){
    this.sequence = sequence
    this.translate = function(){
        return this.sequence.replace(/.../g, function(codon){ return codonTable[codon] })
    }
}
DNASequence.prototype.toString = function(){
    return "{Sequence " + this.sequence + "}"
}

$(function(){
    $("#protein").val("")
    $('#dna').keyup(function(){
        var seq = $(this).val().replace(/\s/g, '')
        console.log(seq)
        if(seq.length % 3 == 0){
            var dna = new DNASequence(seq)
            var prot = dna.translate()
            console.log(prot, $("#protein").val())
            $("#protein").val(prot)            
        }
    }).val("")
})

    </script>
    <style>
textarea{
    border-radius: 3px;
}
    </style>
</head>
<body class='container'>
    <div>
        <h3>Translate DNA</h3>
        <textarea id='dna' placeholder="Write DNA here" rows="10" cols="50">
        </textarea>
        <textarea id='protein' rows="10" cols="50" readonly placeholder='Get Protein Here'>
        </textarea>
    </div>
</body>
</html>
```
<a href="29.html" target='_blank'>Demo</a>


### Now you try it
Try one of the following:
- Make a web page that given a DNA sequence, gives you the RNA sequence
- Make a web page that highlights a repeated pattern in DNA or Protein
- Add more entries to an example's data
- Make something up!
