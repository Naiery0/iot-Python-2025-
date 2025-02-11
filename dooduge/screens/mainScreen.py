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

    def onClosing(self):
        if askokcancel('종료확인', '종료하시겠습니까?'):
            self.destroy()





#     root.protocol('WM_DELETE_WINDOW', onClosing)
# root.mainloop()