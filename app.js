
var express = require('express'); 
var app = express(); 
var port = 3005;
var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', function(req,res){
    res.send('Welcome to BLEU Score server');
})
  
app.post('/score', calculateScore); 
  
function calculateScore(req, res) { 
    // console.log('body', req.body);

    var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
    var py = spawn('python',['./score.py', JSON.stringify(req.body)]); 
    let result = '';
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object 
    py.stdout.on('data', function(data) { 
        result += data.toString();
    })
    
    /*Once the stream is done (on 'end') log the received data to the console.*/
    py.stdout.on('end', function(){
        console.log('score: ',result);
        res.send(result);
    });

    py.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
    });
} 

app.listen(port, function() { 
    console.log('server running on port ', port); 
});