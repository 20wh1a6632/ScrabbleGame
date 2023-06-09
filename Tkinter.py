import tkinter as tk
from PIL import ImageTk, Image

import webbrowser

root = tk.Tk()
root.title("Scrabble Game")
root.geometry("700x350")


bg_image = Image.open("scrab8.jpg")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
frame0 = tk.Frame(root)
frame0.pack(pady=10)

label1 = tk.Label(frame0, text="User Rating Prediction in a Scrabble Game\n ",fg="#e91c54" ,bg="#20e8af",font=('Aerial', 25))
label1.pack()
frame1 = tk.Frame(root)
frame1.pack(pady=10)
label2 = tk.Label(frame1, text="Problem Description", font=('Aerial', 20))
label2.pack()
def open_link1():
   
    webbrowser.open(r"C:\Users\Abdul muqueeth\Desktop\ml\problemdescription.jpg")

button1 = tk.Button(frame1, text="Problem Statement", command=open_link1, bg="#b4c012")
button1.pack()
frame2= tk.Frame(root)
frame2.pack(pady=10)

label3 = tk.Label(frame2, text="Google Colab Notebook ", font=('Aerial', 20))
label3.pack()

def open_link2():
    webbrowser.open("https://colab.research.google.com/drive/1T0loFGcfPtPKRQRpqjIX-SOJfTpLxsrU")

button1 = tk.Button(frame2, text="Notebook", command=open_link2, bg="#b4c012")
button1.pack()

# Create a frame for the second label and button
frame3 = tk.Frame(root)
frame3.pack(pady=10)

label2 = tk.Label(frame3, text="Deployment using gradio", font=('Aerial', 20))
label2.pack()

def open_link3():
    webbrowser.open("https://2f4e779637fcb57e58.gradio.live/")

button2 = tk.Button(frame3, text="click here to view the output", command=open_link3, bg="#b4c012")
button2.pack()

# Create a frame for the third label and button
frame4 = tk.Frame(root)
frame4.pack(pady=10)

label4 = tk.Label(frame4, text="Models Used ", font=('Aerial', 20))
label4.pack()

def open_link4():
    webbrowser.open(r"C:\Users\Abdul muqueeth\Desktop\ml\modelsused.png")

button3 = tk.Button(frame4, text="click here", command=open_link4, bg="#b4c012")
button3.pack()

root.mainloop()
