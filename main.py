# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def insert(aufgabe, aufgaben):
    aufgabe = "{}. "+aufgabe
    text = aufgabe.format(len(aufgaben))
    aufgaben.append(text)
    return aufgaben

def printAufgaben(aufgaben):
    print("\n")
    for x in aufgaben:
        print(x);
    print("\n")

def delete(index, aufgaben):
    aufgaben.pop(int(index))
    return aufgaben

if __name__ == '__main__':
    aufgaben = ["Hier befinden sich Ihre Aufgaben:"]
    while True:
        if(input("Wollen Sie eine neue Aufgabe anlegen? (y/n)")=="y"):
            aufgaben=insert(input("Was ist Ihre Aufgabe?:"), aufgaben)
        else:
            if(input("Wollen Sie eine Aufgabe löschen?(y/n)")):
                aufgaben=delete(input("Geben sie die Nummer der Aufgabe ein:"), aufgaben)
        printAufgaben(aufgaben)

        if(input("Wollen Sie abbrechen? (y/n)")=="y"):
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
