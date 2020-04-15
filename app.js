
var express = require('express'); 
var app = express(); 
var port = 3005;

  
// Function callName() is executed whenever  
// url is of the form localhost:3000/name 
app.get('/score', callName); 
  
function callName(req, res) { 
      console.log(req.query);
    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3005/score?val1=Mike&val2=Will 
    var process = spawn('python',['./score.py', req.query.val1, req.query.val2]); 
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
    process.stdout.on('data', function(data) { 
        res.send(data); 
    } ) 
} 

app.listen(port, function() { 
    console.log('server running on port ', port); 
});