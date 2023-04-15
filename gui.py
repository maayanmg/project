import customtkinter
def first():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("500x350")



    login_frame = customtkinter.CTkFrame(master= root)
    login_frame.pack(pady = 20, padx = 60, fill ="both", expand =True)

    label = customtkinter.CTkLabel(master= login_frame, text= "Login System")
    label.pack(pady = 12, padx = 10)

    entry1 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Username")
    entry1.pack(pady = 12, padx = 10)

    entry2 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
    entry2.pack(pady = 12, padx = 10)

    button = customtkinter.CTkButton(master= login_frame, text="Login", command= login)
    button.pack(pady = 12, padx = 10)

    checkbox = customtkinter.CTkCheckBox(master=login_frame, text="Remember Me")
    checkbox.pack(pady = 12, padx = 10)

    root.mainloop()


def login():
    root.destroy()
    root = customtkinter.CTk()
    root.geometry("500x350")
    upload_frame = customtkinter.CTkFrame(master=root)
    upload_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=upload_frame, text="Upload Picture")
    label.pack(pady=12, padx=10)

    root.mainloop()

if __name__ == '__main__':
    first()

