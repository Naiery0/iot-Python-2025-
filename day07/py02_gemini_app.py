# Tkinter를 클래스화

from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyD6BAUfjcedoPG7Pq-RunFAp2CAW2YmZrU')
model = genai.GenerativeModel('gemini-1.5-flash')

class window(Tk):
    def __init__(self):
        super().__init__()
        self.title('제이나이 챗봇 v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/chatbot.ico')

        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initWindows()

    def onClosing(self):
        if askyesno('종료확인', '종료하시겠습니까?'):
            self.destroy()
     


    def initWindows(self):
        # 7. 전체에서 사용할 폰트 지정 -> 나눔고딕
        self.myFont = Font(family='NanumGothic', size=10, weight=BOLD)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

        # 2. UI 화면
        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        # 3. inputFrame에 들어갈 Entry와 Button
        self.textMesssage = Text(self.inputFrame, width=75, height=1, wrap=WORD, font=self.myFont)
        self.textMesssage.pack(side=LEFT, padx=15)
        self.textMesssage.bind('<Key>', self.keypress)
        
        # 5. API 호출 결과 메시지 출력될 스크롤기능 텍스트위젯 추가
        self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='#ffffff', font=self.myFont)
        self.textResult.pack(fill=BOTH, expand=True)
        # 10. 스크롤텍스트에 나올 메시지 디자인
        self.textResult.tag_configure('user', font=self.myFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.myFont, foreground='limegreen')
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')

        self.buttonSend = Button(self.inputFrame, text='전송', bg='#8f8f8f', fg= 'white', font=self.myFont,
                            command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=20, pady=5)

        # 9. 실행 후 바로 입력창에 포커스가 가도록
        self.textMesssage.focus_set()    

    # 4. 전송버튼 이벤트, 제미나이 실행
    def responseMessage(self): 
        # showinfo('실행', 'API를 실행합니다!')
        self.inputText = self.textMesssage.get('1.0', END)
        # print(self.inputText)
        # shoinfo(inputText) # 다이얼로그, 모달 창
        if self.inputText:
            try:
                self.textResult.insert(END, '유저: ', BOLD)
                self.textResult.insert(END, f'{self.inputText}\n\n', 'user')

                response = model.generate_content(self.inputText)

                self.textResult.insert(END, '챗봇: ', BOLD)
                self.textResult.insert(END, f'{response.text}\n\n', 'ai') # 'ai' -> 텍스트 아규먼트    
                # print(response.text)
            except Exception as e:
                self.textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
            finally:
                self.textMesssage.delete('1.0', END) # 입력창 글 지우기
                self.textResult.see(END)
                # 8. textMesssage 위젯에서 엔터를 치면 전송버튼이 클릭
    def keypress(self, event):
        # print(repr(event.char)) # 키 값 알아내기
       if event.char == '\r':
            self.responseMessage()

           
if __name__ == '__main__':
    app=window()
    app.mainloop()
