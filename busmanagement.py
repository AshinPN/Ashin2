import tkinter as tk
from tkinter import messagebox

class BusManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Management System")
        self.buses = {}
        
        fields = ["Number", "Route", "Driver"]
        self.entries = {field: tk.Entry(root) for field in fields}
        
        for i, field in enumerate(fields):
            label = tk.Label(root, text=f"Bus {field}:")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = self.entries[field]
            entry.grid(row=i, column=1, padx=5, pady=5)
        
        actions = [
            ("Add Bus", self.add_bus),
            ("Display Buses", self.display_buses),
            ("Search Bus", self.search_bus),
            ("Delete Bus", self.delete_bus)
        ]
        
        for i, (label, command) in enumerate(actions):
            button = tk.Button(root, text=label, command=command)
            button.grid(row=i+len(fields), column=0, columnspan=2, padx=5, pady=5)
        
    def add_bus(self):
        bus_info = {field: entry.get() for field, entry in self.entries.items()}
        
        if all(bus_info.values()):
            self.buses[bus_info["Number"]] = {
                "route": bus_info["Route"],
                "driver": bus_info["Driver"]
            }
            messagebox.showinfo("Success", f"Bus {bus_info['Number']} added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    
    def display_buses(self):
        if not self.buses:
            messagebox.showinfo("Info", "No buses in the system.")
        else:
            bus_list = "\n".join([f"Bus {bus_number} - Route: {bus_info['route']}, Driver: {bus_info['driver']}" 
                                  for bus_number, bus_info in self.buses.items()])
            messagebox.showinfo("Buses", bus_list)
    
    def search_bus(self):
        bus_number = self.entries["Number"].get()
        if bus_number in self.buses:
            bus_info = self.buses[bus_number]
            messagebox.showinfo("Bus Information", f"Bus {bus_number} - Route: {bus_info['route']}, "
                                                   f"Driver: {bus_info['driver']}")
        else:
            messagebox.showinfo("Info", f"Bus {bus_number} not found in the system.")
    
    def delete_bus(self):
        bus_number = self.entries["Number"].get()
        if bus_number in self.buses:
            del self.buses[bus_number]
            messagebox.showinfo("Success", f"Bus {bus_number} deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Info", f"Bus {bus_number} not found in the system.")
    
    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BusManagementApp(root)
    root.mainloop()
