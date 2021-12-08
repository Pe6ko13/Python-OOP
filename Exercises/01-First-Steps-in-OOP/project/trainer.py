from FirstStepsOPP.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, new_pokemon):
        if new_pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(new_pokemon)
        return f"Caught {new_pokemon.name} with health {new_pokemon.health}"   #f"Cought {pokemon.pokemon_details()}"

    def release_pokemon(self, name: str):
        # pokemon_names = [p.name for p in self.pokemons]
        # if name not in pokemon_names:
        #     return f"Pokemon is not caught"

        filter_pokemons = [p for p in self.pokemons if p.name == name]
        if not filter_pokemons:
            return f"Pokemon is not caught"
        pokemon = filter_pokemons[0]
        self.pokemons.remove(pokemon)
        return f"You have released {name}"

    def trainer_data(self):
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n- {''.join(pokemon.pokemon_details() for pokemon in self.pokemons)}"


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
#
