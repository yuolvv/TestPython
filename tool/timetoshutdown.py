import time
import os
from tkinter import *
import datetime

class Shut():
    def __init__(self,l_msg,e_hour,e_minute,e_second):
        self.l_msg = l_msg
        self.e_hour = e_hour
        self.e_minute = e_minute
        self.e_second = e_second

    def calctime(self):
        hourtext = self.e_hour.get()
        minutetext = self.e_minute.get()
        secondtext = self.e_second.get()
        d1 = hourtext+':'+minutetext+":"+secondtext

        cur = datetime.datetime.now()
        d2 = str(cur.hour)+':'+str(cur.minute)+':'+str(cur.second)

        date1 = datetime.datetime.strptime(d1,"%H:%M:%S")
        date2 = datetime.datetime.strptime(d2,"%H:%M:%S")
        seconds = (date1 - date2).seconds
        print(seconds)
        return seconds

    def shutdown(self):
        seconds = self.calctime()
        self.l_msg['text'] = '计算机将在'+str(seconds)+'秒后关机'
        #time.sleep(self.seconds)
        #os.system("shutdown -s -t 0")

    def reboot(self):
        seconds = self.calctime()
        self.l_msg['text'] = '计算机将在'+str(seconds)+'秒后重启'
        #time.sleep(self.seconds)
        #os.system("shutdown -r -t 0")

def view():
    root = Tk()

    l_note = Label(root,text='请输入关机的时间：')
    l_note.grid(row=0,sticky=W)

    l_hour = Label(root,text='时:')
    l_hour.grid(row=1,sticky=W,)
    e_hour = Entry(root)
    e_hour.grid(row=1,column=1,sticky=E)

    l_minute = Label(root, text='分:')
    l_minute.grid(row=2, sticky=W)
    e_minute = Entry(root)
    e_minute.grid(row=2, column=1, sticky=E)

    l_second = Label(root, text='秒:')
    l_second.grid(row=3, sticky=W)
    e_second = Entry(root)
    e_second.grid(row=3, column=1, sticky=E)

    l_msg = Label(root, text='')
    l_msg.grid(row=5)

    st = Shut(l_msg,e_hour,e_minute,e_second)

    b1_start = Button(root,text="关机",command=st.shutdown)
    b1_start.grid(row=4,column=0,sticky=E,pady=10)

    b2_start = Button(root, text="重启", command=st.reboot)
    b2_start.grid(row=4, column=1, sticky=W,padx=20,pady=10)

    root.mainloop()

if __name__ == '__main__':
    #seconds = 300
    #shutdown(seconds)
    view()