# week12_07.py

import week12_06 as m
from week12_06 import PI  # 안에 있는 변수도 직접 가져와야 하는 듯
from week12_06 import PI as pi

print(m.PI)
print(PI)
print(pi)
print(m.add(m.PI, 4.4))  # 위에서 import한 방법에 따라 변수 이름 조심
obj = m.Math()
print(obj.solv(2))

print("="*20)

from week12_06 import Math

ob = Math()
print(ob.solv(2))  # 인스턴스를 통한 호출

print("="*20)

print(Math.solv(2))  #클래스를 통한 호출이라서 안 된다고 하는데 잘 모르겠음
