# iot-Python-2025-
IoT 개발자 기초 프로그래밍 언어 리포지토리

## 1일차
- 개발환경 설정
    - 압축, 폰트, 개발용 에디터 설치
        - 반디집 설치(교육, 회사에서 전부 무료)
        - 나눔글꼴 中 D2Coding. 추후 나눔고딕코딩 필요
        - NotePad++ 
    - Visual Studio Code 설치
        - 확장
            - Korean 설치
        - 설정
            - Font Family에 D2Coding 추가, Mouse Wheel Zoom 체크 설정

- 프로그래밍 언어 종류
    - 컴파일러(실행파일 생성)
        - C, C++, C#, Java, ...
    - 인터프리터(소스코드를 바로 실행, 실행파일 無)
        - 파이썬, JavaScript, ...

- Python
    - 파이썬
        - 1990년에 개발한 인터프리터 언어
        - 네덜란드 개발자 귀도 반 로섬
        - 객체지향 프로그래밍 언어(Object Oriented Program)
        - 쉽게 학습할 수 있는 언어

    - 파이썬 개발환경 Pyenv
        - 파이썬 버전을 손쉽게 변경할 수 있는 툴
        - 설치 전, PowerShell(관리자모드), 아래의 명령어 실행
            ```shell
            > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
            ``` 
        - https://pyenv-win.github.io/pyenv-win/ Quick Start 1번 실행
        - pyenv로 파이썬 버전 설치 및 전역설정

    - Visual Studio Code 
        - 확장 Python 설치
        - *.py 파일 생성 후 코딩
        - Ctrl + F5로 실행

## 2일차
- 파이썬 기초
    - 변수
        - `데이터`를 담아서 사용하기 위해
    - 자료형
        - None, int, float, bool, str, list, tuple, dict, set, ...
        - type() 함수로 <class 'str'> 확인 가능
    - 화면입출력: console에서 입력하고 결과 출력하기 위함
        - input(), print()
    - 문자열포맷팅
        - 문자열을 좀 더 깔끔하게 표현하기 위함
        - %s, %d, %f, ...
        - {0}, {1}, {2}, ...
        - f'{name}... {age}'
    - 연산자
        - 사칙연산: +, -, *, /, //, %, **, ()
        - 리스트연산: list[0], list[0:3 + 1]
        - 문자열연산: split(), replace(), strip(), find(), upper(), lower(), ... 

- 깃허브[데스크톱]
    1. **fetch origin**: 리모트 최신 변경사항 확인(중요)
    2. pull: 리모트의 변경사항을 로컬로 내려받기
    3. commit: 로컬, 리모트에 변경사항 저장
    4. push: 로컬의 변경사항을 리모트로 올리기
    

    
## 3일차
- 파이썬 기초
    - 흐름제어
        - if - 참을 기준으로 분기
        - for - 일반적인 반복문
        - while - 참인 조건일 동안 무한 반복
    - 파일입출력
        - open(경로, mode = r | w | a, encoding = 'utf-8')
        - write(), readline()
        - close()
    - 함수
        - f(x) = y
        - 자주 사용할 로직을 묶어놓은 덩어리
        - 함수 호출
        ```python
        def funcName(param):
            # 로직
        ```
    - 객체지향
        - 현실세계와 동일하게 프로그래밍 하겠다는 설계방식
        - 객체의 틀이 되는 클래스 선언
        - 클래스: 명사와 동사의 집합
            - 명사: 멤버변수(속성)
            - 동사: 멤버함수(메서드)

        ```python
        class ClassName:
            # 멤버변수
            def 멤버함수(self, param):
                # 로직
        ```

## 4일차 
- 파이썬 기초
    - 리스트연산 추가
        - append(), insert(index, value), del(list[index]), pop(), sort(), ...
    - 객체지향 다시
        - 모든 클래스의 조상은 object 클래스
        - 클래스 작성 방법
        - 속성(멤버변수)
        - 메서스(멤버함수)
        - 캡슐화 - 멤버변수 폐쇄화 (__멤버변수)
        - 상속 - 상위클래스를 가지고 자식클래스를 만드는 것
        - **추상화**
        - **인터페이스**
        - **다형성**
        - **SOLID 원칙**

    - 모듈, 패키지
        - 모듈: 함수나 클래스 등 자주 사용할 것들을 파이썬 파일로 만든 것
        - 패키지(라이브러리): 모듈을 모아둔 폴더
        - pip: 외부 모듈을 다운로드 받는 명령어
    - 예외처리
        - Exception: 실행 중 비정상 종료되는 현상
    - 디버깅

