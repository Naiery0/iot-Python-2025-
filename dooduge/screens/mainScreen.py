# 두더지게임?

from tkinter import *
from tkinter.messagebox import * # 닉네임 입력
from tkinter.scrolledtext import * # 랭킹 도식
from tkinter.font import * # 폰트용

class mainScreen(Tk):
    def __init__(self):
        super().__init__()
        self.title('두더지를 잡자')
        self.geometry('800x600')
        
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initScreen()

    def onClosing(self):
        if askokcancel('종료확인', '종료하시겠습니까?'):
            self.destroy()

    def initScreen(self):
        # 프레임
        self.mainFrame = Frame(self, width=800, height=600, bg='black')
        self.mainFrame.pack()
        self.titleFrame = Frame(self.mainFrame, width=800, height=250, bg='yellow')
        self.titleFrame.pack()
        self.buttonFrame = Frame(self.mainFrame, width=800, height=350, bg='red')
        self.buttonFrame.pack()

        # 게임 타이틀

        # 시작 버튼
        self.startButton = Button(self.buttonFrame, text='게임 시작', bg='gray', fg='black')
        self.startButton.pack() # 엥?


if __name__ == '__main__':
    app=mainScreen()
    app.mainloop()



#     root.protocol('WM_DELETE_WINDOW', onClosing)
# root.mainloop()