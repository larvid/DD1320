def rot13(meddelande):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kod = ""
    for bokstav in meddelande:
        index = (alfabet.find(bokstav) + 13) % 26
        kod = kod + alfabet[index]
    return kod

meddelande = input().upper()
print(rot13(meddelande))