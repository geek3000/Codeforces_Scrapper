from tkinter import *
import requests, sys, PIL
from tkinter.messagebox import askokcancel, showerror
from PIL import Image, ImageTk


def quit_master(master):
    if askokcancel("Quit", "Do you really wish to quit ?"):
        master.destroy()
        sys.exit(0)
    

def get_data(e1):
    
    handle=e1.get()
    print(handle)
    url="https://codeforces.com/api/user.info?handles="+handle
    try:
        rep=requests.get(url).json()
        user_info={}
        if rep['status']=='OK':
            result=rep['result'][0]
            try:
                handle_L['text']=result['handle']
                rating_L['text']=result['rating']
                rank_L['text']=result['rank']
                m_rat_L['text']=result['maxRating']
                m_rank_L['text']=result['maxRank']

                url = "http:"+result['titlePhoto']
                print(url)
                response = requests.get(url)
                print(response)
                if response.status_code == 200:
                    with open("./avatar.jpg", 'wb') as f:
                        f.write(response.content)

                    img = Image.open('./avatar.jpg')
                    size=img.size
                    can1['height']=size[0]
                    can1['width']=size[1]
                    photo = ImageTk.PhotoImage(img)
                    can1['image']=photo
                    can1.image=photo
            except:
                showerror("User", "User info are incomplete")
        else:
            showerror("User", "Can't found user!")
    except:
        showerror("User", "Can't get user data")



def ask_user():
    ask = Toplevel(master)
    ask['bg']="green"
    ask.resizable(False, False)
    ask.title("Geek GCI")

    Label(ask, text='Handle: ', width=25, bg='green', fg="yellow", relief="raised").pack()
    e1=Entry(ask)
    e1.pack()

    Button(ask, width=25, text="Get User", bg='green', fg="yellow", relief="raised", command=lambda e=1e1:get_data(e1)).pack()


master = Tk()
master['bg']="green"
master.resizable(False, False)
master.protocol("WM_DELETE_WINDOW", lambda master=master:quit_master(master))
master.title("Geek GCI")

name = StringVar()

Label(master, text='Codeforces Scrapper@Geek3000', width=50, bg='green', fg="yellow", relief="raised").grid(column=0, columnspan=2)

can1 = Label(master, width = 50, height=30, bg = 'white')
can1.grid(row=1, rowspan=5, column=0, columnspan=2)

Label(master, text='Handle: ', width=25, bg='green', fg="yellow", relief="raised").grid(row=6, column=0)
handle_L=Label(master, text='Handle', width=25, bg='yellow', fg="green", relief="raised")
handle_L.grid(row=6, column=1)

Label(master, text='Rating: ', width=25, bg='green', fg="yellow", relief="raised").grid(row=7, column=0)
rating_L=Label(master, text='rating', width=25, bg='yellow', fg="green", relief="raised")
rating_L.grid(row=7, column=1)

Label(master, text='Rank: ', width=25, bg='green', fg="yellow", relief="raised").grid(row=8, column=0)
rank_L=Label(master, text='rank', width=25, bg='yellow', fg="green", relief="raised")
rank_L.grid(row=8, column=1)

Label(master, text='Max Rating: ', width=25, bg='green', fg="yellow", relief="raised").grid(row=9, column=0)
m_rat_L=Label(master, text='max rating', width=25, bg='yellow', fg="green", relief="raised")
m_rat_L.grid(row=9, column=1)

Label(master, text='Max Rank: ', width=25, bg='green', fg="yellow", relief="raised").grid(row=10, column=0)
m_rank_L=Label(master, text='max rank', width=25, bg='yellow', fg="green", relief="raised")
m_rank_L.grid(row=10, column=1)

Button(master, width=50, text="Get User", bg='yellow', fg="green", relief="raised", command=ask_user).grid(row=11, column=0, columnspan=2)
mainloop()
