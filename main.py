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
        testo = f"{self.testo}{lista_risposte_mescolate[0]}{lista_risposte_mescolate[1]}{lista_risposte_mescolate[2]}{lista_risposte_mescolate[3]}"
        return testo


def leggi_domande():
    domande = set()
    filename = "domande.txt"
    file = open(filename, "r")

    i = 1
    for line in file:
        if i == 1:
            t = line
        if i == 2:
            d = int(line)
        if i == 3:
            rc = line
        if i == 4:
            r1 = line
        if i == 5:
            r2 = line
        if i == 6:
            r3 = line
            dTemp = Domanda(t, d, rc, r1, r2, r3)
            domande.add(dTemp)
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




domande = seleziona_domande()
if input(domande[0]) == domande[0].risp_corr.strip("\n"):
    print("Risposta corretta")
else:
    print("Risposta errata")
