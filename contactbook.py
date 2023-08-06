import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("630x550")  # Set window size
        
        self.contacts = []
        
        self.root.configure(bg="#c0e2c4")  # Set background color
        
        self.name_label = tk.Label(root, text="Name:", anchor="w")
        self.name_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=20, pady=10)
        
        self.phone_label = tk.Label(root, text="Phone:", anchor="w")
        self.phone_label.grid(row=1, column=0, padx=20, pady=10)
        
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=20, pady=10)
        
        self.email_label = tk.Label(root, text="Email:", anchor="w")
        self.email_label.grid(row=2, column=0, padx=20, pady=10)
        
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=20, pady=10)
        
        self.address_label = tk.Label(root, text="Address:", anchor="w")
        self.address_label.grid(row=3, column=0, padx=20, pady=10)
        
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=20, pady=10)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=20, pady=10)
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=1, padx=20, pady=10)
        
        self.view_box = tk.Text(root, wrap=tk.WORD, width=70, height=10)
        self.view_box.grid(row=6, columnspan=3, padx=20, pady=10)
        
        self.search_label = tk.Label(root, text="Search:", anchor="w")
        self.search_label.grid(row=7, column=0, padx=20, pady=10)
        
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=7, column=1, padx=20, pady=10)
        
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=2, padx=20, pady=10)
        
        self.update_button = tk.Button(root, text="Update", command=self.update_contact)
        self.update_button.grid(row=8, column=0, padx=20, pady=10)
        
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=8, column=1, padx=20, pady=10)
    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    
    def view_contacts(self):
        contacts_list = ""
        for contact in self.contacts:
            contacts_list += f"Name: {contact['name']}, Phone: {contact['phone']},   email: {contact['email']},   address: {contact['address']}\n"
        
        if contacts_list:
            self.view_box.delete("1.0", tk.END)  # Clear previous content
            self.view_box.insert(tk.END, contacts_list)
        else:
            self.view_box.delete("1.0", tk.END)
            self.view_box.insert(tk.END, "No contacts found.")
    
    def search_contact(self):
        query = self.search_entry.get()
        search_results = ""
        
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                search_results += f"Name: {contact['name']}, Phone: {contact['phone']}, email: {contact['email']}, address: {contact['address']}\n"
        
        if search_results:
            messagebox.showinfo("Search Results", search_results)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")
    
    def update_contact(self):
        selected_contact = self.search_entry.get()
        
        for index, contact in enumerate(self.contacts):
            if selected_contact.lower() in contact['name'].lower() or selected_contact in contact['phone']:
                updated_name = self.name_entry.get()
                updated_phone = self.phone_entry.get()
                updated_email = self.email_entry.get()
                updated_address = self.address_entry.get()
                
                self.contacts[index]['name'] = updated_name
                self.contacts[index]['phone'] = updated_phone
                self.contacts[index]['email'] = updated_email
                self.contacts[index]['address'] = updated_address
                
                self.clear_entries()
                messagebox.showinfo("Success", "Contact updated successfully.")
                return
        
        messagebox.showerror("Error", "Contact not found.")
    
    def delete_contact(self):
        selected_contact = self.search_entry.get()
        
        for index, contact in enumerate(self.contacts):
            if selected_contact.lower() in contact['name'].lower() or selected_contact in contact['phone']:
                del self.contacts[index]
                self.clear_entries()
                messagebox.showinfo("Success", "Contact deleted successfully.")
                return
        
        messagebox.showerror("Error", "Contact not found.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
