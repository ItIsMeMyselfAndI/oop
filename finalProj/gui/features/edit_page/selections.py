import customtkinter as ctk


class Selection(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.font1 = ctk.CTkFont(family="Bodoni MT", size=30, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        self.options = ["Option 1", "Option 2", "Option 3"]
        # create guide frames
        self.frame1 = ctk.CTkFrame(self, fg_color="white", corner_radius=10)
        self.frame2 = ctk.CTkFrame(self, fg_color="white", corner_radius=10, height=100)
        self.frame3 = ctk.CTkFrame(self, fg_color="white", corner_radius=10, height=100)
        # create frame 1 components
        self.transactionLabel = ctk.CTkLabel(self.frame1, text="Select Transaction",
                                             font=self.font1, text_color="#545454")
        self.dateLabel = ctk.CTkLabel(self.frame1, text="New Date",
                                      font=self.font1, text_color="#545454")
        self.transactionMenu = ctk.CTkOptionMenu(self.frame1, values=self.options,
                                                 font=self.font2, text_color="#545454",
                                                 fg_color="#559eef", dropdown_font=self.font2,
                                                 dropdown_fg_color="#559eef",
                                                 dropdown_hover_color="#427cbd",
                                                 dropdown_text_color="#545454",
                                                 corner_radius=10, width=680, height=40)
        self.dateMenu = ctk.CTkOptionMenu(self.frame1, values=self.options,
                                          font=self.font2, text_color="#545454",
                                          fg_color="#559eef", dropdown_font=self.font2,
                                          dropdown_fg_color="#559eef",
                                          dropdown_hover_color="#427cbd",
                                          dropdown_text_color="#545454",
                                          corner_radius=10, width=400, height=40)
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select Category",
                                             font=self.font1, text_color="#545454")
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="New Description",
                                      font=self.font1, text_color="#545454")
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=self.options,
                                                 font=self.font2, text_color="#545454",
                                                 width=680, fg_color="#559eef",
                                                 dropdown_font=self.font2,
                                                 dropdown_fg_color="#559eef",
                                                 dropdown_hover_color="#427cbd",
                                                 dropdown_text_color="#545454",
                                                 corner_radius=10, height=40)
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font2,
                                             text_color="#545454", fg_color="#559eef",
                                             corner_radius=10, width=400, height=40,
                                             placeholder_text="Description",
                                             placeholder_text_color="grey",
                                             border_width=0)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="New Amount",
                                        font=self.font1, text_color="#545454")
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font2,
                                        text_color="#545454", fg_color="#559eef",
                                        corner_radius=10, width=1100, height=40,
                                        placeholder_text="Philippine Peso",
                                        placeholder_text_color="grey",
                                        border_width=0)
        # display guide frames
        self.frame1.pack(fill="both", pady=(10,10))
        self.frame2.pack(fill="both", pady=(0,10))
        self.frame3.pack(fill="both", pady=(0,10))
        # display frame 1 components
        self.transactionLabel.grid(row=0, column=0, sticky="w", pady=(10,0), padx=(20,0))
        self.dateLabel.grid(row=0, column=1, sticky="w", pady=(20,0), padx=(20,0))
        self.transactionMenu.grid(row=1, column=0, sticky="w", pady=(20,10), padx=(20,0))
        self.dateMenu.grid(row=1, column=1, sticky="w", pady=(20,10), padx=(20,20))
        # display frame 2 components
        self.categoryLabel.grid(row=0, column=0, sticky="w", pady=(20,0), padx=(20,0))
        self.descriptionLabel.grid(row=0, column=1, sticky="w", pady=(20,0), padx=(20,0))
        self.categoryMenu.grid(row=1, column=0, sticky="w", pady=(20,10), padx=(20,0))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", pady=(20,10), padx=(20,20))
        # display frame 3 components
        self.amountLabel.pack(anchor="w", pady=(20,0), padx=(20,0))
        self.amountEntry.pack(anchor="w", pady=(20,20), padx=(20,20))