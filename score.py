
import sys
from nltk.translate.bleu_score import sentence_bleu

# print("Output from Python") 
sentence1 = sys.argv[1]
sentence2 = sys.argv[2]
sentence1 = sentence1.split(' ')
sentence2 = sentence2.split(' ')

reference = [sentence1]
score = sentence_bleu(reference, sentence2)
print(score)

