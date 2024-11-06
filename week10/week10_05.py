#week10_05.py
import os

mypath = "c:\\s202444074"
myfile = "lyh_02.txt"
'''
if os.path.exists(mypath):
    print("Exist:",mypath)
else:
    os.mkdir(mypath)
'''
if False == os.path.exists(mypath):  # 그냥 파일 없으면 만드는 코드로 바꿈
    os.mkdir(mypath)

myfullfile = mypath + "\\" + myfile

if os.path.exists(myfullfile):
    scores=[]
    with open(myfullfile, 'r') as f:
        lines = f.readlines()
        for line in lines:  # 'm,10|k,90|e,40\n' 형식으로 들어옴 \n 주의
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
