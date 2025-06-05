import csv
import os
import tkinter as tk
from tkinter import ttk
import random

csvpath = os.getcwd()
print(csvpath)
csvpath2 = csvpath+r"/hamu.csv"
print(csvpath2)
#csvpath = r'C:\RICOH'
with open(csvpath2) as file:
    lsts = list(csv.reader(file))
    #print(lsts)

""""""""""""""""""""""""'https://syachiku.net/pythontkintertree/'""""""""""""""""""""""""
#背景色交互にして
#意味のフォントを変えて見やすく（細めの明朝とか？）
#縦線入れたい

class viewer:
    def __init__(self, viewer_title, windowx, windowy, viewer_size, sortlever, startquiz):
        self.viewer_title=viewer_title
        self.windowx=windowx
        self.windowy=windowy
        self.viewer_size=viewer_size
        self.sortlever=sortlever
        self.startquiz=startquiz
        self._create_root()
        self._create_tree()
        self._create_scroll()
        self._create_separator()
        self._create_sbutton()
        self._create_qbutton()
        self._insert_word()
        self.sbutton.configure(text="ソート切り替え")
        self.root.mainloop()

    def _create_root(self):
        self.root=tk.Tk()
        self.root.title(self.viewer_title)
        self.root.geometry(self.viewer_size)
        self.root.configure(background="#030200")
        print(type(self.viewer_size))
        
    def _create_tree(self):
        self.style=ttk.Style()
        self.style.layout("Treeview.Heading",[("Treeheading.cell",{"sticky":"nswe","children":[("Treeheading.padding",{"sticky":"nswe","children":[("Treeheading.image",{"side": "right", "sticky": ""}),("Treeheading.text", {"sticky": "we"}),]})]})])
        self.style.configure("Treeview.Heading", font=("Meiryo UI", 13, "bold"), background="#FFAF37")
        self.style.configure("Treeview", font=("BIZ UDP明朝 Medium", 11))
        self.tree=ttk.Treeview(self.root, height=int(self.windowy*0.0440))
        self.tree['columns']=('word1', 'mean1', 'word2', 'mean2')
        self.tree.column('#0', width=0, stretch='no')
        self.tree.column('word1', width=int(self.windowx*0.21875), anchor='w')
        self.tree.column('mean1', width=int(self.windowx*0.21875), anchor='w')
        self.tree.column('word2', width=int(self.windowx*0.21875), anchor='w')
        self.tree.column('mean2', width=int(self.windowx*0.21875), anchor='w')

        self.tree.heading('word1', text='単語', anchor='w')
        self.tree.heading('mean1', text='意味', anchor='w')
        self.tree.heading('word2', text='単語', anchor='w')
        self.tree.heading('mean2', text='意味', anchor='w')

        self.tree.place(x=self.windowx*0.035, y=self.windowy*0.02778)
    
    def _create_scroll(self):
        def upsc():
            self.tree.yview("moveto", 0)
        def dwsc():
            self.tree.yview("moveto", 10)
        self.upscroll=tk.Button(self.root, command=upsc, text="↑", bg="#FFEDD1", font=("Meiryo UI", 13, "bold"))
        self.dwscroll=tk.Button(self.root, command=dwsc, text="↓", bg="#FFEDD1", font=("Meiryo UI", 13, "bold"))
        self.upscroll.place(x=self.windowx*0.91, y=self.windowy*0.02734, width=self.windowx*0.05, height=self.windowy*0.45)
        self.dwscroll.place(x=self.windowx*0.91, y=self.windowy*0.47851, width=self.windowx*0.05, height=self.windowy*0.45)

    def _create_separator(self):
        self.sepa=ttk.Separator(self.root, orient='vertical')
        self.sepa.place(x=self.windowx*0.46, y=self.windowy*0.02916, height=self.windowy*0.900, width=5)
        
        self.sepa2=ttk.Separator(self.root, orient='vertical')
        self.sepa2.place(x=self.windowx*0.25, y=self.windowy*0.02916, height=self.windowy*0.900, width=2)
        
        self.sepa3=ttk.Separator(self.root, orient='vertical')
        self.sepa3.place(x=self.windowx*0.69, y=self.windowy*0.02916, height=self.windowy*0.900, width=2)

    def _create_sbutton(self):
        self.sbutton=tk.Button(self.root, command=self._insert_word, font=("Meiryo UI", 10), width=10, bg="#FFDEAD")
        self.sbutton.place(x=self.windowx*0.22916, y=self.windowy*0.93889)
        
    def _create_qbutton(self):
        self.qbutton=tk.Button(self.root, text="tk.Button", command=self.startquiz, font=("Meiryo UI", 10), width=10, bg="#FFDEAD")
        self.qbutton.place(x=self.windowx*0.58333, y=self.windowy*0.93889)

    
    def _insert_word(self):
        self.tree.delete(*self.tree.get_children())
        i=0
        n=0
        if self.sortlever==1:
            self.sbutton.configure(text="単語順")
            for lst in lsts:
                if i%2==0:
                    wd1=lst[1]
                    me1=lst[2]
                    i+=1
                else :
                    if n%2==0:
                        wd2=lst[1]
                        me2=lst[2]
                        self.tree.insert(parent='', index='end', iid=i, values=(wd1,me1,wd2,me2), tags="whit")
                        i+=1
                        n+=1
                    else:
                        wd2=lst[1]
                        me2=lst[2]
                        self.tree.insert(parent='', index='end', iid=i, values=(wd1,me1,wd2,me2), tags="gray")
                        i+=1
                        n+=1
                if i==132:
                    break
                self.tree.tag_configure("whit", background="#ECECEC")
                self.tree.tag_configure("gray", background="#CFCFCF")
                self.tree.heading('word1', text='単語▼', anchor='w')
                self.tree.heading('mean1', text='意味', anchor='w')
                self.tree.heading('word2', text='単語▼', anchor='w')
                self.tree.heading('mean2', text='意味', anchor='w')
                self.sortlever=0
        else:
            self.sbutton.configure(text="意味順")
            for lst in lsts[132:]:
                if i%2==0:
                    wd1=lst[1]
                    me1=lst[2]
                    i+=1
                else :
                    if n%2==0:
                        wd2=lst[1]
                        me2=lst[2]
                        self.tree.insert(parent='', index='end', iid=i, values=(wd1,me1,wd2,me2), tags="whit")
                        i+=1
                        n+=1
                    else:
                        wd2=lst[1]
                        me2=lst[2]
                        self.tree.insert(parent='', index='end', iid=i, values=(wd1,me1,wd2,me2), tags="gray")
                        i+=1
                        n+=1
                if i==264:
                    break
                self.tree.tag_configure("whit", background="#ECECEC")
                self.tree.tag_configure("gray", background="#CFCFCF")

                self.tree.heading('word1', text='単語', anchor='w')
                self.tree.heading('mean1', text='意味▼', anchor='w')
                self.tree.heading('word2', text='単語', anchor='w')
                self.tree.heading('mean2', text='意味▼', anchor='w')
                self.sortlever=1


