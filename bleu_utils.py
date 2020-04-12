from nltk.translate.bleu_score import sentence_bleu

def get_references_and_candidate(filename, rows_length):
    list_all = []
    with open(filename, 'r', encoding='utf-8') as f:
        for i in range(0, rows_length):
            line = f.readline().rstrip()
            line_arr = line.split('	')
            in_list = [line_arr[0], line_arr[1]]
            list_all.append(in_list)
        return list_all

def cal_bleu(reference, candidate):
    ref_arr = reference.split(' ')
    can_arr = candidate.split(' ')
    score = sentence_bleu([ref_arr], can_arr)
    return score


def evaluate(param):
    return "test", "test", "test"


def cal_sum_bleu(filename,startnum,endnum):
    score = 0
    list_all = get_references_and_candidate(filename,endnum)
    for i in range(startnum,endnum):
        result, sentence, attention_plot = evaluate(list_all[i][1])
        res = result[:-9]+result[-8]
        score_now = cal_bleu(list_all[i][0].replace("'", " ").upper(),res.upper())
        score += score_now
        if(i%100 == 0):
          print(list_all[i][0] + ' ---- ' +res)
          print(score_now)
    score /= endnum-startnum
    return score