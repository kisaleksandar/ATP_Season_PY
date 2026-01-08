
from src.AtpFinals import AtpFinals
from src.Championship import Championship

list_of_tournaments = ["Australian Open", "Indian Wells Masters", "Miami Open", "Monte-Carlo Masters", "Madrid Open", "Italian Open", "French Open", "Wimbledon", "Canadian Open", "Cincinnati Open", "US Open", "Shanghai Masters", "Paris Masters"]
tournaments_already_played = []

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
            if UserInput in range(4,13):
                NumOfTour = UserInput
                break
            else:
                print("Nije dobar broj turnira!")

    for i in range(UserInput):
        while True:
            UserTour = input("Unesite  turnir koji zelite da se odigra: ")
            if UserTour in list_of_tournaments and UserTour not in tournaments_already_played:
                tournaments_already_played.append(UserTour)
                break
            elif UserTour in tournaments_already_played:
                print("Turnir je vec odigran, morate odabrati drugi:")
            else:
                print("Morate pravilno uneti ime turnira: ")

        for tour_instance in championship.getTournaments():
            if UserTour == tour_instance.getName:
                Tour = tour_instance
                break

        if Tour is not None:
            Tour.play()

    while True:
        i = input("Sada ce se odigrati ATP finals turnir, jeste li spremni kapetane?: ")
        if i in ["yes", "y"]:
            Atp = AtpFinals(championship)
            Atp.play()
            for player in championship.getPlayersForTournament():
                print(f"{player.name}  points: {player.points}  rank: {player.rank}")
            break
        else:
            print("Aj razmisli jos jednom")

    print("Kraj simulacije!!!")


















                   
                   









