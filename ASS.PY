class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def add_reagent(self, reagent, amount):
        for _ in range(amount):
            if isinstance(reagent, Herb):
                self.herbs.append(reagent)
            elif isinstance(reagent, Catalyst):
                self.catalysts.append(reagent)

    def refine_reagents(self):
        refined_herbs = []
        refined_catalysts = []

        for herb in self.herbs:
            herb.refine()
            refined_herbs.append(Herb(herb.name, herb.potency))  # Add refined herb to the list

        for catalyst in self.catalysts:
            catalyst.refine()
            refined_catalysts.append(Catalyst(catalyst.name, catalyst.potency, catalyst.quality))  # Add refined catalyst to the list

        self.herbs = refined_herbs  # Update the herbs list with refined herbs
        self.catalysts = refined_catalysts  # Update the catalysts list with refined catalysts

    def mix_potion(self, first_ingredient, second_ingredient):
        if isinstance(first_ingredient, Herb) and isinstance(second_ingredient, Catalyst):
            return Potion(f"Super {first_ingredient.name}", first_ingredient.potency + (second_ingredient.potency * second_ingredient.quality * 1.5))
        elif isinstance(first_ingredient, Catalyst) and isinstance(second_ingredient, Potion):
            return Potion(f"Extreme {first_ingredient.name}", (first_ingredient.potency * second_ingredient.boost_attribute) * 3.0)

    def display_reagents(self):
        print("\nAvailable Reagents in the Laboratory:")
        print("Herbs:")
        for herb in self.herbs:
            print(f"{herb.name}: Potency {herb.potency}")

        print("\nCatalysts:")
        for catalyst in self.catalysts:
            print(f"{catalyst.name}: Potency {catalyst.potency}, Quality {catalyst.quality}")

    def display_potions(self):
        print("\nAvailable Potions in the Laboratory:")
        for potion in self.potions:
            print(f"{potion.name}: Boost Attribute {potion.boost_attribute}")


class Herb:
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency

    def refine(self):
        self.potency *= 2.5
        print(f"{self.name}: Potency refined to {self.potency:.2f}")


class Catalyst:
    def __init__(self, name, potency, quality):
        self.name = name
        self.potency = potency
        self.quality = quality

    def refine(self):
        if self.quality < 8.9:
            self.quality += 1.1
            print(f"{self.name}: Quality refined to {self.quality:.2f}")
        else:
            self.quality = 10
            print(f"{self.name}: Quality cannot be refined any further")


class Potion:
    def __init__(self, name, boost_attribute):
        self.name = name
        self.boost_attribute = round(boost_attribute, 2)


# Sample testing
lab = Laboratory()

# Add reagents to the laboratory
herb_data = {
    "Arbuck": 2.6, "Avantoe": 3.0, "Cadantine": 1.5, "Dwarf Weed": 2.5,
    "Irit": 1.0, "Kwuarm": 1.2, "Lantadyme": 2.0, "Torstol": 4.5
}

catalyst_data = {
    "Eye of Newt": (4.3, 1.0), "Limpwurt Root": (3.6, 1.7), "White Berries": (1.2, 2.0),
    "Potato Cactus": (7.3, 0.1), "Wine of Zamorak": (1.7, 5.0), "Blood of Orcus": (4.5, 2.2),
    "Ground Mud Rune": (2.1, 6.7), "Grenwall Spike": (6.3, 4.9), "Ground Miasma Rune": (3.3, 5.2)
}

for herb_name, potency in herb_data.items():
    lab.add_reagent(Herb(herb_name, potency), 5)

for catalyst_name, (potency, quality) in catalyst_data.items():
    lab.add_reagent(Catalyst(catalyst_name, potency, quality), 10)

# Display available reagents in the laboratory
lab.display_reagents()

# Mix potions
herb = lab.herbs[0]
catalyst = lab.catalysts[0]
potion = lab.mix_potion(herb, catalyst)
lab.potions.append(potion)
lab.display_potions()

# Refine reagents in the laboratory
lab.refine_reagents()
lab.display_reagents()
