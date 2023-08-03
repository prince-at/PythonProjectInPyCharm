import customtkinter
import tkinter

#main = tkinter.Tk()
#root=tkinter.Tk()
#main.mainloop()
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x500")

def login():
    print("text")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill ="both", expand = True)

label = customtkinter.CTkLabel(master = frame, text="LOGIN TO SHARE FILE", text_color="green")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text="Password", show ="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame,text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()