class quizer(viewer):
    def __init__(self, quizer_title, pagex, pagey, quizer_size):
        self.quizer_title=quizer_title
        self.pagex=pagex
        self.pagey=pagey
        self.quizer_size=quizer_size
        self.pa = 0
        self._create_page()
        self._create_page_button()
        self._create_page_frame()
        self._create_page_quiz()
        self._create_page_answer()
        self.page.mainloop()

    def _create_page(self):
        self.page=tk.Tk()
        self.page.title(self.quizer_title)
        self.page.geometry(self.quizer_size)
        self.page.configure(background="#030200")
        print(type(self.quizer_size))
    
    def _create_page_button(self):
        def answ():
            if self.page_answ.cget("text")=="・・・":
                self.page_answ.configure(text="ああああああああああああああああああ")
            elif self.pa==0:
                print(0)
                self.page_answ.configure(fg="#FFFFFF")
                self.pa=1
            else:
                print(1)
                self.page_answ.configure(fg="#030200")
                self.pa=0

        def next():
            self.pa=0;self.page_answ.configure(fg="#030200");self.page_quiz.configure(fg="#FFBB00")
            RNG = random.randint(0,131)
            print(lsts[0][1],"～",lsts[131][1])
            print(f"quiz:{lsts[RNG][1]}")
            print(f"answ:{lsts[RNG][2]}")
            self.page_quiz.configure(text=f"{lsts[RNG][1]}")
            self.page_answ.configure(text=f"{lsts[RNG][2]}")
            if RNG==131:
                self.page_quiz.configure(fg="#B90000")
                self.page_answ.configure(fg="#B90000")

        def clos():
            self.page.destroy()
        self.answbut=tk.Button(self.page, bg="#FFEDD1", font=("Meiryo UI", 12), command=answ, text="答へ", )
        self.nextbut=tk.Button(self.page, bg="#FFEDD1", font=("Meiryo UI", 12), command=next, text="次へ", )
        self.closbut=tk.Button(self.page, bg="#FFEDD1", font=("Meiryo UI", 10), command=clos, text="閉じる", )

        self.answbut.place(x=5,y=220,width=250, height=65)
        self.nextbut.place(x=258,y=220,width=250, height=65)
        self.closbut.place(x=434,y= 20,width=60, height=50)

    def _create_page_frame(self):
        self.page_frame=tk.Frame(self.page, bg="#030200", width=350, height=200)
        self.page_frame.propagate(False)
        self.page_frame.pack(pady=20)

    def _create_page_quiz(self):
        self.page_quiz=tk.Label(self.page_frame, text="とっとこ単語帳", bg="#030200", fg="#FFBB00", font=("BIZ UDPゴシック", 35))
        self.page_quiz.pack(pady=40)

    def _create_page_answer(self):
        self.page_answ=tk.Label(self.page_frame, text="yep", bg="#030200", fg="#030200", font=("BIZ UDP明朝 Medium", 20))
        self.page_answ.pack(pady=10)


def start_quiz():
    pagex=512
    pagey=288
    quiz = quizer(quizer_title='hamu', 
                  pagex=512,
                  pagey=288,
                  quizer_size=f'{pagex}x{pagey}'
                  )
    
windowx=576
windowy=1024
view = viewer(viewer_title='hamu', 
              windowx=576,
              windowy=1024,
              viewer_size=f'{windowx}x{windowy}', 
              sortlever=1,
              startquiz=start_quiz
              )
        

#クイズ画面出すdefをclass外に作ってviewer内のボタンのコマンドに指定したらいけないかな？


