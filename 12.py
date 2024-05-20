class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
        print()

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}")

# Создаем экземпляр класса Restaurant
restaurant = Restaurant("Итальянский уголок", "Итальянская кухня", 4.5)

# Выводим информацию о ресторане
restaurant.describe_restaurant()

# Обновляем рейтинг ресторана
restaurant.update_rating(4.8)

# Выводим обновленную информацию о ресторане
restaurant.describe_restaurant()



class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating, flavors, location, opening_hours):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors
        self.location = location
        self.opening_hours = opening_hours

    def display_flavors(self):
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print(f"Сорт мороженого '{new_flavor}' успешно добавлен.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого '{flavor}' успешно удален.")
        else:
            print(f"Сорт мороженого '{flavor}' отсутствует в списке.")

    def check_flavor_availability(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' доступен в данном кафе-мороженом.")
        else:
            print(f"Сорт мороженого '{flavor}' не доступен в данном кафе-мороженом.")

    def serve_popsicle_ice_cream(self):
        print("Подаю мороженое на палочке.")

    def serve_soft_serve_ice_cream(self):
        print("Подаю мягкое мороженое.")

# Создаем экземпляр класса IceCreamStand
ice_cream_stand = IceCreamStand("Мороженое рай", "Мороженое", 4.7, ["Ваниль", "Шоколад", "Клубника", "Карамель"],
                                "ул. Летняя, 25", "10:00 - 20:00")

# Выводим информацию о кафе-мороженом
ice_cream_stand.describe_restaurant()

# Выводим список сортов мороженого
ice_cream_stand.display_flavors()

# Добавляем новый сорт мороженого
ice_cream_stand.add_flavor("Банан")

# Проверяем доступность определенного сорта мороженого
ice_cream_stand.check_flavor_availability("Банан")

# Удаляем сорт мороженого
ice_cream_stand.remove_flavor("Шоколад")

# Проверяем доступность удаленного сорта мороженого
ice_cream_stand.check_flavor_availability("Шоколад")

# Подаём мороженое на палочке
ice_cream_stand.serve_popsicle_ice_cream()

# Подаём мягкое мороженое
ice_cream_stand.serve_soft_serve_ice_cream()
