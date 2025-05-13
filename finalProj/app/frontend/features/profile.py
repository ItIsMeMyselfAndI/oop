import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw


class Profile(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, ** kwargs)
        
        # Extract keyword arguments with defaults
        self.savings = kwargs.get('Savings', 0)
        self.investment = kwargs.get('Investments', 0)
        self.name = kwargs.get('Username', 'Username')

        # Top bar
        top_frame = ctk.CTkFrame(self, 
                                 height=1000, 
                                 fg_color="#2d6ca7", 
                                 corner_radius=0)
        top_frame.pack(fill="x", side="top")
        self.total_label = ctk.CTkLabel(top_frame,
                                         text="", 
                                         font=("Arial", 100, "bold"), 
                                         text_color="white")
        self.total_label.pack(side="right", 
                              padx=20, 
                              pady=10)

       # Profile section and finance rows 
        content_frame = ctk.CTkFrame(self, fg_color='transparent')
        content_frame.pack(fill='x', padx=20, pady=20)

        # Profile row
        profile_row = ctk.CTkFrame(content_frame, fg_color='transparent')
        profile_row.pack(fill='x', pady=(0, 96))

        profile_pic_path = './frontend/assets/icons/profile.png'
        profile_img_size = 300

        profile_image_with_border = self.create_circular_image_with_border(
            profile_pic_path,
            size=profile_img_size,
            border_size=10,
            border_color="#7fbcd2"
        )

        profile_img_label = ctk.CTkLabel(profile_row,
                                        image=profile_image_with_border,
                                        text='',
                                        fg_color='transparent')
        profile_img_label.image = profile_image_with_border
        profile_img_label.pack(side='left')

        name_label = ctk.CTkLabel(profile_row,
                                text=self.name,
                                font=("Bodoni MT", 40, "italic"),
                                text_color='#545454',
                                fg_color='transparent')
        name_label.pack(side='left', padx=15)


        # Savings section 
        savings_row = ctk.CTkFrame(content_frame, fg_color='transparent')
        savings_row.pack(fill='x', pady=(0, 96))  # 1 inch below profile

        # Ico big enough to cover both lines of text
        savings_image = Image.open('./frontend/assets/icons/savings.png').resize((150, 150))
        savings_circular_img = ImageTk.PhotoImage(savings_image)
        savings_image_label = ctk.CTkLabel(savings_row,
                                        image=savings_circular_img,
                                        text='',
                                        fg_color='transparent')
        savings_image_label.image = savings_circular_img
        savings_image_label.pack(side='left', padx=20)

        # Text container (Label + Amount stacked vertically)
        savings_text_frame = ctk.CTkFrame(savings_row, fg_color='transparent')
        savings_text_frame.pack(side='left')

        self.savings_label = ctk.CTkLabel(savings_text_frame,
                                        text="Savings",
                                        font=("Bodoni MT", 50, 'italic'),
                                        text_color='#545454',
                                        fg_color='transparent')
        self.savings_label.pack()

        self.savings_amount_label = ctk.CTkLabel(savings_text_frame,
                                                text="",  # Will be set dynamically
                                                font=("Bodoni MT", 50, "italic"),
                                                text_color='#545454',
                                                fg_color='transparent')
        self.savings_amount_label.pack()


        # Investment section
        invest_row = ctk.CTkFrame(content_frame, fg_color='transparent')
        invest_row.pack(fill='x')

        invest_image = Image.open('./frontend/assets/icons/investment.png').resize((150, 150))
        invest_circular_img = ImageTk.PhotoImage(invest_image)
        invest_image_label = ctk.CTkLabel(invest_row,
                                        image=invest_circular_img,
                                        text='',
                                        fg_color='transparent')
        invest_image_label.image = invest_circular_img
        invest_image_label.pack(side='left', padx=20)

        invest_text_frame = ctk.CTkFrame(invest_row, fg_color='transparent')
        invest_text_frame.pack(side='left')

        self.investment_label = ctk.CTkLabel(invest_text_frame,
                                            text="Investments",
                                            font=("Bodoni MT", 50, 'italic'),
                                            text_color='#545454',
                                            fg_color='transparent')
        self.investment_label.pack()

        self.investment_amount_label = ctk.CTkLabel(invest_text_frame,
                                                    text="",  # Will be set dynamically
                                                    font=("Bodoni MT", 50, "italic"),
                                                    text_color='#545454',
                                                    fg_color='transparent')
        self.investment_amount_label.pack()

        self.update_financial_display()
    
    def create_circular_image_with_border(self, img_path, size, border_size, border_color):

        # Resize original image
        img = Image.open(img_path).resize((size, size))

        # Create circular mask for the profile image
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        circular_img = Image.new("RGBA", (size, size))
        circular_img.paste(img, (0, 0), mask=mask)

        # Create bordered image
        total_size = size + 2 * border_size
        bordered_img = Image.new("RGBA", (total_size, total_size), border_color)
        bordered_img.paste(circular_img, (border_size, border_size), mask=mask)

        # Final circular mask for entire bordered image
        final_mask = Image.new("L", (total_size, total_size), 0)
        draw = ImageDraw.Draw(final_mask)
        draw.ellipse((0, 0, total_size, total_size), fill=255)

        final_img = Image.new("RGBA", (total_size, total_size))
        final_img.paste(bordered_img, (0, 0), mask=final_mask)
        return ImageTk.PhotoImage(final_img)

    def update_financial_display(self):
        savings_str = f"₱ {self.savings:,.2f}"
        investment_str = f"₱ {self.investment:,.2f}"
        total_str = f"₱ {self.savings + self.investment:,.2f}"

        self.savings_amount_label.configure(text=savings_str)
        self.investment_amount_label.configure(text=investment_str)
        self.total_label.configure(text=total_str)

    def set_financial_data(self, savings, investment):
        self.savings = savings
        self.investment = investment
        self.update_financial_display()

