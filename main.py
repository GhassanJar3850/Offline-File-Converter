import os
from tkinter import filedialog
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
import ctypes as ct
from Utils import *
from PIL import Image, ImageTk


class DragDropApp:
    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.geometry("553x340")
        self.root.title("Universal File Converter")
        self.root.resizable(False, False)
        self.root.iconbitmap(ICON_APP)
        self.root.configure(bg="#2B2B2B")

        self.font_dragndrop = ctk.CTkFont(size=18, weight="bold")
        self.font_convertTo = ctk.CTkFont(size=14, weight="bold")
        self.font_Button = ctk.CTkFont(size=14, weight="bold")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        dark_title_bar(self.root)

        # variables
        self.selected_file_path = None
        self.destination_folder = None

        def on_drop(event):
            file_path = event.data.replace("{", "").replace("}", "")
            self.selected_file_path = file_path
            extension = file_path.split(".")[-1].lower()
            
            print(extension)

            if extension not in file_conversions:
                print(f"Unsupported file type: {extension}")
                return  # Prevent setting the selected file and displaying message

            self.drag_drop_icon.configure(light_image=Image.open(
                fileIconMap[extension]), dark_image=Image.open(fileIconMap[extension]))

            file_name = os.path.basename(
                file_path).replace("{", "").replace("}", "")

            self.conversion_options = file_conversions[extension]
            self.convert_to_combobox.configure(values=self.conversion_options)
            self.convert_to_combobox.set(self.conversion_options[0])

            self.drag_drop_label.configure(text=file_name)
            print(f"File dropped: {file_name}")

        # region GUI
        drag_drop_frame = ctk.CTkFrame(
            self.root, width=300, height=300, corner_radius=10)
        drag_drop_frame.grid(row=0, column=0, rowspan=3, padx=20, pady=20)

        self.drag_drop_label = ctk.CTkLabel(
            drag_drop_frame, text="Drag'n'Drop your file", anchor="center", font=self.font_dragndrop, wraplength=260)
        self.drag_drop_label.place(relx=0.5, rely=0.8, anchor="center")

        self.drag_drop_icon = ctk.CTkImage(light_image=Image.open(
            ICON_DRAG_N_DROP), dark_image=Image.open(ICON_DRAG_N_DROP), size=(130, 130))
        dropped_file_icon = ctk.CTkLabel(
            master=drag_drop_frame, width=100, height=100, corner_radius=10, image=self.drag_drop_icon, text="")
        dropped_file_icon.place(relx=0.5, rely=0.4, anchor="center")

        browse_file_button = ctk.CTkButton(
            drag_drop_frame, text="", width=32, height=32, command=self.browse_for_file, font=self.font_Button, image=ctk.CTkImage(light_image=Image.open(
                ICON_FOLDER), dark_image=Image.open(ICON_FOLDER), size=(20, 20)))
        browse_file_button.place(relx=0.86, rely=0.87)

        drag_drop_frame.drop_target_register(DND_FILES)
        drag_drop_frame.dnd_bind('<<Drop>>', on_drop)

        conversion_options = [""]
        self.convert_to_combobox = ctk.CTkComboBox(
            self.root, values=conversion_options, width=150, bg_color="transparent")
        self.convert_to_combobox.grid(row=0, column=1, padx=20, pady=(40, 0))

        convert_to_label = ctk.CTkLabel(
            self.root, text="Convert to", anchor="center", bg_color="transparent", fg_color="transparent", font=self.font_convertTo)
        convert_to_label.grid(row=0, column=1, padx=20, pady=(0, 20))

        destination_label = ctk.CTkLabel(
            self.root, text="Destination", anchor="center", bg_color="transparent", fg_color="transparent", font=self.font_convertTo)
        destination_label.grid(row=1, column=1, padx=20, pady=(0, 60+65))

        destination_detailsFrame = ctk.CTkFrame(
            self.root, width=150, height=130, corner_radius=10, border_width=1, border_color="#343638", fg_color="#2b2b2b")
        destination_detailsFrame.grid(
            row=1, column=1, rowspan=3, padx=20, pady=(0, 45))

        self.destination_details = ctk.CTkLabel(
            destination_detailsFrame, text="", anchor="center", bg_color="transparent", fg_color="transparent", wraplength=130)
        self.destination_details.place(relx=0.5, rely=0.6, anchor="center")

        destination_button = ctk.CTkButton(
            self.root, text="Browse", width=80, command=self.select_destination, font=self.font_Button)
        destination_button.grid(row=1, column=1, padx=20, pady=(10, 10+50))

        convert_button = ctk.CTkButton(
            self.root, text="Convert", width=150, height=45, command=self.convert, font=self.font_Button)
        convert_button.grid(row=2, column=1, padx=20, pady=(0, 10))
        # endregion

    def browse_for_file(self):
        file_path = filedialog.askopenfile().name

        self.selected_file_path = file_path
        extension = file_path.split(
            ".")[-1].lower().replace("{", "").replace("}", "")
        print(extension)

        if extension not in file_conversions.keys():
            print(f"Unsupported file type: {extension}")
            return  # Prevent setting the selected file and displaying message

        self.drag_drop_icon.configure(light_image=Image.open(
            fileIconMap[extension]), dark_image=Image.open(fileIconMap[extension]))

        file_name = os.path.basename(
            file_path).replace("{", "").replace("}", "")

        self.conversion_options = file_conversions[extension]
        self.convert_to_combobox.configure(values=self.conversion_options)
        self.convert_to_combobox.set(self.conversion_options[0])

        self.drag_drop_label.configure(text=file_name)
        print(f"File dropped: {file_name}")

    def select_destination(self):
        folder_path = filedialog.askdirectory()
        self.destination_details.configure(text=folder_path)
        self.destination_folder = folder_path
        print(f"Selected destination folder: {folder_path}")

    def convert(self):
        from Services import Video, Audio, Documents
        desired_extension = self.convert_to_combobox.get()
        extension = self.selected_file_path.split(
            ".")[-1].lower().replace("{", "").replace("}", "")

        # if fileIconMap[extension] in [ICON_TXT, ICON_MD]:
        #     Audio.convert_audio(self.selected_file_path,
        #                         desired_extension, self.destination_folder)
            
        if fileIconMap[extension] in [ICON_MUSIC, ICON_RECORD]:
            Audio.convert_audio(self.selected_file_path,
                                desired_extension, self.destination_folder)

        # if fileIconMap[extension] in [ICON_IMAGE, ICON_SVG]:
        #     Audio.convert_audio(self.selected_file_path,
        #                         desired_extension, self.destination_folder)

        # if fileIconMap[extension] in [ICON_DOC, ICON_DOCX]:
        #     Audio.convert_audio(self.selected_file_path,
        #                         desired_extension, self.destination_folder)

        # if fileIconMap[extension] in [ICON_CSV, ICON_XLS]:
        #     Audio.convert_audio(self.selected_file_path,
        #                         desired_extension, self.destination_folder)

        # if fileIconMap[extension] == ICON_COMPRESSED:
        #     Audio.convert_audio(self.selected_file_path,
        #                         desired_extension, self.destination_folder)
            
        if fileIconMap[extension] == ICON_PDF:
            Documents.convert_pdf(self.selected_file_path,
                                desired_extension, self.destination_folder)
            
        if fileIconMap[extension] == ICON_VIDEO:
            Video.convert_video(self.selected_file_path,
                                desired_extension, self.destination_folder)
            
        # if fileIconMap[extension] == ICON_PPT:
        #     Audio.convert_audio(self.selected_file_path,
        #                         desired_extension, self.destination_folder)

    def run(self):
        self.root.mainloop()


def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy,
                         ct.byref(value), ct.sizeof(value))


if __name__ == "__main__":
    app = DragDropApp()
    app.run()
