import random

def morra_golosa():
    """Un carta-forbice-sasso alternativo e all'italiana"""

    nome_giocatore = input("Ciao! Come ti chiami? ")
    print(f"Ciao {nome_giocatore}, benvenuto alla morra golosa!")

    while True:
        scelta_giocatore = input("Scegli tra rigatoni, penne o fusilli: ").lower()

        if scelta_giocatore not in ["rigatoni", "penne", "fusilli"]:
            print("Scelta non valida. Riprova con rigatoni, penne o fusilli.")
            continue

        PASTA = ["rigatoni", "penne", "fusilli"]
        scelta_computer = random.choice(PASTA)

        print(f"Hai scelto {scelta_giocatore} e il computer ha scelto {scelta_computer}.")

        if scelta_giocatore == scelta_computer:
            print("È un pareggio, entrambi avete scelto lo stesso formato di pasta!")
        elif (scelta_giocatore == "rigatoni" and scelta_computer == "penne") or \
             (scelta_giocatore == "penne" and scelta_computer == "fusilli") or \
             (scelta_giocatore == "fusilli" and scelta_computer == "rigatoni"):
            print(f"Congratulazioni, {nome_giocatore}! {scelta_giocatore.capitalize()} batte {scelta_computer}. Hai vinto!")
        else:
            print(f"Oh no, {nome_giocatore}! {scelta_computer.capitalize()} batte {scelta_giocatore}. Hai perso!")

        giocare_ancora = input("Vuoi continuare a sfidare il computer? (s/n): ").lower()
        if giocare_ancora != "s":
            break

    print("Grazie per aver partecipato, e buon appetito!")

morra_golosa()