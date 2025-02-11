# py01_gpt_clone.py
# 


from tkinter import * # tkinter 모듈에 있는 모든 클래스, 함수, 변수 등을 다 쓰겠다
from tkinter.messagebox import * # 모듈이라 위에서는 안 가져온대 (tkinter가 이렇고 아닌 애들도 있음)
from tkinter.scrolledtext import *
from tkinter.font import *
# 제미나이를 위한 모듈
import google.generativeai as genai

# 6. 제미나이 API용 구성
genai.configure(api_key='AIzaSyD6BAUfjcedoPG7Pq-RunFAp2CAW2YmZrU')
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. 전송버튼 이벤트, 제미나이 실행
def responseMessage(): 
    # showinfo('실행', 'API를 실행합니다!')
    inputText = textMesssage.get('1.0', END).replace('\n', '').strip()
    # print(inputText)
    # shoinfo(inputText) # 다이얼로그, 모달 창
    if inputText:
        try:
            textResult.insert(END, '유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user')

            response = model.generate_content(inputText)

            textResult.insert(END, '챗봇: ', BOLD)
            textResult.insert(END, f'{response.text}\n\n', 'ai') # 'ai' -> 텍스트 아규먼트    
            # print(response.text)
            textMesssage.delete('1.0', END) # 입력창 글 지우기
            textResult.see(END)
        except Exception as e:
            textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        finally:
            textMesssage.delete('1.0', END) # 입력창 글 지우기
            textResult.see(END)


# 8. textMesssage 위젯에서 엔터를 치면 전송버튼이 클릭
def keypress(event):
    # print(repr(event.char)) # 키 값 알아내기
    if event.char == '\r':
        responseMessage()

# 11. 종료시 이벤트 처리 함수
def onClosing():
    if askokcancel('종료확인', '종료하시겠습니까?'):
        root.destroy()

# 1. 메인 윈도우 생성
root = Tk()
root.title('제미나이 챗봇')
root.geometry('730x450')
# 12. 아이콘 변경
# ./image
root.iconbitmap('chatbot.ico')

# 7. 전체에서 사용할 폰트 지정 -> 나눔고딕
myFont = Font(family='NanumGothic', size=10, weight=BOLD)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

# 2. UI 화면
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF')
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame에 들어갈 Entry와 Button
textMesssage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont)
# 8. 입력창에서 엔터를 치면 keypress 이벤트처리함수 발생시킴
textMesssage.bind('<Key>', keypress)
textMesssage.pack(side=LEFT, padx=15)

buttonSend = Button(inputFrame, text='전송', bg='#8f8f8f', fg= 'white',
                    font=myFont,
                    command=responseMessage)
buttonSend.pack(side=RIGHT, padx=20, pady=5)

# 5. API 호출 결과 메시지 출력될 스크롤기능 텍스트위젯 추가
textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='#ffffff', font=myFont)
textResult.pack(fill=BOTH, expand=True)

# 10. 스크롤텍스트에 나올 메시지 디자인
textResult.tag_configure('user', font=myFont, foreground='yellow')
textResult.tag_configure('ai', font=myFont, foreground='limegreen')
textResult.tag_configure('error', font=boldFont, foreground='red')

# 9. 실행 후 바로 입력창에 포커스가 가도록
textMesssage.focus_set()

# 11. 프로그램 종료 버튼 누를 때 종료 확인 창
root.protocol('WM_DELETE_WINDOW', onClosing)

# 1. 종료까지 계속 실행
root.mainloop()