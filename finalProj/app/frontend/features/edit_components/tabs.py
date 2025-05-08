import customtkinter as ctk


class Tabs(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        # create buttons/tabs
        self.expenseBtn = ctk.CTkButton(self, text="Expense", text_color="#545454",
                                        height=40, width=270,
                                        font=self.font, corner_radius=10,
                                        fg_color="white", hover_color="#c4c4c4",
                                        command=self.on_click_expense)
        self.savingsBtn = ctk.CTkButton(self, text="Savings", text_color="#545454",
                                        height=40, width=270,
                                        font=self.font, corner_radius=10,
                                        fg_color="white", hover_color="#c4c4c4",
                                        command=self.on_click_savings)
        self.investmentBtn = ctk.CTkButton(self, text="Investment", text_color="#545454",
                                           height=40, width=270,
                                           font=self.font, corner_radius=10,
                                           fg_color="white", hover_color="#c4c4c4",
                                           command=self.on_click_investment)
        self.incomeBtn = ctk.CTkButton(self, text="Income", text_color="#545454",
                                       height=40, width=270,
                                       font=self.font, corner_radius=10,
                                       fg_color="white", hover_color="#c4c4c4",
                                       command=self.on_click_income)
        # show buttons/tabs
        self.expenseBtn.grid(row=0, column=0, padx=(20, 0))
        self.savingsBtn.grid(row=0, column=1, padx=(20, 0))
        self.investmentBtn.grid(row=0, column=2, padx=(20, 0))
        self.incomeBtn.grid(row=0, column=3, padx=(20, 20))
        # open default tab
        self.selections["expense"].grid(row=2, column=0, sticky="nsew")
        self.selections["expense"].isCurrentSelection = True
        self.expenseBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_expense(self):
        # close other selections
        self.selections["savings"].grid_forget()
        self.selections["investment"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.savingsBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.investmentBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.incomeBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        # open expense and change fg, hover & text color
        self.selections["expense"].grid(row=2, column=0, sticky="nsew")
        self.selections["expense"].isCurrentSelection = True
        self.expenseBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_savings(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["investment"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.investmentBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.incomeBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.selections["expense"].isCurrentSelection = False 
        self.selections["investment"].isCurrentSelection = False
        self.selections["income"].isCurrentSelection = False
        # open savings and change fg, hover & text color
        self.selections["savings"].grid(row=2, column=0, sticky="nsew")
        self.selections["savings"].isCurrentSelection = True
        self.savingsBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_investment(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["savings"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.savingsBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.incomeBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        # set other selections isCurrentSelection to false
        self.selections["expense"].isCurrentSelection = False 
        self.selections["savings"].isCurrentSelection = False
        self.selections["income"].isCurrentSelection = False
        # open investment and change fg, hover & text color
        self.selections["investment"].grid(row=2, column=0, sticky="nsew")
        self.selections["investment"].isCurrentSelection = True
        self.investmentBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_income(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["savings"].grid_forget()
        self.selections["investment"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.savingsBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.investmentBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        # set other selections isCurrentSelection to false
        self.selections["expense"].isCurrentSelection = False 
        self.selections["savings"].isCurrentSelection = False
        self.selections["investment"].isCurrentSelection = False
        # open income and change fg, hover & text color
        self.selections["income"].grid(row=2, column=0, sticky="nsew")
        self.selections["income"].isCurrentSelection = True
        self.incomeBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

