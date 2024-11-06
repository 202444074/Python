#week10_03.py

myfile = "c:\\s202444074\\lyh_02.txt"


f = open(myfile, 'r')

#type1 가장 단순하지만 모두 가져옴
#d = f.read()
#print(d)

#type2 위를 주석처리하지 않으면 위가 텍스트를 모두 읽어 실행 안됨
'''
while True:
    d = f.readline()
    if not d:
        break
    print(d.strip())  # 줄사이 공백 없앰
'''

#type3
d = f.readlines()  # 리스트 형태로 가져옴
for line in d:
    print(line.strip())


f.close()
