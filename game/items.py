class Item():
        #base item class
        def __init__(slef, name, description, value):
            self.name = name
            self.description = description
            self.value = value

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
