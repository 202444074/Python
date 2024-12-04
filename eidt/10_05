import os

mypath = "c:\\s202444074"
myfile = "lyh_02.txt"

if False == os.path.exists(mypath):
    os.mkdir(mypath)

myfullfile = mypath + "\\" + myfile

if os.path.exists(myfullfile):
    scores=[]
    with open(myfullfile, 'r') as f:
        lines = f.readlines()
        for line in lines:  # 'm,10|k,90|e,40\n' 형식으로 들어옴 \n 주의, for line in f도 \n 가져옴
            dict_scores = {}
            sub_scores = line.strip().split('|')  # m,10이 하나의 값이 되어 line리스트에 들어감
            for sub_score in sub_scores:  # 'm,10'
                kv = sub_score.split(',')  # ['m', '10']
                dict_scores[kv[0]] = int(kv[1])  # {'m':10}
            if dict_scores:
                scores.append(dict_scores)
    print(scores)
    if scores:
        for score in scores:
            print(score)
else:  # 없으면 만들기, 없을때 어떻게 할지는 자기 선택
    f = open(myfullfile, 'w')
    d.close
