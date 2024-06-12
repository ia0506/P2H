import tkinter
import random

KUJI = ["大吉", "中吉", "小吉", "凶"]

def btn_on():
    lbl["text"] = random.choice(KUJI) # choiceメソッド。リストの中の１つを選ぶ

root = tkinter.Tk()
root.title("おみくじ")
root.geometry("400x200")
btn = tkinter.Button(text="く\nじ\nを\n引\nく", font=("Times New Roman", 16), command=btn_on)
btn.place(x=0, y=0)
lbl = tkinter.Label(text="おみくじ", font=("Times New Roman", 48))
lbl.place(x=100, y=0)
root.mainloop()
