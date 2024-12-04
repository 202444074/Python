def test():
    raise NotImplementedError("test함수 미작성")  #except Exception as e:에 묶여서 중단은 안 되고 "test함수 미작성"만 출력됨

while True:
    try: # 에러가 있을 것 같은 코드를 넣어서 실행함
        dvd = int(input("피제수:"))
        dvs = int(input("제수:"))
        result = dvd/dvs
        print(result)
        test()
    except ValueError: # 에러 종류에 따라 대처방법
        print("올바른 값을 넣어")
    except ZeroDivisionError:
        print("제수는 0을 넣으면 안돼")
    except Exception as e: # 다른 모든 에러가 발생할때 에러 메세지를 출력함
        print(e)
    else: # try에 에러가 없어서 모두 실행하면 얘도 실행
        print("try문이 완벽히 실핼하면 할 것")
    finally: # 항상 실행하는 블록
        print("안녕히 계세요")
#except:는 모든 에러를 검출함 except Exception as e:는 에러 객체를 다뤄서 위처럼 사용할 수 있어서 유용함

file = "c:/abc/abc.txt"

f = None
try:
    f = open(file, "r")
except:  # 모든 에러를 처리함
    print(file, "이 없어요.")
finally:
    if f != None:  # 파일이 있어서 파일이 열렸다면 닫아야 하니까 if문 달아줌
        f.close()
