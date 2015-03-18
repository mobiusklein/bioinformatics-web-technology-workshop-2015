<script src='https://code.jquery.com/jquery-2.1.3.min.js'></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/highlight.min.js" type="text/javascript" charset="utf-8"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/languages/javascript.min.js" type="text/javascript" charset="utf-8"></script>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/styles/monokai_sublime.min.css">
<link rel="stylesheet" type="text/css" href="../../css/slides.css">
<script src='../../js/slides.js'></script>
## JavaScript and Web Technology Workshop
##### Joshua Klein 


## What is this?
An introduction to the wide world of web technology and how we can use it in science. Here are a few you might already be using:

- Rstudio
- IPython/Jupyter Notebook
- NCBI BLAST Website


## How to unlock the powers of your web browser
- [Chrome Devtools](https://developer.chrome.com/devtools)
- [FireFox WebConsole](https://developer.mozilla.org/en-US/docs/Tools/Web_Console)
- [Internet Explorer](https://msdn.microsoft.com/en-us/library/ie/gg699336%28v=vs.85%29.aspx)
- [Safari](https://developer.apple.com/library/mac/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/KeyboardShortcuts/KeyboardShortcuts.html)


### Lecture 1 - A language primer


## Rough Timeline of Web Technologies
```
1991: HTML
1994: HTML 2
1996: CSS 1 + JavaScript
1997: HTML 4
1998: CSS 2 + ECMAScript 2 | Google
2000: XHTML 1
2002: Tableless Web Design
2005: AJAX  | Facebook
2009: HTML 5 + ECMAScript 5
2015: ECMAScript 6
```
<cite>HTML5Rocks Slideshow @ <a href="http://slides.html5rocks.com/#landing-slide">http://slides.html5rocks.com/#landing-slide</a></cite>


## Why yet another scripting language?

Because it made sense <code>{currentYear - 1996}</code> years ago. Netscape wanted a light-weight language to add dynamic behavior to web pages that was not `Java`.

JavaScript is used to implement `client-side` logic, and to orchestrate communication with the `server`


  ## Is JavaScript not a real programming language?

  It's real (Turing Complete), it just has a limited sandbox it plays in provided by the host (web browser). It does not directly have:

  - File System
  - Threading
  - Other System Calls


## What kind of language is it?
- Dynamic
- Multi-paradigm
    - Object-Oriented (Prototypal)
    - Functional
- Asynchronous


## Syntax
```javascript
// C Family Syntax
if (true){
    var foo = 5;
} else {
    bar = new Promise(); // New non-literal objects declared with "new" keyword
    console.log(bar) // Print function accessed through console API
}
/* Dynamically typed */
function pow(x, p){
    var result = x;
    p -= 1
    while(p > 0){ //While loops and for loops exist
        result *= x;
        p -= 1;
    }
    return result
}
```


 ## Some comments
 JavaScript has a semi-colon delimited grammar, but the semi-colons are "optional". Most of the time, they can be omitted, but this may cause expressions to be fused if they are a single syntactic expression

 ```javascript
 foo = [1, 2, 33]
 bar = foo
 [1] + 1
 ```


## Basic Types
- Number   `42, 3.1415`
- Boolean   `true, false, new Boolean(42)`
- String    `"The quick brown fox jumps over the lazy dog"`
- Array     `[42, "The quick brown fox", 3.1415`
- **Object**    `{'type': 'fox', 'color': 'brown'}}`

Also `null` (user null values), `undefined` (language null values), and `NaN` are distinct but similar non-value special types


  ## Additional Standard Types
  - Date     <span class='de-emphasis'>`Sun Mar 15 2015 22:21:19 GMT-0400 (Eastern Daylight Time`</span>
  - RegExp   `/([A-Z][a-z]+)/` <span class='de-emphasis'>(Note the `/.../` literal syntax)</span>
  - Error    <span class='de-emphasis'>`throw new Error("You are mistaken");`</span>

  Many more built-in Objects and Types have been added, most with with specialized behavior such as specialized strongly typed ArrayViews. 


## Scope Rules
```javascript
//Global Scope
var myVar = "A global variable";

function myFunc(a, b){
    //Function Scope
    var funcVal = "A local variable"
    if(funcVal.length > a){
        //Block variable is hoisted
        var result = true;
    } else {
        //Variable name used without declaration
        //is automatically looked up in global "window" scope
        myVar = b
    }

    return result;
}
```


 ## When can hoisting go wrong?
 ### A contrived example...
  ```javascript
  var state = 'loading'
 
  function update(data){
     console.log(state) // Should say "loading"
     if(state == 'loading'){ // We'll check the global variable
         var state = 'isLoading' // and shadow it internally
     }
     console.log(state) // Should say "isLoading"
  }
  update()
  ```


## Operators - Binary Numerical
```javascript
// Binary numerical operators are as you expect them
num8 = 3 + 5
num2 = num8 - 6
num10_4 = num8 * 1.3
num2 = 6 / 3

console.log("Hello, " + "World") // Strings know about addition

console.log([12, 17] + [13, 19]) // Everyone else is a bit confused...

console.log((5 > 2) && ((3 < 2) || true)) // Boolean binaries are as expected
```


  ## Operators - Comparison
  ```javascript
  // Numbers are well defined for ordinal comparison
  55 >= 50
  // Arrays and Strings are lexically ordered
  "ab" < "ba"
  ```



 ## Operators - Equality
  ```javascript
  //Naturally numbers work
  4 == 2 + 2
  
  //As do strings
  "Quick brown fox" != "quick brown fox"
  
  //But Arrays and Objects do not have any "deep equality testing"
  a = [1, 2]
  console.log(a == [1, 2])
  console.log(a == a)
  ```



 ## Gotchas - Automatic type coercion and ===
  ```javascript
  //Don't
  console.log(1 == "1")
  console.log(null == undefined)
  //Do
  console.log(1 === "1")
  console.log(null === undefined)
  ```
 The double-equals tries to find any way to make the values equal, including  casting them to different types.
 
 The triple-equals is strict and does not allow type conversion. The inequality  analog is `!==`.


## More on Object
```javascript
//FarScape
var johnCrichton = {'name': "John Crichton", 'profession': "Astronaut"}
console.log(johnCrichton.name)
console.log(johnCrichton.species)
johnCrichton.species = "Human"
//Alternate attribute lookup
console.log(johnCrichton['species'])
```

`Objects` are just arbitrary key-value pairs. Anything can be a value. `Numbers` and `Strings` can be keys. Anything else will be turned into a `String` when referenced. Only valid identifiers can be dot-accessed though.


 ## JSON Notation
 ```json
 {
    "key": "attribute", "number": 1,
    "values": {
        1: [2, 3, 4],
        2: [5, 6, 7]
    }
 }
 ```
 A lighter-than-xml data transport text format for conveying structured data with the common JavaScript Basic Types. Handy for sending objects to and from the server. Use `JSON.stringify` to serialize, and `JSON.parse` to deserialize.


## Now for something more serious
```javascript
/*
Given some text and a list of phrases,
return the list which the current text 
is a good lexical stem for
*/
function completePhrase(text, lookUp){
    var pattern = new RegExp(text, 'i'); //Global and ignore case
    var matches = [];
    for(var i = 0; i < lookUp.length; i++){
        var phrase = lookUp[i];
        if(pattern.test(phrase)){
            matches.push(phrase);
        }
    }
    return matches;
}
```


## How to include JS in a web page
```html
<!DOCTYPE html5>
<html>
<head>
    <script src='path/to/script.js'></script>
    <script>
    //Script Body Here
    </script>
</head>
<body>
<!-- Page Body Here -->
</body>
</html>
```


### Including completePhrase in a web page
```html
<!DOCTYPE html5>
<html>
<head>
<script>
function completePhrase(text, lookUp){
    var pattern = new RegExp(text, 'i'); //Global and ignore case
    var matches = [];
    for(var i = 0; i < lookUp.length; i++){
        var phrase = lookUp[i];
        if(pattern.test(phrase)){
            matches.push(phrase);
        }
    }
    return matches;
}    
</script>
</head>
<body>
<!-- Page Body -->
</body>
</html>
```


### Namespacing
JavaScript does not have a built-in namespacing or module system. This will change with ECMAScript 6 later this year. 

There are a few 3rd-party libraries that add sophisticated library loading features today, with distinct philosophies and additional functionalities. Two well known ones:

- [Requre.js](http://requirejs.org/)
- [Browserify](http://browserify.org/)


### Namspacing and Modules
#### Simple Grouping
You can also roll your own namespacing
```javascript
var TextUtils = {} //Define an object literal
TextUtils.completePhrase = function(text, lookUp){
    var pattern = new RegExp(text, 'i'); //Global and ignore case
    var matches = [];
    for(var i = 0; i < lookUp.length; i++){
        var phrase = lookUp[i];
        if(pattern.test(phrase)){
            matches.push(phrase);
        }
    }
    return matches;
}
```


 ### Namespacing and Modules
 #### Enclosed Scope
 ```javascript
 TextUtils = (function(){
     namespace = {}
     var regexpFlags = "i"
     namespace.completePhrase = function(text, lookUp){
         var pattern = new RegExp(text, regexpFlags); //Namspace Local Variable
         var matches = [];
         for(var i = 0; i < lookUp.length; i++){
             var phrase = lookUp[i];
             if(pattern.test(phrase)){
                 matches.push(phrase);
             }
         }
         return matches;
     }
 
     return namespace
 })() // Immediately Invoked Function Evalution (IIFE) returns the namespace
      // which carries all of the exposed public methods
 
 ```


### Remember the Central Dogma?
```javascript
codonTable = { "CTT": "L", "ATG": "M", "ACA": "T", "ACG": "T", "ATC": "I", "ATA": "I", "AGG": "R", "CCT": "P", "AGC": "S", "AGA": "R", "ATT": "I", "CTG": "L", "CTA": "L", "ACT": "T", "CCG": "P", "AGT": "S", "CCA": "P", "CCC": "P", "TAT": "Y", "GGT": "G", "CGA": "R", "CGC": "R", "CGG": "R", "GGG": "G", "GGA": "G", "GGC": "G", "TAC": "Y", "CGT": "R", "GTA": "V", "GTC": "V", "GTG": "V", "GAG": "E", "GTT": "V", "GAC": "D", "GAA": "E", "AAG": "K", "AAA": "K", "AAC": "N", "CTC": "L", "CAT": "H", "AAT": "N", "CAC": "H", "CAA": "Q", "CAG": "Q", "TGT": "C", "TCT": "S", "GAT": "D", "TTT": "F", "TGC": "C", "TGG": "W", "TTC": "F", "TCG": "S", "TTA": "L", "TTG": "L", "TCC": "S", "ACC": "T", "TCA": "S", "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A" }

function translate(dna){
    var protein = []
    var codons = dna.split(/(...)/);
    for(var i = 0; i < codons.length; i++){
        var codon = codons[i];
        protein.push(codonTable[codon])
    }
    return protein.join("")
}

translate("TCTATTATGCAGAATATTTCTGGTCGTGAGGCTACT")
```


### I was promised Functional Programming!
```javascript
codonTable = { "CTT": "L", "ATG": "M", "ACA": "T", "ACG": "T", "ATC": "I", "ATA": "I", "AGG": "R", "CCT": "P", "AGC": "S", "AGA": "R", "ATT": "I", "CTG": "L", "CTA": "L", "ACT": "T", "CCG": "P", "AGT": "S", "CCA": "P", "CCC": "P", "TAT": "Y", "GGT": "G", "CGA": "R", "CGC": "R", "CGG": "R", "GGG": "G", "GGA": "G", "GGC": "G", "TAC": "Y", "CGT": "R", "GTA": "V", "GTC": "V", "GTG": "V", "GAG": "E", "GTT": "V", "GAC": "D", "GAA": "E", "AAG": "K", "AAA": "K", "AAC": "N", "CTC": "L", "CAT": "H", "AAT": "N", "CAC": "H", "CAA": "Q", "CAG": "Q", "TGT": "C", "TCT": "S", "GAT": "D", "TTT": "F", "TGC": "C", "TGG": "W", "TTC": "F", "TCG": "S", "TTA": "L", "TTG": "L", "TCC": "S", "ACC": "T", "TCA": "S", "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A" }

function ftranslate(dna){
    return dna.replace(/.../g, function(codon){ return codonTable[codon] })
}

ftranslate("TCTATTATGCAGAATATTTCTGGTCGTGAGGCTACT")
```
That's right. Functions are first-class objects, and can be passed around like any other variable.


### More Functional Programming
```javascript
[1, 2, 3, 4, 5].map(Math.exp)
[1, 2, 3, 4, 5].map(Math.exp).map(Math.log)
[1, 2, 3, 4, 5].reduce(function(result, current, previous, all){return current + result})
```


### But there are also Objects
```javascript
typeof 1
typeof "string"
typeof [1, 2, 3]
typeof {"type": "Object"}
typeof function(args){console.log(args)}
```

Yes, Array is an Object, not its own type.


 ### Gotcha - Beware thy primitive types
 ```javascript
 typeof new Number(5)
 typeof new String("In a box")
 ```



### Prototypes
All JavaScript types have a `prototype`, an object that defines how they are created. When you create an object with the `new` operator, you're creating a new base `Object` type as a new *object*, adding the desired type's `prototype` to it, and running any constructor logic on the resulting structure.

A `prototype` is just an object, so we can slap on new values and they will automatically be available on all objects that share that prototype


### Teaching a built-in type new tricks
```javascript
console.log([1, 2, 3, 4, 5].sum === undefined)

Array.prototype.sum = function() {
    var total = 0;
    for(var i = 0; i < this.length; i++){
        total += this[i];
    }
    return total
}

console.log([1, 2, 3, 4, 5].sum())
```
I had to write a pretty unpleasant looking summation by hand with `Array.reduce` earlier. If I find I will be doing that often, I would rather write something legible.


### What is This?
```javascript
console.log(this)
Object.prototype.greet = function() { console.log(this, " says Hello") }
{}.greet()
[].greet()
```
In the normal, "unbound" context, `this` refers to the top-level `Window` object, also referenced by `window`.

When evaluating a function bound to an object or its prototype, `this` refers to the calling object


### Binding a function
You can bind a function to an object without adding it to the prototype by using the `Function` method `bind`.
```javascript
pi = new Number(Math.PI)
pi.concat = [1, 2, 3, 4].concat.bind(pi)
pi.concat(5)
```

Now, `pi` has a `concat` function, forever more


### What if you don't want forever?
```javascript
Math.max.apply(null, [1, 2, Number.MAX_VALUE + 1, 12, Infinity, 12])
//Note this doesn't work
Math.max([1, 2, Number.MAX_VALUE + 1, 12, Infinity, 12])
//But this does
Math.max(1, 2, Number.MAX_VALUE + 1, 12, Infinity, 12)
```
`Function.apply` takes 2+ parameters. The first is the value of `this` for a single evaluation, and the rest are passed as parameters.


### Special `arguments`
```javascript
debugArgs = function(){
    console.log(arguments)
}
debugArgs("foo", "bar", 1, 2, "baz", "bzip2", {"icon": "32 bit א"})
```
All arguments passed can be accessed by the special `arguments` Array-like object, even if there is no name for them listed in the function's definition.

`Math.max` and the like take its arguments from this list, and by passing an array to `call` as the second parameter, that array is used in its place.


### A better *Class* of String
```javascript
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

dna = new DNASequence("TCTATTATGCAGAATATTTCTGGTCGTGAGGCTACT")
```


### Hereditary Traits
```javascript
RNASequence = function(sequence){
    DNASequence.call(this, sequence)
    this.translate = undefined;
}
RNASequence.reverseTranscribe = function(dnaSequence){
    seq = dnaSequence.sequence.split("").reverse().join("").replace("T", "U")
    return new RNASequence(seq)
}

rna = RNASequence.reverseTranscribe(dna)
console.log(rna.reverseTranscribe, rna.translate)
```

Here, traits are passed on by the constructor.


### Prototype as Template
```javascript
ProteinSequence = function(sequence){
    this.sequence = sequence
}
ProteinSequence.prototype = Object.create(DNASequence.prototype)
protein = new ProteinSequence("SIMQNISGREAT")
protein.toString()
console.log(protein.translate)
```
Here, traits are passed on by the prototype.


### JavaScript Standard Library Resources
-[The Mozilla Developers Network Javascript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
-[W3C Schools JavaScript Reference](http://www.w3schools.com/js/default.asp)

If you want a function but don't know if it exists, check one of these first.


### Now you try it
Try one of the following:
- Implement a Fasta File Format Parser (We'll see one or two implementations of these later)
- Define a **dot product** function for `Arrays`
- Add a `translate` method to `RNASequence`
- Make something up!
