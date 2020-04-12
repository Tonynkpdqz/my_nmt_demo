from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import corpus_bleu
def cal_bleu(reference, candidate):
    ref_arr = reference.split(' ')
    can_arr = candidate.split(' ')
    score = sentence_bleu([ref_arr], can_arr)
    return score
reference = "I don't like movies.".replace("'", " ").upper()
candidate = "i don t like movies . <end> ".upper()
can = candidate[:-9]+candidate[-8]
print(reference)
print(can)
#score = sentence_bleu(reference, candidate)
#score = corpus_bleu(reference,candidate)
score = cal_bleu(reference, can)

print(score)