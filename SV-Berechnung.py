import csv                                                     # importiere das CSV Modul, das du hinterlegt hast

f = open("KK_Zusatz1.csv", newline="", encoding="iso8859-15")                         # öffnen der Datei und in Variable abspeichern, f für file, newline aktiviert den universellen Zeichenmodus,Python erkennt automatisch, welcher der vielen möglichen Zeilenumbrüche genutzt wird
KKZ_csv = csv.DictReader(f, delimiter=",", quotechar='"')      # DictReader wandelt die jeweilige Zeile aus CSV Datei in ein Dictionary um, delimiter legt das Trennzeichen fest (hier ein Semikolon)
dictKKZ = {}

for dictionary in KKZ_csv:
    #print(dictionary)
    k = dictionary["Krankenkasse"]
    b = dictionary["Beitragssatz"]
    bs = float(b.replace(",", ".").replace("%", ""))  # string.replace(old,new), erzeugt eine Kopie des Strings, indem das alte Zeichen durch ein neues ersetzt wird
                                                      # wert.irgendwas -> .irgendwas ist eine Methode, die auf den Wert angewandt wird, diese Methode gibt ewas aus, auf das wieder eine Methode angewandt werden kann, daher kann es miteinander verknüpft werden
    dictKKZ[k] = bs
#print(dictKKZ)

print()
print("SV-Beitragsrechner")
print("-------------------------------")
print()

#if dictKKZ.get(kk) is None:
   # print("get mit None!!!")

entgelt = float(input("Eingabe Entgelt: "))
kk = input("Eingabe Krankenkasse: ")
while kk not in dictKKZ:
   print("Gibts nicht. Versuchs noch einmal.")
   kk = input("Eingabe Krankenkasse: ")

kinderlos = input("Über 23 Jahre ohne Kind (j/n): ")
print()
kkzusatz = dictKKZ[kk]

if kinderlos == "j":
    PVZusatz = 0.6
else:
    PVZusatz = 0

if entgelt > 538 and entgelt < 2000.01:
    print("Es liegt der Übergangsbereich vor. SV müssen mittels Faktorrechnung ermittelt werden.")
    BBGAN = round(1.351351351 * entgelt - 702.7027027, 2)
    print("Die geminderte Beitragsbemessungsgrundlage liegt bei: ", BBGAN, "Euro.")
    kv = round((7.3 + kkzusatz) * BBGAN / 100, 2)
    pv = round((2.2 + PVZusatz) * BBGAN / 100, 2)
    rv = round(9.3 * BBGAN / 100, 2)
    av = round(1.3 * BBGAN / 100, 2)
    sv = kv + pv + rv + av
    print()
    print("Die SV-Beiträge lauten: ")
    print("KV: ", kv, "Euro")
    print("PV: ", pv, "Euro")
    print("RV: ", rv, "Euro")
    print("AV: ", av, "Euro")
else :
    if entgelt < 520:
        print("Entgelt unter 538 Euro. Es sind die Regeln für geringfügige Beschäftigung zu prüfen.")
    else :
        print("Hier ist der Halbteilungsgrundsatz anzuwenden. Bemessungsgrundlage:", entgelt, "Euro.")
        print()
        kv = round((14.6 + kkzusatz) * entgelt / 100 / 2, 2)
        pv = round((2.2 + PVZusatz) * entgelt / 100, 2)
        rv = round(9.3 * entgelt / 100, 2)
        av = round(1.3 * entgelt / 100, 2)
        sv = kv + pv + rv + av
        print("Die SV-Beiträge lauten: ")
        print("KV: ", kv, "Euro")
        print("PV: ", pv, "Euro")
        print("RV: ", rv, "Euro")
        print("AV: ", av, "Euro")

print("-------------------------")
print("Es geht noch weiter.")
print("Du willst doch bestimmt wissen, wie dein Nettobetrag aussehen wird.")
print()
print("Deine Lohnsteuer kannst du hier berechnen lassen: https://www.bmf-steuerrechner.de/bl/bl2023_01/eingabeformbl2023_01.xhtml")
print("Der benötige Zusatzbeitrag der Krankenkasse lautet: ", kkzusatz)
print()
steuern = float(input("Steuern: "))
netto = entgelt - steuern - sv
print()
print("Dein Nettobetrag lautet: ", netto, "Euro.")
print()