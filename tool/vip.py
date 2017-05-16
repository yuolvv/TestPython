'''
    各大视频网站VIP视频播放
'''
from tkinter import *
from tkinter import ttk
import webbrowser

def view():
    root = Tk()
    #root.withdraw()
    root.title('VIP视频播放')
    width = 650
    height = 280
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(width=False, height=False)

    l_url= Label(root,text='VIP视频地址')
    l_url.grid(row=0,sticky=W,padx=20,pady=10)
    e_url = Entry(root,width=100)
    e_url.grid(row=0,column=1,sticky=W)

    l_release = Label(root,text='视频播放源：')
    l_release.grid(row=1,sticky=W,padx=20,pady=10)

    rversion = StringVar()
    verChosen = ttk.Combobox(root,textvariable=rversion,width=10,state='readonly')
    verChosen['values'] = ('视频播放源1','视频播放源2','视频播放源3','视频播放源4','视频播放源5')
    verChosen.grid(row=1,column=1,sticky=W)
    verChosen.current(0)

    def query():
        if verChosen.get() == "视频播放源1":
            url = "http://www.wmxz.wang/video.php?url=" + e_url.get()
        elif verChosen.get() == "视频播放源2":
            url = "http://api.47ks.com/webcloud/?v=" + e_url.get()
        elif verChosen.get() == "视频播放源3":
            url = "http://q.z.vip.totv.72du.com/?url=" + e_url.get()
        elif verChosen.get() == "视频播放源4":
            url = "http://www.yydy8.com/Common/?url=" + e_url.get()
        elif verChosen.get() == "视频播放源5":
            url = "http://yyygwz.com/index.php?url=" + e_url.get()

        webbrowser.open(url,new=0,autoraise=True)

    b_query = Button(root, text="立刻播放", command=query)
    b_query.grid(row=2, sticky=W, padx=20)

    l_note = Label(root, text='使用教程：')
    l_note.grid(row=3, sticky=W, padx=20, pady=10)
    l_note1 = Label(root, text='1.将观看的VIP视频地址粘贴到上面的文本框中;')
    l_note1.grid(row=4, columnspan=2,sticky=W, padx=20)
    l_note2 = Label(root, text='2.选择合适的视频播放源;')
    l_note2.grid(row=5, columnspan=2,sticky=W, padx=20)
    l_note3 = Label(root, text='3.点击立即播放，则使用默认的浏览器打开免会员播放地址。')
    l_note3.grid(row=6, columnspan=2,sticky=W, padx=20)

    l_note4 = Label(root, text='软件版权所有：@听风吟且行，软件官网：http://www.iyu.pub')
    l_note4.grid(row=7, columnspan=2,sticky=W, padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    view()





