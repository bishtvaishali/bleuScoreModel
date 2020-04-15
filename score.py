
import sys
from nltk.translate.bleu_score import sentence_bleu

# print("Output from Python") 
sentence1 = sys.argv[1]
sentence2 = sys.argv[2]
sentence1 = sentence1.split(' ')
sentence2 = sentence2.split(' ')

# score = sentence_bleu(reference, sentence2)
reference = [sentence1]
candidate = sentence2
score = sentence_bleu(reference, candidate)

onegram = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
twogram = sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0))
threegram = sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0))
fourgram = sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25))
avg = (onegram + twogram + threegram + fourgram)/4

print(score)
print('Cumulative 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
print('Cumulative 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
print('Cumulative 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
print('Cumulative 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))
print('Average: %f' % avg)

