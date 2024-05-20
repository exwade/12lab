import tkinter as tk

class IceCreamStand:
    def __init__(self, flavors):
        self.flavors = flavors

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def check_flavor_availability(self, flavor):
        if flavor in self.flavors:
            return f"{flavor}: Доступно"
        else:
            return f"{flavor}: Нет в наличии"

# Создаем экземпляр класса IceCreamStand
ice_cream_stand = IceCreamStand(["Ваниль", "Шоколад", "Клубника", "Карамель"])

class IceCreamGUI:
    def __init__(self, root, ice_cream_stand):
        self.root = root
        self.ice_cream_stand = ice_cream_stand
        
        self.root.title("Ice Cream Stand")

        self.flavor_label = tk.Label(root, text="Flavors:")
        self.flavor_label.grid(row=0, column=0, padx=10, pady=5)

        self.flavor_listbox = tk.Listbox(root, width=20, height=6)
        self.flavor_listbox.grid(row=1, column=0, padx=10, pady=5)
        for flavor in self.ice_cream_stand.flavors:
            self.flavor_listbox.insert(tk.END, flavor)

        self.new_flavor_entry = tk.Entry(root)
        self.new_flavor_entry.grid(row=2, column=0, padx=10, pady=5)

        self.add_flavor_button = tk.Button(root, text="Add Flavor", command=self.add_flavor)
        self.add_flavor_button.grid(row=3, column=0, padx=10, pady=5)

        self.remove_flavor_button = tk.Button(root, text="Remove Flavor", command=self.remove_flavor)
        self.remove_flavor_button.grid(row=4, column=0, padx=10, pady=5)

    def add_flavor(self):
        new_flavor = self.new_flavor_entry.get()
        self.ice_cream_stand.add_flavor(new_flavor)
        self.flavor_listbox.insert(tk.END, new_flavor)

    def remove_flavor(self):
        selected_index = self.flavor_listbox.curselection()
        if selected_index:
            flavor_to_remove = self.flavor_listbox.get(selected_index)
            self.ice_cream_stand.remove_flavor(flavor_to_remove)
            self.flavor_listbox.delete(selected_index)

# Создаем корневое окно tkinter
root = tk.Tk()

# Создаем экземпляр класса IceCreamGUI и передаем ему экземпляр класса IceCreamStand
ice_cream_gui = IceCreamGUI(root, ice_cream_stand)

# Запускаем главный цикл tkinter
root.mainloop()

