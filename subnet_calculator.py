import tkinter as tk
from tkinter import messagebox
import ipaddress

class SubnetCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Subnet Calculator")
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        explanation_text = (
            "Welcome to the Subnet Calculator!\n\n"
            "What is a Network?\n"
            "A network is a group of devices, like computers, phones, and printers, that are connected so they can share information and resources.\n\n"
            "What is an IP Address?\n"
            "An IP address is a unique address for each device on the network, like a phone number, that helps devices find and communicate with each other.\n\n"
            "What is Subnetting?\n"
            "Subnetting is the process of dividing a large network into smaller, more manageable pieces called subnets. Each subnet has its own range of IP addresses. This helps improve network performance, security, and management.\n\n"
            "Why Subnetting is Important:\n"
            "- Better Performance: Reduces unnecessary data traffic, making your network faster.\n"
            "- More Security: Isolates parts of the network to contain security issues.\n"
            "- Easier Management: Simplifies the management of the network.\n\n"
            "How to Find Your IP Address:\n"
            "1. On Windows: Open Command Prompt: Type 'cmd' in the search bar and press Enter. Type 'ipconfig' and press Enter. Look for 'IPv4 Address'.\n"
            "2. On Mac: Open Terminal: Type 'Terminal' in the search bar and press Enter. Type 'ifconfig' and press Enter. Look for 'inet' under 'en0' or 'en1'.\n"
            "3. On Linux: Open Terminal: Usually found in the applications menu. Type 'hostname -I' and press Enter.\n\n"
            "How to Use the Subnet Calculator:\n"
            "1. Base IP Address: This is the main address of your network (e.g., 192.168.1.0).\n"
            "2. Prefix Length: Determines the size of your subnet. A common prefix length is 24, which means your subnet can have up to 256 addresses.\n"
            "3. Number of Subnets: How many smaller networks you want to create.\n\n"
            "Get Started\n"
            "To calculate your subnets, enter your base IP address, prefix length, and the number of subnets you need."
        )
        
        tk.Label(self.root, text=explanation_text, justify=tk.LEFT, wraplength=600).pack(pady=10)
        
        tk.Label(self.root, text="Enter the base IP address (e.g., 192.168.1.0):").pack()
        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.pack()
        
        tk.Label(self.root, text="Enter the prefix length (e.g., 24):").pack()
        self.prefix_entry = tk.Entry(self.root)
        self.prefix_entry.pack()
        
        tk.Label(self.root, text="Enter the number of subnets needed:").pack()
        self.subnets_entry = tk.Entry(self.root)
        self.subnets_entry.pack()
        
        tk.Button(self.root, text="Calculate Subnets", command=self.calculate_subnets).pack(pady=10)
        self.output_label = tk.Label(self.root, text="Calculated Subnets:")
        self.output_label.pack()
        
        self.output_text = tk.Text(self.root, height=10, width=70)
        self.output_text.pack()
        
    def calculate_subnets(self):
        base_ip = self.ip_entry.get()
        prefix_length = int(self.prefix_entry.get())
        num_subnets = int(self.subnets_entry.get())
        
        try:
            network = ipaddress.ip_network(f"{base_ip}/{prefix_length}", strict=False)
            subnets = list(network.subnets(prefixlen_diff=num_subnets))
            
            self.output_text.delete(1.0, tk.END)
            for subnet in subnets:
                self.output_text.insert(tk.END, f"{subnet}\n")
                
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = SubnetCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
