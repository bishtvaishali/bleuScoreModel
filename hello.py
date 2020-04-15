
import sys
from nltk.translate.bleu_score import sentence_bleu
# Takes first name and last name via command  
# line arguments and then display them 
print("Output from Python") 

print("First name: " + sys.argv[1]) 
print("Last name: " + sys.argv[2])

sentence1 = sys.argv[1]
sentence2 = sys.argv[2]
sentence1 = sentence1.split(' ')
sentence2 = sentence2.split(' ')

reference = [sentence1]
score = sentence_bleu(reference, sentence2)
print('##  The BLEU score is: ',score)

