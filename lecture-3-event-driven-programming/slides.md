<script src='https://code.jquery.com/jquery-2.1.3.min.js'></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/highlight.min.js" type="text/javascript" charset="utf-8"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/languages/javascript.min.js" type="text/javascript" charset="utf-8"></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/styles/monokai_sublime.min.css">
<link rel="stylesheet" type="text/css" href="../css/slides.css">
<script src='../js/slides.js'></script>
<script>runDemo=DOMDemo</script>
## JavaScript and Web Technology Workshop
##### Joshua Klein 


### Lecture 3 - Event Driven Programming and AJAX


### Pragma - jQuery & other "Wrappers"
Rarely if ever use the built-in methods over `jQuery` and other wrapping APIs. Assume I am using `jQuery` through the `$` variable unless I say otherwise.


### Pragma - Servers and Requests
Starting this week, I am going to be using simple CGI scripts written in `Python` for some more advanced examples.

If you download the lectures from [https://github.com/mobiusklein/bioinformatics-web-technology-workshop-2015] and store them in a directory `workshop`, you can run them locally like this:
```bash
cd workshop/lecture-3-event-driven-programming
python -m CGIHTTPServer # Python 2.X
python -m http.server --cgi # Python 3.X
```


### What is "Synchronous" mean?
```javascript
value = syncWithSideEffects();
value2 = anotherSync();
```
`syncWithSideEffects()` and all of its side effects will resolve before `anotherSync()`. 

Their return values will be immediately defined.


### What is "Asynchronous" mean?
```javascript
asyncWithSideEffects();
anotherAsync();
```
`asyncWithSideEffects()` will return before its side effects have resolved. Its return value may be `undefined` or not readily usable. 

`anotherAsync()` may complete before `asyncWithSideEffects()` completes. They may have unexpected interactions.



### Events and Asynchronous Execution
```javascript
// Add an event handler for clicks on this button
$("#button").click(function(eventObj){
    //...
    moreLogic();
    //...
    //No return value from here
})
```
There is no way to know when this function will be called, or to *directly* capture information from its execution. 


### When is Asynchrony useful
1. Setting up responses to events, user-generated or otherwise
2. Requesting remote resources, e.g. data from the server &ast;
3. Timer-based invocation


### AJAX Requests
**A**synchronous **J**avascript **A**nd **X**ML

Make HTTP Requests asynchronously. There is a sophisticated built-in object type called `XMLHTTPRequest`, but it requires many lines of code to use.

Instead I'll using a `jQuery` wrapper.


### GET Requsts
<button onclick="runDemoBlock()"><b>Run Me</b></button>
```javascript
//$.get(urlFragment, successCallback)
$.get("drug_array.json", function(data){
    alert(data[0].Name)
})
```
A *GET* request is for fetching resources by name, or by passing a relatively small amount of data to the server to look it up with.

Here we're requesting a JSON file, containing some information. When the request completes, the `successCallback` will fire with the fetched content in the `data` variable.


### In Action
Drug Listing Demo features

1. Load data from server with AJAX on page load
    - Render data as a list of items to display
    - Render a detailed view of one selected item
4. Filter the list of items every time a text box changes

<a href="24.html" target='_blank'>Demo</a>


### Looking at the Code
```javascript
var DrugSource = [];
$(function(){
    //AJAX Here
    $.get("drug_array.json", function(data){
        //Save the data here
        DrugSource = data
        renderList(DrugSource)
        renderEntry(DrugSource[0])
    })
    //Event Handler when search changes
    $("#search-box").keyup(function(){
        var pattern = $(this).val()
        //In-memory filtering
        filterList(pattern)
    })
})
```


### Was AJAX necessary?
This request only fires once and it is only to load the data into the browser. Do we need AJAX for this? 

No, but it speeds up page loading since the page isn't waiting for all of the data to be parsed before it is `ready`. 



### A More Involved Example - What does the data look like?
```javascript
{
    "573":{ //A Genome
        "AT-polypeptides": [ //A data set
    { //An entry in a data set
        query_def: "gi|499528894|ref|CCI75254| ddl [Klebsiella pneumoniae]",
        hits: [
            {
                hit_def: "CP000647.1.gene96.p01 D-alanylalanine synthetase. Encoded by gene ddl. ARO:1000001 process or component of antibiotic biology or chemistry. ARO:3000723 cycloserine sensitive D-alanine synthetase. [Klebsiella pneumoniae subsp. pneumoniae MGH 78578]",
                e_value: 0,
                hsps: [
                {
                hit_from: 1,
                query_from: 1,
                hit_frame: "0",
                gaps: 0,
                identity: "304",
                hit_to: 306,
                query_to: 306,
                hseq: "MADKIAVLFGGTSAEREVSLNSGAAVLAGLREGGVDAHPVDPRDVDITQLKKQGFK...",
                qseq: "MADKIAVLFGGTSAEREVSLNSGAAVLAGLREGGVDAHPVDPRDVDITQLKKQG...",
                e_value: 0,
                query_frame: "0",
                __len__: 306,
                midline: "MADKIAVLFGGTSAEREVSLNSGAAVLAGLREGGVDAHPVDPRDVDITQLKKQG..."
                    }
                    ...
                ],
            },
            ...
        ],
        ...
    },
    ...
```


### The Plan
1. The user selects a genome and a data set to get a list of gene annotations
2. The user can view individual genes and their matches, or a summary
3. The user can change the genome or data set at any time to get a new list of genes.


### What Do We Need?
1. A list of genomes and data sets for each genome from the server
    - Assume we can't hard-code the genomes
    - Assume the same data sets may be available for all genomes
2. A way to get the chosen genome and data set from the user
3. A way to show the user the genes in the data set recieved



### A More Involved Example - Server Action: Retrieve Available Genomes and Data sets
```python
#!python
'''/cgi-bin/klebsiella_data.py'''
import cgi
import cgitb
import json
cgitb.enable()

data = json.load(open("klebsiella-pneumoniae_ti.fa.filtered.genomes.innate_resistance.json"))

options = {
    "genome_ids": data.keys(),
    "dataset_ids": data.values()[0].keys()
}

print "Content-Type: application/json;charset=utf-8;"
print

print json.dumps(options)
```


### A More Involved Example - Server Action: Retrieve Data set
```python
#!python
'''/cgi-bin/klebsiella_options.py'''
import cgi
import cgitb
import json
cgitb.enable()

store = cgi.FieldStorage()
data = json.load(open("klebsiella-pneumoniae_ti.fa.filtered.genomes.innate_resistance.json"))

parameters = {}
for key in store.keys():
    parameters[key] = store[key].value

if parameters.get("genome_id") is None:
    parameters["genome_id"] = u'573'
if parameters.get("dataset_id") is None:
    parameters["dataset_id"] = "comprehensive_antibiotic_resistance_database_AT-polypeptides"

genome = data[parameters["genome_id"]]
dataset = genome[parameters["dataset_id"]]

# Write HTTP Headers
print "Content-Type: application/json;charset=utf-8;"
print
# Write Response content
print json.dumps(dataset)
```



### Front-End Problem 1: Offer the user a choice
```javascript
var Genomes = []
var DataSets = []

$(function(){
    $.get("/cgi-bin/klebsiella_options.py", function(data){
        Genomes = data.genome_ids
        DataSets = data.dataset_ids
        var genomeSelector = $("#genome-selector")
        for(var i = 0; i < Genomes.length; i++){
            var genomeId = Genomes[i]
            var option = $("<option></option>").val(genomeId).text(genomeId)
            genomeSelector.append(option)
        }
        var dataSetSelector = $("#dataset-selector")
        for(var i = 0; i < DataSets.length; i++){
            var dataSetId = DataSets[i];
            var label = $("<lable class='radio-label'></lable>").text(dataSetId.replace("comprehensive_antibiotic_resistance_database_", "") + " ")
            var radioBtn = $('<input type="radio" name="dataset_id"/>').val(dataSetId)
            dataSetSelector.append(label.append(radioBtn))
        }
    })
})
```
<a href="http://localhost:8000/313.html" target='_blank'>Run Local Demo</a>


### Front-End Problem 2 - Processing the user's choice
```javascript
$(function(){
    //...
    $("#load-btn").click(function(evt){
        evt.preventDefault();
        loadDataset()
    })
})
var currentDataSet = []
function loadDataset(){
    //Translate the options form into a string or object
    //to be sent to the server
    var form = $("#option-form").serialize()
    //POST the data to the server
    $.post("/cgi-bin/klebsiella_data.py", form)
    //If the request succeeds, handle the response as follows
    .success(function(data){
        //Save the response data
        currentDataSet = data;
        //If there is content to render
        if(data.length > 1){
            //Show the first entry
            renderQuery(data[0])
            //Render the list of available entries as a select list
            renderQueryList(data)
        } else {
            //Otherwise let the user know this query had no data
            apologize("No data were found meeting these search criterion")
        }
    //If the request failed, let the user know
    }).error(function(error){
        apologize("An error occurred while processing your request. " + error.toString())
        })
}
```


### Render Queries
```javascript
$(function(){
    //...
    $("#gene-selector").change(function(){
        renderQuery(currentDataSet[this.value])
    })
})
function renderQueryList(queries){
    var container = $("#gene-selector")
    container.html("")
    for(var i = 0; i < queries.length; i++){
        var queryObj = queries[i]
        var queryName = queryObj.query_def.replace(/\[.+\]$/, "")
        var optionTag = $("<option></option>").text(queryName + " - " + queryObj.hits.length)
            .data('object', queryObj).val(i)
        container.append(optionTag)
    }
}

function renderQuery(queryObj){
    var container = $("#query")
    container.html("")
    container.append(
        $("<h3></h3>").text(queryObj.query_def.replace(/\[.+\]$/, ""))
        )
    var hitContainer = $("<div></div>")
    for(var i = 0; i < queryObj.hits.length; i++){
        var hitRep = renderHit(queryObj.hits[i])
        hitContainer.append(hitRep)
    }
    container.append(hitContainer)
}

function renderHit(hitObj){
    var container = $("<div></div>").addClass("hit")
    var parts = hitObj.hit_def.split(/\s/)
    var name = parts[0]
    var description = parts.slice(1).join(" ")
    .replace("ARO:1000001 process or component of antibiotic biology or chemistry. ", "")
    container.append($("<h5></h5>").text(name))
    .append($("<b></b>").text("E value: " + hitObj.e_value))
    .append("<br>")
    .append($("<b></b>").text("Identity: " + hitObj.hsps[0].identity))    
    .append($("<div></div>").addClass("hit-description").html(description.split(/\.\s/).join(".<br>")))
    return container
}
```

<a href="http://localhost:8000/314.html" target='_blank'>Run Local Demo</a>


### Drawing Charts
There is a new graphics library born for the internet every week. Some very good ones are:

1. D3.js
2. HighCharts
3. Raphael
4. KineticJS


### Visualizing Ontologies - Count Occurences
```javascript
function getARO(query){
    var aros = []
    function extractARO(hit){
        var pattern = /ARO:\d+/
        var parts = hit.hit_def.split(/\.\s/)
        for(var i = 0; i < parts.length; i++){
            if(pattern.test(parts[i]) && parts[i] != "ARO:1000001 process or component of antibiotic biology or chemistry"){
                //Reference variable from parent scope
                aros.push(parts[i])
            }
        }
    }
    query.hits.map(extractARO)    
    return aros
}
```


### Visualize Ontologies - Render Plot
```javascript
//Call this into the renderQuery function
function plotARO(queryObj){
    var aros = getARO(queryObj)
    var counts = {}
    aros.forEach(function(term){ counts[term] = (counts[term]||0) + 1})
    var plotSeries = []
    Object.keys(counts).forEach(function(aro){
        plotSeries.push({name: aro, data: [counts[aro]]})
    })

    $('#plot-container').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Antibiotic Resistance Ontology Matches'
        },
        subtitle: {
            text: 'Source: http://arpcard.mcmaster.ca/'
        },
        yAxis:{
            title: "Occurences"
        },
        xAxis:{

            categories: ["Antibiotic Resistance Ontology"]
        },
        series: plotSeries
        }
    )
}
```

<a href="http://localhost:8000/315.html" target='_blank'>Run Local Demo</a>


### You Try It
1. Link drug names from the annotations to drug names in "drug_array.json"
2. Add a new event handler to an example
3. Add a new AJAX request route to the server
4. Make Something Up
