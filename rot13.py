def kryptera(meddelande):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    kod = ""
    for bokstav in meddelande.upper():
        if bokstav in alfabet:
            index = (alfabet.find(bokstav) + 14) % len(alfabet)
            kod += alfabet[index]
        else:
            kod += bokstav
    return kod

def dekrypt(kod):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    meddelande = ""
    for bokstav in kod:
        if bokstav in alfabet:
            index = (alfabet.find(bokstav) - 14) % len(alfabet)
            meddelande += alfabet[index]
        else:
            meddelande += bokstav
    return meddelande
if __name__ == "__main__":
    while True:

        print("\n1: Kryptera ett meddelande \n2: De-kryptera ett meddelande \nq: Avslutar")
        val = input("\nVälj 1, 2 eller q: ").strip()


        if val == "1":
            meddelande = input("\nKryptera meddelande:").strip().upper()
            print("\nkrypterat meddelande:", kryptera(meddelande))
        

        elif val == "2":
            meddelande = input("\nDekryptera meddelande: ").strip().upper()
            print ("\nDekrypterat meddelande:", dekrypt(meddelande))

        elif val == "q":
            print("Stänger ner!")
            break
        
        else:
            print("\nFel!\nVälj 1, 2 eller q")



