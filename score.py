
import sys
from nltk.translate.bleu_score import sentence_bleu

# print("Output from Python") 

sentence1 = sys.argv[1]
sentence2 = sys.argv[2]
arr1 = sentence1.split(' ')
arr2 = sentence2.split(' ')

score = sentence_bleu(arr1, arr2)
print(score)

