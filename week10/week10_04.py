#week10_04.py
myfile = "c:\\s202444074\\lyh_02.txt"

# type1
f = open(myfile, 'r')
pass # 작업
f.close()


# type2 with문을 벗어나는 순간 close가 자동으로 작동
with open(myfile, 'r') as f:
    pass # 작업
