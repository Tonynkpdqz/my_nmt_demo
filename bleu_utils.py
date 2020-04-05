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


def translate(old_string):
    # only for test
    return 'let it long '+old_string

list_all = get_references_and_candidate('new_spa', 30000)
score = 0
for i in range(30000):
    print(list_all[i][0])
    print(i)
    candidate = translate(list_all[i][0])
    score += cal_bleu(translate(list_all[i][0]), candidate+' test')
print(score)
print(score/30000)
