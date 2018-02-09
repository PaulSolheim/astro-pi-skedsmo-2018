from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
text = []
sense.set_rotation(270)

def init_text():
    # Gruppe 1
    text.append("Vincent")
    text.append("Alex")
    text.append("Max")
    text.append("Christian")
    text.append("Tomas")
    text.append("William")
    text.append("Huy")
    text.append("Theodor")
    text.append("Andreas")
    text.append("Arvan")
    text.append("Peter")
    text.append("Leonard")
    text.append("Oliver")
    text.append("Gunnar")
    text.append("Ellen")
    text.append("Vilje")
    text.append("Gabriela")
    text.append("Mathilde")
    text.append("Amalie")
    text.append("Daniel")
    text.append("Fabian")
    # Gruppe 2
    text.append("Thomas")
    text.append("Eline")
    text.append("Marius")
    text.append("Aina")
    text.append("Eline")
    text.append("Sebastian")
    text.append("Ashiq")
    text.append("Marius")
    text.append("Mikkel")
    text.append("Jonas")
    text.append("Robin")
    text.append("Amelie")
    text.append("Teodor")
    text.append("Haakon")
    text.append("Alessandro")
    text.append("Sander")
    text.append("Vincent")
    text.append("Lin-Na")
    text.append("Andrei")
    text.append("Colin")
    text.append("William")
    text.append("Evelin")
    text.append("Froeya")
    text.append("Henrik")
    text.append("Danny")
    # Gruppe 3
    text.append("Haakan")
    text.append("Linnea")
    text.append("Edvard")
    text.append("Tinius")
    text.append("August")
    text.append("Rasmus")
    text.append("Mathias")
    text.append("Martin")
    text.append("Helene")
    text.append("Glenn Andre")
    text.append("Elias-Andre")

def show_text():
    maximum = len(text) - 1
    chosen_text = text[randint(0, maximum)]
    sense.show_message(chosen_text)
