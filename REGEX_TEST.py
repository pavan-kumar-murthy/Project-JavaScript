# file1 = open("file1.txt", 'r')
# print(file1.read())
# file1.close()
# import re
# mystr = "_The crow was travelling 910 for tigertharun a long time so he was very thirsty. He looked around for water to drink, but was unable to find any water source. He started searching for water all around the jungle and in the nearby town. After travelling around the town, the crow saw a house and thought there must be water in the house."
# print(re.findall("[^was]", mystr))
# print(re.findall("in*", mystr))
# print(re.findall("was+", mystr))
# print(re.findall("the?", mystr))
# print(re.match("the|a", mystr))
# print(re.findall("a{2}m{2}", "Python Progaamming"))
# print(re.findall("\AThe", mystr))
# print(re.findall(r"\bti", mystr))
# print(re.findall(r"\Brou", mystr))
# print(re.findall("\d", mystr))
# print(re.findall("\D", mystr))
# print(re.findall("\s", mystr))
# print(re.findall("\S", mystr))
# print(re.findall("\w", mystr))
# print(re.findall("[tharun*]", mystr))




class InventoryItem:
    def _init_(self, name, initial_quantity, price_per_unit):
        self._name = name
        self._quantity = initial_quantity
        self._price = price_per_unit

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def update_quantity(self, update_qty):
        new_quantity = self._quantity + update_qty

        if new_quantity >= 0:
            self._quantity = new_quantity
            return new_quantity
        else:
            print("Insufficient quantity")
            return None