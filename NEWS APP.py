import io

import requests
import webbrowser
from tkinter import *
from urllib.request import urlopen

from PIL import ImageTk,Image

class NewsApp:
    def __init__(self):
        #fetching data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country='
                                 'us&apiKey=77277d5f08c949bcb50e2577fc5d0bd1').json()


        #create initial gui
        self.gui_load()
        #load data
        self.load_data(0)


    def gui_load(self):
        self.root = Tk()
        self.root.geometry(('350x600'))
        self.root.resizable(0,0)
        self.root.title('Abhi Tak')
        self.root.configure(background='white')


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def link_open(self,url):
        webbrowser.open(url)

    def load_data(self,index):

        #clear the screen for next item to be printed
        self.clear()


        #image
        try:
            img_url =  self.data['articles'][index]['urlToImage']
            temp = urlopen(img_url).read()
            img = Image.open(io.BytesIO(temp)).resize((350,200))
            photo = ImageTk.PhotoImage(img)

        except:
            img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRleKTGZ3asGHBqoap1YPeldfLJ9Iwk8ZN7prhoOh0Fo6hv8_JoSXxFwIbu_cEYlO8HtG4&usqp=CAU'
            temp = urlopen(img_url).read()
            img = Image.open(io.BytesIO(temp)).resize((350, 200))
            photo = ImageTk.PhotoImage(img)

        label = Label(self.root, image=photo)
        label.pack()

        heading = Label(self.root,text= self.data['articles'][index]['title'],bg='white',fg='black',wraplength=340,
                        justify='center')
        heading.config(font=('verdana',15,'bold'))
        heading.pack(pady=(10,20))

        detail = Label(self.root, text=self.data['articles'][index]['description'], bg='white', fg='black',
                       wraplength=340,justify='center')
        detail.config(font=('verdana', 12,))
        detail.pack(pady=(2, 20))

        author = Label(self.root, text=self.data['articles'][index]['author'], bg='white', fg='black',
                            wraplength=340, justify='center')
        author.config(font=('verdana', 10))
        author.pack()

        publishedAt = Label(self.root,text= self.data['articles'][index]['publishedAt'],bg = 'white',fg= 'black',
                            wraplength=340,justify= 'center')
        publishedAt.config(font=('verdana',10))
        publishedAt.pack()

        frame = Frame(self.root,bg= 'white')
        frame.pack(expand = True,fill= BOTH)

        if index != 0:
            prev = Button(frame,text= '<<<',height= 3,width=16,command= lambda : self.load_data(index - 1))
            prev.pack(side= LEFT)

        read = Button(frame,text= 'Read More',width= 16,height=3,command= lambda : self.link_open(self.data['articles'][index]['url']))
        read.pack(side= LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame,text='>>>',width=16,height= 3,command= lambda : self.load_data(index + 1))
            next.pack(side=LEFT)


        self.root.mainloop()

a = NewsApp()