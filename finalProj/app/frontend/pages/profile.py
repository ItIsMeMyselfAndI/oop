import customtkinter as ctk
# from PIL import Image, ImageTk, ImageDraw

WHITE= "white"

WHITE_BLUE = "#ebf2fe"
WHITE_RED = "#fdecec"
WHITE_GREEN = "#e7f8f2"
WHITE_PURPLE = "#f3eefe"

LIGHT_BLUE = "#cef2ff"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"

LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"

class Balance(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, ** kwargs)


class Income(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, ** kwargs)
        

class Expense(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, ** kwargs)


class Savings(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, ** kwargs)


class Investment(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, ** kwargs)


class Profile(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, ** kwargs)
        # create page sections
        self.profile = Balance(self, fg_color=BLUE, corner_radius=10, height=250) # (1080-20-20-20)/3
        self.summary = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=10, height=680) # [(1080-20-20-20)/3]*2
        # create summary sub-sections
        self.income = Income(self.summary, fg_color=WHITE_BLUE, corner_radius=10)
        self.expense = Expense(self.summary, fg_color=WHITE_RED, corner_radius=10)
        self.savings = Savings(self.summary, fg_color=WHITE_GREEN, corner_radius=10)
        self.investment = Investment(self.summary, fg_color=WHITE_PURPLE, corner_radius=10)
        # display page sections
        self.profile.pack(pady=(20,0), padx=(20,20))
        self.summary.pack(pady=(20,0), padx=(20,20))
        # display summary sections
        self.income.grid(row=0, column=0, pady=(20,0), padx=(20,0))
        self.expense.grid(row=0, column=1, pady=(20,0), padx=(20,20))
        self.savings.grid(row=1, column=0, pady=(20,20), padx=(20,0))
        self.investment.grid(row=1, column=1, pady=(20,20), padx=(20,20))

        # self.padx = 20
        # self.pady_large = 96

        
        # # Extract keyword arguments with defaults
        # self.savings = kwargs.get('Savings', 0)
        # self.investment = kwargs.get('Investments', 0)
        # self.name = kwargs.get('Username', 'Username')

        # # Top bar
        # profile_balance_frame = ctk.CTkFrame(self, height=100, fg_color=BLUE, corner_radius=0)
        # profile_balance_frame.pack(fill="both", anchor="ne")
        # self.total_label = ctk.CTkLabel(profile_balance_frame,
        #                                  text="", 
        #                                  font=("Arial", 50, "bold"), 
        #                                  text_color=WHITE)
        # self.total_label.pack(side="right", 
        #                       padx=20, 
        #                       pady=10)

        # # Profile row
        # profile_row = ctk.CTkFrame(self, fg_color='green')
        # profile_row.pack(fill='both')

        # profile_pic_path = './frontend/assets/icons/profile.png'
        # profile_img_size = 150

        # profile_image_with_border = self.create_circular_image_with_border(
        #     profile_pic_path,
        #     size=profile_img_size,
        #     border_size=10,
        #     border_color="#7fbcd2"
        # )

        # profile_img_label = ctk.CTkLabel(profile_row,
        #                                 image=profile_image_with_border,
        #                                 text='',
        #                                 fg_color='transparent')
        # profile_img_label.image = profile_image_with_border
        # profile_img_label.pack(side='left', padx=(30, 10), pady=(10, 0))


        # name_label = ctk.CTkLabel(profile_row,
        #                         text=self.name,
        #                         font=("Bodoni MT", 40, "italic"),
        #                         text_color=DARK_GREY,
        #                         fg_color='transparent')
        # name_label.pack(side='left', padx=self.padx)


        # Savings section 
        # savings_row = ctk.CTkFrame(self, fg_color='transparent')
        # savings_row.pack(fill='x', pady=(0, self.pady_large))

        # Ico big enough to cover both lines of text
        # savings_image = Image.open('./frontend/assets/icons/savings.png').resize((150, 150))
        # savings_circular_img = ImageTk.PhotoImage(savings_image)
        # savings_image_label = ctk.CTkLabel(savings_row,
        #                                 image=savings_circular_img,
        #                                 text='',
        #                                 fg_color='transparent')
        # savings_image_label.image = savings_circular_img
        # savings_image_label.pack(side='left', padx=(30, 10), pady=(10, 0))


        # # Text container (Label + Amount stacked vertically)
        # savings_text_frame = ctk.CTkFrame(savings_row, fg_color='transparent')
        # savings_text_frame.pack(side='left')

        # self.savings_label = ctk.CTkLabel(savings_text_frame,
        #                                 text="Savings",
        #                                 font=("Bodoni MT", 50, 'italic'),
        #                                 text_color=DARK_GREY,
        #                                 fg_color='transparent')
        # self.savings_label.pack()

        # self.savings_amount_label = ctk.CTkLabel(savings_text_frame,
        #                                         text="",  # Will be set dynamically
        #                                         font=("Bodoni MT", 50, "italic"),
        #                                         text_color=DARK_GREY,
        #                                         fg_color='transparent')
        # self.savings_amount_label.pack()


        # Investment section
        # invest_row = ctk.CTkFrame(self, fg_color='transparent')
        # invest_row.pack(fill='x', pady=(0, self.pady_large))

        # invest_image = Image.open('./frontend/assets/icons/investment.png').resize((150, 150))
        # invest_circular_img = ImageTk.PhotoImage(invest_image)
        # invest_image_label = ctk.CTkLabel(invest_row,
        #                                 image=invest_circular_img,
        #                                 text='',
        #                                 fg_color='transparent')
        # invest_image_label.image = invest_circular_img
        # invest_image_label.pack(side='left', padx=(30, 10), pady=(10, 0))


        # invest_text_frame = ctk.CTkFrame(invest_row, fg_color='transparent')
        # invest_text_frame.pack(side='left')

        # self.investment_label = ctk.CTkLabel(invest_text_frame,
        #                                     text="Investments",
        #                                     font=("Bodoni MT", 50, 'italic'),
        #                                     text_color=DARK_GREY,
        #                                     fg_color='transparent')
        # self.investment_label.pack()

        # self.investment_amount_label = ctk.CTkLabel(invest_text_frame,
        #                                             text="",  # Will be set dynamically
        #                                             font=("Bodoni MT", 50, "italic"),
        #                                             text_color=DARK_GREY,
        #                                             fg_color='transparent')
        # self.investment_amount_label.pack()

        # self.update_financial_display()
    
    # def create_circular_image_with_border(self, img_path, size, border_size, border_color):

    #     # Resize original image
    #     img = Image.open(img_path).resize((size, size))

    #     # Create circular mask for the profile image
    #     mask = Image.new("L", (size, size), 0)
    #     draw = ImageDraw.Draw(mask)
    #     draw.ellipse((0, 0, size, size), fill=255)

    #     circular_img = Image.new("RGBA", (size, size))
    #     circular_img.paste(img, (0, 0), mask=mask)

    #     # Create bordered image
    #     total_size = size + 2 * border_size
    #     bordered_img = Image.new("RGBA", (total_size, total_size), border_color)
    #     bordered_img.paste(circular_img, (border_size, border_size), mask=mask)

    #     # Final circular mask for entire bordered image
    #     final_mask = Image.new("L", (total_size, total_size), 0)
    #     draw = ImageDraw.Draw(final_mask)
    #     draw.ellipse((0, 0, total_size, total_size), fill=255)

    #     final_img = Image.new("RGBA", (total_size, total_size))
    #     final_img.paste(bordered_img, (0, 0), mask=final_mask)
    #     return ImageTk.PhotoImage(final_img)

    # def update_financial_display(self):
    #     savings_str = f"₱ {self.savings:,.2f}"
    #     investment_str = f"₱ {self.investment:,.2f}"
    #     total_str = f"₱ {self.savings + self.investment:,.2f}"

    #     self.savings_amount_label.configure(text=savings_str)
    #     self.investment_amount_label.configure(text=investment_str)
    #     self.total_label.configure(text=total_str)

    # def set_financial_data(self, savings, investment):
    #     self.savings = savings
    #     self.investment = investment
    #     self.update_financial_display()

