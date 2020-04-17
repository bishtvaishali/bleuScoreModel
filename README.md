# Run instructions
- Application runs on port 3005
- For python script to run, Use anaconda prompt
- node app.js/ nodemon app.js

# BLEU SCORE
- POST request : http://localhost:3005/score

body :{
	"sentence" : "Brian Dietzen smiling for the camera",   
	"reference" : ["Brian Dietzen looking at the camera", "Erinn Hayes smiling for the camera"] // list of sentences
}
sentence is the candidate sentence.
reference is the list of sentences for comparison.

Response : Score between 0 to 1.
