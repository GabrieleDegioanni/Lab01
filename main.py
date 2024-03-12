import random


class Domanda:
    def __init__(self, testo, difficolta, risp_corr, risp1, risp2, risp3):
        self.testo = testo
        self.difficolta = difficolta
        self.risp_corr = risp_corr
        self.risp1 = risp1
        self.risp2 = risp2
        self.risp3 = risp3

    def __repr__(self):
        return f"Testo: '{self.testo}', Difficolta: {self.difficolta}"

    def __lt__(self, other):
        return self.difficolta < other.difficolta

    def __str__(self):
        lista_risposte = [self.risp_corr, self.risp1, self.risp2, self.risp3]
        l = list(range(4))
        random.shuffle(l)
        lista_risposte_mescolate = []
        for j in range(4):
            lista_risposte_mescolate.append(lista_risposte[l[j]])
        testo = f"{self.testo}\n{lista_risposte_mescolate[0]}\n{lista_risposte_mescolate[1]}\n{lista_risposte_mescolate[2]}\n{lista_risposte_mescolate[3]}\n"
        return testo


class Player:
    def __init__(self, nome, punteggio):
        self.nome = nome
        self.punteggio = punteggio

    def __lt__(self, other):
        return self.punteggio > other.punteggio

    def __repr__(self):
        return f"{self.nome} {self.punteggio}"


class Game:
    def __init__(self, lista_domande, giocatore, punteggio):
        self.lista_domande = seleziona_domande()
        punti = 0
        alive = True
        for i in range(0, len(self.lista_domande)):
            if alive:
                if input(self.lista_domande[i]) == self.lista_domande[i].risp_corr:
                    print("Risposta corretta")
                    punti += 1
                else:
                    print("Risposta errata")
                    alive = False
        self.punteggio = punti
        self.giocatore = Player(input(f"Punteggio raggiunto: {punti}\nInserisci il tuo nickname:\n"), punti)


def leggi_domande():
    domande = set()
    filename = "domande.txt"
    file = open(filename, "r")

    i = 1
    for line in file:
        if i == 1:
            t = line.strip("\n")
        if i == 2:
            d = int(line.strip("\n"))
        if i == 3:
            rc = line.strip("\n")
        if i == 4:
            r1 = line.strip("\n")
        if i == 5:
            r2 = line.strip("\n")
        if i == 6:
            r3 = line.strip("\n")
            dtemp = Domanda(t, d, rc, r1, r2, r3)
            domande.add(dtemp)
            i = -1
        i = i + 1

    file.close()
    return domande


def dividi_domande():
    domande_possibili = sorted(leggi_domande())
    diff_max = domande_possibili[-1].difficolta
    diff = 0
    gruppo = []
    gruppone = []
    for i in range(0, len(domande_possibili)):
        if domande_possibili[i].difficolta == diff:
            gruppo.append(domande_possibili[i])
        else:
            gruppone.append(gruppo)
            gruppo = []
            gruppo.append(domande_possibili[i])
            diff = diff + 1
        if i == len(domande_possibili) - 1:
            gruppone.append(gruppo)
    return gruppone


def seleziona_domande():
    domande_possibili = dividi_domande()
    domande = []
    for i in range(0, len(domande_possibili)):
        domande.append(random.choice(domande_possibili[i]))
    return domande


def leggi_giocatori():
    giocatori = set()
    filename = "punti.txt"
    file = open(filename, "r")

    for line in file:
        campi = line.split(" ")
        gtemp = campi[0]
        ptemp = int(campi[1].strip("\n"))
        giocatori.add(Player(gtemp, ptemp))

    file.close()
    return giocatori


def scrivi_giocatori(lista):
    filename = "punti.txt"
    file = open(filename, "w")

    for p in lista:
        file.write(f"{p.nome} {p.punteggio}\n")

    file.close()


def main():
    insieme_giocatori = set()
    insieme_partite = set()
    gioco = Game(0, 0, 0)
    insieme_partite.add(gioco)
    insieme_giocatori.add(gioco.giocatore)
    insieme_giocatori_file = leggi_giocatori()
    insieme_giocatori_fin = insieme_giocatori.union(insieme_giocatori_file)
    lista = sorted(insieme_giocatori_fin)
    scrivi_giocatori(lista)


if __name__ == "__main__":
    main()
