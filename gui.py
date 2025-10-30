import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from core import ops
from models.contact import Contact

class CRMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRM GUI")
        self.geometry("900x500")
        self.minsize(700, 350)

        # --- DARK THEME SETUP ---
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(".", 
            background="#23272e", 
            foreground="#f8f8f2", 
            fieldbackground="#23272e", 
            bordercolor="#44475a"
        )
        style.configure("Treeview", 
            background="#282a36", 
            fieldbackground="#282a36", 
            foreground="#f8f8f2", 
            rowheight=28,
            bordercolor="#44475a",
            font=("Consolas", 11)
        )
        style.map("Treeview", background=[("selected", "#44475a")])
        style.configure("Treeview.Heading", 
            background="#44475a", 
            foreground="#f8f8f2", 
            font=("Segoe UI", 11, "bold")
        )
        style.configure("TButton", 
            background="#44475a", 
            foreground="#f8f8f2", 
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
            focusthickness=3,
            focuscolor="#6272a4"
        )
        style.map("TButton", background=[("active", "#6272a4")])

        self.configure(bg="#23272e")

        # --- HEADER ---
        header = tk.Label(self, text="Contact Manager", font=("Segoe UI", 22, "bold"),
                          bg="#23272e", fg="#50fa7b", pady=10)
        header.pack(fill=tk.X)

        # --- BUTTON FRAME ---
        btn_frame = tk.Frame(self, bg="#23272e")
        btn_frame.pack(fill=tk.X, pady=10)
        ttk.Button(btn_frame, text="Add Contact", command=self.add_contact).pack(side=tk.LEFT, padx=8, pady=2)
        ttk.Button(btn_frame, text="Search", command=self.search_contacts).pack(side=tk.LEFT, padx=8, pady=2)
        ttk.Button(btn_frame, text="Import", command=self.import_contacts).pack(side=tk.LEFT, padx=8, pady=2)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected).pack(side=tk.LEFT, padx=8, pady=2)
        ttk.Button(btn_frame, text="Clear All", command=self.clear).pack(side=tk.LEFT, padx=8, pady=2)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_contacts).pack(side=tk.LEFT, padx=8, pady=2)

        # --- TREEVIEW FRAME WITH SCROLLBAR ---
        tree_frame = tk.Frame(self, bg="#23272e")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
        columns = ("name", "email", "phone", "company")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=200, anchor=tk.W, stretch=True)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # --- STATUS BAR ---
        self.status = tk.Label(self, text="", anchor="w", bg="#282a36", fg="#f8f8f2", font=("Segoe UI", 10))
        self.status.pack(fill=tk.X, padx=10, pady=(0, 5))

        self.refresh_contacts()

    def set_status(self, msg):
        self.status.config(text=msg)

    def refresh_contacts(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        count = 0
        for rec in ops.list_records():
            guid = rec.get("guid", "")
            self.tree.insert("", tk.END, iid=guid, values=(
                rec.get("name", ""),
                rec.get("email", ""),
                rec.get("phone", ""),
                rec.get("company", "")
            ))
            count += 1
        self.set_status(f"{count} contact(s) loaded.")

    def add_contact(self):
        add_win = tk.Toplevel(self)
        add_win.title("Add Contact")
        add_win.geometry("320x260")
        add_win.configure(bg="#23272e")
        for label in ["Name", "Email", "Phone", "Company"]:
            tk.Label(add_win, text=label+":", bg="#23272e", fg="#f8f8f2", font=("Segoe UI", 10)).pack()
            entry = tk.Entry(add_win, bg="#282a36", fg="#f8f8f2", insertbackground="#f8f8f2")
            entry.pack()
            setattr(add_win, f"{label.lower()}_entry", entry)

        def save():
            name = add_win.name_entry.get()
            email = add_win.email_entry.get()
            phone = add_win.phone_entry.get()
            company = add_win.company_entry.get()
            if name and email:
                contact = Contact(name, email, phone, company)
                ops.add_record(contact)
                self.refresh_contacts()
                self.set_status(f"Added contact: {name}")
                add_win.destroy()
            else:
                messagebox.showerror("Error", "Name and Email are required.")

        ttk.Button(add_win, text="Save", command=save).pack(pady=10)

    def search_contacts(self):
        query = simpledialog.askstring("Search", "Enter name to search:")
        if query:
            results = ops.search_records(query)
            for row in self.tree.get_children():
                self.tree.delete(row)
            for rec in results:
                guid = rec.get("guid", "")
                self.tree.insert("", tk.END, iid=guid, values=(
                    rec.get("name", ""),
                    rec.get("email", ""),
                    rec.get("phone", ""),
                    rec.get("company", "")
                ))
            self.set_status(f"{len(results)} contact(s) found.")

    def import_contacts(self):
        n = simpledialog.askinteger("Import", "How many random users?")
        if n:
            ops.import_records(n)
            self.refresh_contacts()
            self.set_status(f"Imported {n} contacts.")

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Delete", "No contact selected.")
            return
        guid = selected[0]
        name = self.tree.item(guid)["values"][0]
        if messagebox.askyesno("Delete", f"Are you sure you want to delete contact '{name}'?"):
            ops.delete_record(guid)
            self.refresh_contacts()
            self.set_status(f"Deleted contact: {name}")

    def clear(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all contacts?"):
            ops.clear_records()
            self.refresh_contacts()
            self.set_status("All contacts cleared.")

if __name__ == "__main__":
    app = CRMApp()
    app.mainloop()