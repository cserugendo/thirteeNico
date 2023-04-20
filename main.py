import matplotlib.pyplot as plt
import numpy as np

def somme_chiffres(heure: int, minute: int):
    somme_des_heures = sum(int(chiffre) for chiffre in str(heure))
    somme_des_minutes = sum(int(chiffre) for chiffre in str(minute))
    return somme_des_heures + somme_des_minutes


def somme_nombres(heure: int, minute: int):
    return heure + minute


occurrences = []
for heure in range(0, 24):
    for minute in range(0, 60):
        if (
            somme_chiffres(heure=heure, minute=minute) == 13
            or somme_nombres(heure=heure, minute=minute) == 13
        ):
            occurrences.append(heure)
            print(f'{heure}:{minute}')

plt.hist(occurrences, bins= np.arange(0, 25) - 0.5, edgecolor="black")
plt.xlabel("Heure")
plt.ylabel("Occurence")
plt.savefig('fig.png')
