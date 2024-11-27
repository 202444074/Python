# week13_B_08_1.py
# id:20240000
# name:jang eunmee

from datetime import datetime as dt
import os

dtformat = "%Y-%m-%d %H:%M:%S"


def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    mydir = "c:\\car1_24000001"
    myfile = "list.txt"
    myfullfile = os.path.join(mydir, myfile)

    if not os.path.isdir(mydir):
        os.mkdir(mydir)

    cars = []

    # read 작업해야 할 곳!
    # 파일이 있는지 확인
    # 있으면 파싱, 없으면 그대로 밑으로 떨어지면 됨.

    while True:
        number = input("차량번호:").strip()
        if not number:
            break

        while True:
            try:
                intime = input("입차시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
            except:
                pass

        while True:
            try:
                outtime = input("출차시간:").strip()
                if not outtime:
                    outtime = None
                    break
                outtime = dt.strptime(outtime, dtformat)
                break
            except:
                pass

        car = {"num": number, "in": intime, "out": outtime}
        cars.append(car)

    for car in cars:
        print(car["num"], car["in"], car["out"])
        print(diff_seconds(car["in"], car["out"]))

    with open(myfullfile, "w", encoding="utf-8") as f:
        for car in cars:
            num = car["num"]
            intime = dt.strftime(car["in"], dtformat)
            outtime = dt.strftime(car["out"], dtformat) if car["out"] else ""
            f.write(f"{num}|{intime}|{outtime}\n")

