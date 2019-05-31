class Electrolamp:
    color_of_light = "white"

    def __init__(self, manufacturer=None, effective_lighting_power=None, guaranteed_length_of_work=None,
                 producing_country=None, corpus_material=None, number_of_lamps=None, price=None):
        self.manufacturer = manufacturer
        self.effective_lighting_power = effective_lighting_power
        self.guaranteed_length_of_work = guaranteed_length_of_work
        self.producing_country = producing_country
        self.corpus_material = corpus_material
        self.number_of_lamps = number_of_lamps
        self.price = price

    def __str__(self):
        print(
               "\nmanufacturer: ", self.manufacturer,
               "\neffective_lighting_power: ", self.effective_lighting_power,
               "\nguaranteed_length_of_work: ", self.guaranteed_length_of_work,
               "\nproducing_country: ", self.producing_country,
               "\ncorpus_material: ", self.corpus_material,
               "\nnumber_of_lamps: ", self.number_of_lamps)

    @staticmethod
    def color():
        print("color_of_light:", Electrolamp.color_of_light, "\n")

    def __del__(self):
         pass

