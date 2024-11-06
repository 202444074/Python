# 기말에 폴더관련 중요  / 절대경로 상대경로 조금 알고있기
# 9주차 ppt 4페이지 열기 → 처리 → 파일 파일이 아니라 닫기임
# .strip  .lower 같은 메소드는 파일에서 다시 사용해야하기 때문에 주의
# 9주차 15페이지 중요 코드 다 알고있기 9주차에서 아마 가장 중요
# 기말에 파일 읽어서 class로 만든 타입으로 변환시키는 방식으로 나옴

# week10_01.py
myfile = "c:\\s202444074\\lyh.txt"


# 1. 열기
# f = open(myfile, 'w')  # 쓰기모드(덮어쓰기) / 파일을 제어할 권한을 f에게 줌 
# f = open(myfile, 'a')  # 추가모드 (없으면 새로만들기)

# 2. 작업
f.write('이영희\n')
# print(f.read())

# 3. 닫기
f.close()




f = open(myfile, 'r')  # 읽기모드
print(f.read())
f.close()
