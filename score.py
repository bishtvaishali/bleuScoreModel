
import sys, json 
from nltk.translate.bleu_score import sentence_bleu

data = sys.argv[1]

data = json.loads(data)
sentence = data['sentence']
reference = data['reference']

# print("Body json->", data)
# print ("reference->", reference) 
# print ("sentence->", sentence)

candidate = sentence.split(' ') 
# print('candidate: ', candidate)

referenceList = []
for i in range(len(reference)): 
    arr = reference[i].split(' ') 
    referenceList.append(arr)
# print('refernceList-> ', referenceList)


score = sentence_bleu(referenceList, sentence)

onegram = sentence_bleu(referenceList, candidate, weights=(1, 0, 0, 0))
twogram = sentence_bleu(referenceList, candidate, weights=(0.5, 0.5, 0, 0))
threegram = sentence_bleu(referenceList, candidate, weights=(0.33, 0.33, 0.33, 0))
fourgram = sentence_bleu(referenceList, candidate, weights=(0.25, 0.25, 0.25, 0.25))
avg = (onegram + twogram + threegram + fourgram)/4
print(avg)

# print('Average: %f' % avg)
# print('score: ', score)
# print('Cumulative 1-gram: %f' % onegram)
# print('Cumulative 2-gram: %f' % twogram)
# print('Cumulative 3-gram: %f' % threegram)
# print('Cumulative 4-gram: %f' % fourgram)

