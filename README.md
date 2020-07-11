Pypi 만들기
-----

Python으로 작업한 결과를 배포하는 연습을 하기 위해 생성한 repo 입니다.
- 연습목적으로 작성한 코드와 네이밍이 포함되어 있으므로 참고만 해주시기 바랍니다.

## Steps

### 1. 가상 환경 구축 및 gitignore
Python 가상 환경 구축을 우선 한 뒤, 불필요한 항목이 commit 되지않도록 사전 작업을 합니다.
- 가상 환경 구축은 Pycharm으로 손쉽게 하였습니다. 이렇게 하면 setuptools가 기본으로 설치되어 있습니다.
- Pycharm이 아닐경우 virtualenv를 사용하면 됩니다.
- .gitignore는 https://www.toptal.com/developers/gitignore 참고

### 2. 배포를 위한 간단한 코드 작업
배포 후에 import 하여 사용할 코드를 작성 합니다. 이 단계는 생략해도 무방하나, 진행하였습니다.

간단한 계산기를 만들었습니다.
```python
class Calculator:
    def __init__(self):
        pass

    def sum(self, a, b):
        sum_result = a + b

        return sum_result

    def sub(self, a, b):
        sub_result = a - b

        return sub_result

    def mul(self, a, b):
        mul_result = a * b

        return mul_result

    def div(self, a, b):
        try:
            div_result = a // b

            return div_result

        except Exception as e:
            print(e)
            return False
```

### 3. Setup.py 생성 및 코드 작성
setup.py를 생성 합니다.

```bash
touch setup.py
```

setup.py에 필요한 정보를 입력합니다.
- 참고 문서를 바탕으로 custom하여 작성하였습니다.

```python
from setuptools import setup, find_packages

setup(
    name='intotherain',
    version='0.0.2',
    description='Basic Calculator',
    author='timetobye',
    author_email='secret@secret.com',
    url='https://github.com/timetobye/Make_pypi_practice',
    packages=find_packages(exclude=['docs', 'test.py']),
    install_requires=[],
    keywords=['practice', 'temp_practice'],
    python_requires='>=3'
)
```
### 4. setup.cfg
setup.cfg는 configuration 파일입니다.
- setuptools는 setup.py 대신 setup.cfg 라는 configuration 파일로 대신 setuptools.setup() 의 옵션을 지정하는 것을 허용
- 아래와 같이 생성하고 내용을 넣어주면 된다. 보통 README.md를 넣는듯

```bash
touch setup.cfg
```

```bash
-- setup.cfg

[metadata]
description-file = README.md
```

### 5. 빌드 설정
우선 필요한 라이브러리 설치 진행

```bash
pip install wheel
```

setup.py가 있는 위치에서 아래 명령어를 실행

```bash
python3 setup.py bdist_wheel
```

### 6. 배포
배포 작업에 앞서 두 가지를 진행한다.
- twine을 설치
- https://pypi.org/ 에서 회원 가입 - 인증까지 완료

```bash
pip install twine
```

배포는 아래와 같이 진행한다.
- https://pypi.org/ 에 등록한 아이디와 비밀번호를 입력한다.

```bash
twine upload dist/파일 이름.whl
```

동일한 이름이 있으면 에러가 난다. 그럴 경우 setup.py에서 변경을 해줘야 한다.

## 실제 설치

이제 업로드가 완료 되었으니 설치를 해보자.

## Installation
```bash
pip install intotherain
```

```python

from Calculator import Calculator

a, b = 5, 10

cal = Calculator.Calculator()
print(cal.sum(a, b))
print(cal.sub(a, b))
print(cal.mul(a, b))
print(cal.div(a, b))

```

```bash
(venv) [iMac]:~/PycharmProjects/Howtomake_pypi$ python3 tests/test.py 
15
-5
50
0
```

정상적으로 설치가 완료됐고, 계산기능도 사용이 가능하다.

기타 사항
- 0.0.1 버전을 만들 때 이슈가 있었는데, 처음부터 다시 진행을 해서 설치하였음

참고 문서
- [파이썬 package 배포 하기](https://rampart81.github.io/post/python_package_publish/)
- [파이썬 PIP Install 패키지 만들어보기](https://medium.com/@onlytojay/%ED%8C%8C%EC%9D%B4%EC%8D%AC-pip-install-%ED%8C%A8%ED%82%A4%EC%A7%80-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EA%B8%B0-42ea68f4fabd)
- [Deep Dive into pip - 2](https://suhwan.dev/2018/10/30/deep-dive-into-pip-2/)