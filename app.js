
var express = require('express'); 
var app = express(); 
var port = 3001;

  
// Function callName() is executed whenever  
// url is of the form localhost:3000/name 
app.get('/name', callName); 

// app.get('/name', function(req, res) {
//     console.log(req.query);

//     res.send('Hello'); 
//   });
  
  
function callName(req, res) { 
      console.log(req.query);
    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python',["./hello.py", 
                            req.query.firstname, 
                            req.query.lastname] ); 
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
} 

app.listen(port, function() { 
    console.log('server running on port ', port); 
});