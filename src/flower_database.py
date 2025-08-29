class FlowerDatabase:
    def __init__(self):
        self.flowers = {}

    def add_flower(self, name, scientific_name, care_info):
        self.flowers[name] = {'scientific_name': scientific_name, 'care_info': care_info}

    def get_flower_info(self, name):
        return self.flowers.get(name, 'Blume nicht gefunden')