animais = [
    "Leão", "Tigre", "Elefante", "Girafa", "Zebra",
    "Cachorro", "Gato", "Coelho", "Cavalo", "Lobo",
    "Panda", "Águia", "Tubarão", "Golfinho", "Urso",
    "Cobra", "Jacaré", "Canguru", "Rinoceronte", "Coruja"
]

animais.sort()

with open("animais.csv", "w", encoding="utf-8") as saida:
    [saida.write(animal + "\n") for animal in animais]