from Electrolamp import Electrolamp


def main():
    Electrolamp.color()
    LG = Electrolamp(manufacturer="Electron", effective_lighting_power=200, guaranteed_length_of_work=365,
                     producing_country="China", corpus_material="plastic", number_of_lamps=2, price=70)
    Samsung = Electrolamp(effective_lighting_power=250, guaranteed_length_of_work=500, producing_country="USA",
                          number_of_lamps=2, price=200)
    Xiaomi = Electrolamp(effective_lighting_power=180, producing_country="China", price=150)

    LG.__str__()
    Samsung.__str__()
    Xiaomi.__str__()


main()
