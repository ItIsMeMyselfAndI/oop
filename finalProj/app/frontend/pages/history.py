import customtkinter as ctk


class History(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # initialize state
        self.isCurrentPage = False

        self.transaction_data = []

        # Make self fully expandable
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title Label
        title_label = ctk.CTkLabel(self,
                                   text="Transaction History",
                                   font=ctk.CTkFont(family="Bodoni MT", size=40, slant="italic"),
                                   text_color='#545454')
        title_label.grid(row=0, column=0, sticky="w", padx=30, pady=(30, 10))

        # Table container
        self.table_frame = ctk.CTkFrame(self, corner_radius=25, fg_color='white')
        self.table_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=30)

        # Columns
        for col in range(4):
            self.table_frame.grid_columnconfigure(col, weight=1)

        # Headers
        headers = ['Category', 'Date', 'Amount', 'Description']
        for index, header in enumerate(headers):
            label = ctk.CTkLabel(self.table_frame,
                                 text=header,
                                 font=ctk.CTkFont(family='Sans Serif', size=20, weight='bold'),
                                 text_color='black')
            label.grid(row=0, column=index, sticky="nsew", padx=40, pady=20)

        self.row_index = 1


    def add(self, category, date, amount, description):
        self.transaction_data.append((category, date, amount, description))
        values = [category, date, amount, description]
        for col, value in enumerate(values):
            label = ctk.CTkLabel(self.table_frame, text=value, text_color='black')
            label.grid(row=self.row_index, column=col, sticky="nsew", padx=40, pady=15)
        self.row_index += 1
