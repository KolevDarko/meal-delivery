from .models import Restoran, Meal

class Cart():
    def __init__(self):
        self.items = []
        self.quantities = []
        self.restoran = ''

    def add_item(self, meal, quantity):
        if not self.restoran or self.restoran == meal.menu.restoran:
            if meal in self.items:
                self.quantities[self.items.index(meal)] += quantity
            else:
                self.items.append(meal)
                self.quantities.append(quantity)

        else:
            self.items.clear()
            self.quantities.clear()
            self.restoran = meal.menu.restoran
            self.items.append(meal)
            self.quantities.append(quantity)

