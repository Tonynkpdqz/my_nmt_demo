from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import corpus_bleu
def cal_bleu(reference, candidate):
    ref_arr = reference.split(' ')
    can_arr = candidate.split(' ')
    score = sentence_bleu([ref_arr], can_arr)
    return score
reference = 'this is test'
candidate = 'this is a test'
#score = sentence_bleu(reference, candidate)
#score = corpus_bleu(reference,candidate)
score = cal_bleu(reference, candidate)

print(score)