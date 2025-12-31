import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.Championship import Championship
from src.SeasonTournament import SeasonTournament

list_of_tournaments = ["Australian Open", "Indian Wells Masters", "Miami Open", "Monte-Carlo Masters", "Madrid Open", "Italian Open", "French Open", "Wimbledon", "Canadian Open", "Cincinnati Open", "US Open", "Shanghai Masters", "Paris Masters"]

if __name__ == "__main__":
    NumOfTour = 0
    UserInput = 0
    championship = Championship()
    championship.loadFiles()
    while True:

        try:
            UserInput = int(input("Koliko turnira zelite da se odigrate(min = 4, max =13): "))

        except ValueError:
            print("Morate uneti broj gospodine!")

        else:
            if UserInput >= 4 and UserInput <= 13:
                NumOfTour = UserInput
                break
            else:
                print("Nije dobar broj turnira!")

    for i in range(UserInput):
        while True:
            UserTour = input("Unesite  turnir koji zelite da se odigra: ")
            if UserTour in list_of_tournaments:
                break
            else:
                print("Morate uneti validno ime turnira sa razmakom i prvim slovom velikim")

        for tour_instance in championship.getTournaments():
            if UserTour == tour_instance.getName:
                Tour = tour_instance
                break

        Tour.play()

















                   
                   









