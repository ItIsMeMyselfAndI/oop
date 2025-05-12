# external/built-in modules/libs
import customtkinter as ctk


class Save(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections 
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=270, height=40, text="Save Changes",
                                 font=self.font, text_color="white",
                                 fg_color="#559eef", hover_color="#427cbd",
                                 corner_radius=10, command=self.on_click_save)
        self.btn.pack(pady=(10,10))

    def on_click_save(self):
        for name, selection in self.selections.items():
            if selection.isCurrentSelection == True:
                selection_type = name
                transaction = selection.transactionMenu.get()
                day = selection.dateMenu.day.get()
                month = selection.dateMenu.month.get()
                year = selection.dateMenu.year.get()
                category = selection.categoryMenu.get()
                description = selection.descriptionEntry.get()
                amount = selection.amountEntry.get()
                break
        print()
        print(f"{selection_type = }")
        print(f"{transaction = }")
        print(f"new date = {day} {month} {year}")
        print(f"new {category = }")
        print(f"new {description = }")
        print(f"new {amount = }")