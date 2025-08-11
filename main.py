from tkinter import *
import requests

def quote():
    response =  requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()["quote"]
    canvas.itemconfig(quote_text,text= data)


window = Tk()
window.config(pady=50,padx=150)

background = PhotoImage(file="background.png")
kanye = PhotoImage(file="kanye.png")
canvas = Canvas(width=300,height=414,highlightthickness=0)
canvas.create_image(150, 212, image= background)
quote_text = canvas.create_text(150, 207,text=f"Kanye's Quotes here",fill="yellow",width=280, font=("Arial", 25, "bold"))
canvas.grid(row=0,column=0)


button = Button(image=kanye,highlightthickness=0,command=quote)
button.grid(row=1,column=0)

window.mainloop()