## 5일차
- 파이썬 기초
    - 예외처리
        - 프로그래밍에서 가장 중요!
        - 예외: 실행 중 발생, 프로그램을 비정상 종료시키는 것
    - 디버깅
        - F9, F5, F10, F11, Shift+F5, 변수탭, 조사식탭
        - 버그를 잡을 때 가장 유용
        - 소스코드를 분석할 때
- 파이썬 응용
    - 토이프로젝트
        - 콘솔앱: My Movie List 

## 6일차
- 파이썬 응용
    - 토이프로젝트
        - 내 영화 앱 수정, 마무리
            - 예외처리: 입력 시 바로 엔터, 입력 시 4개의 아이템을 입력하지 않으면,
            - 화면편집: 검색, 출력 시 데이터 수 표시
            

https://github.com/user-attachments/assets/bca97d38-e7ca-455e-ad57-49dcddf08221
 
 - 파이썬 응용
    - 주피터 노트북 학습
            - 파이썬을 사용, 연구를 목적으로 하는 리포트 작성에 특화된 기술
            - 주피터 프로젝트에서 나온 결과물
            - Ctrl + Shift + P(명령 팔레트) 에서 시작
                - Create: 새 Jupyter 노트북 클릭
                - 무조건 저장 먼저(.ipynb)
            - GUI 학습에는 불리
            - 머신러닝, 딥러닝, 빅데이터분석 시 많이 활용

        - GUI 학습(tkinker)
            - GUI(Graphic User Interface) - 그래픽 사용자 인터페이스
            - CLI(Console Line Interface) - GUI이전에 사용자 인터페이스. 사용이 불편. 사용자가 명령어를 거의 다 외워서 사용
        
        - 파이썬 GUI 라이브러리
            1. PyQt, PySide: 파이썬 최고의 GUI 라이브러리. Qt라는 C/C++ GUI라이브러리를 Python용으로 변경
                - 화려한 UI구성
                - 코딩 다양성
                - 조금 어려움(파이썬 코드와 분리 가능)
                - Qt가 라이센스를 구매 필수, 프리웨어로 변경한 것이 PySide
            2. tkinter: 파이썬에 내장된 GUI 라이브러리.
                - 아주 단순, 학습이 쉬움
                - 파이썬 기본 내장
                - 안 이쁘다
            3. Kivy: 가장 최근에 나온 GUI 라이브러리
                - 안드로이드, iOS 모바일 앱 UI로 사용 가능
                - 모바일 특화로 멀티플랫폼 지원
                - 어렵다
        
        - Tkinker 학습
            - 기본 템플릿
            
            ```python
            from tkinter import *

            root = Tk()
            # 위젯, 이벤트 등이 들어갈 공간
            # Label, Button, Entry, Radiobutton, Checkbutton, Listbox, Frame 등...
            # 위젯.pack()은 필수!
            root.mainloop()
            ```
<!-- 주석-->
<!-- html에서 사용하는 <img>태그로 캡처한 이미지를 추가-->
<img src="./image/py001.png" width="400">

## 7일차
- 파이썬 응용
    - 토이 프로젝트
        - ChatGPT 유사앱 - 구글 제미나이 API
    - 실습
        - 제미나이 챗앱 -> **클래스형태**로 변경 
    

https://github.com/user-attachments/assets/1459b6e1-ae26-4b2f-9f61-2f16270e84e4


    - 실행파일 만들기
        - `pyinstaller` 모듈 설치
            - pip install pyinstaller
        - 실행파일 명령어(터미널에 실행)
            - pyinstaller --onefile 파이썬파일명
            - 같이 실행되는 터미널을 제거하려면
            - pyinstaller --onefile --noconsole 파이썬파일명
            - 아이콘 등의 리소스를 같은 폴더에 복사 필요

## 8일차
- 파이썬 응용  
    - GUI 중 PyGame
        - 기본 윈도우 학습
        - 이벤트 처리
        - 간단한 게임
        - 이미지, 사운드 등 리소스 활용 게임

    - 토이프로젝트 
        - 블록깨기 게임     
        - 공의 위치에 대한 수식
            - x축 방향 계산방법 : $x = r \cdot \cos \theta$
            - y축 방향 계산방법 : $y = r \cdot \sin \theta$
        - 공의 시작방향, 경계부분 문제 해결, 종료 후 다시 시작 로직

<!-- $$ y = r \cdot \sin \theta $$ -->
<img src="./image/py004.gif" width="700" height="450">

## 9일차
- 코딩 테스트