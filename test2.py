def rot13(meddelande):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ "
    kod = ""
    for bokstav in meddelande:
        index = (alfabet.find(bokstav) + 13) % 30
        kod = kod + alfabet[index]
    return kod

def decrypt(meddelande):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ "
    kod = ""
    for bokstav in meddelande:
        index = (alfabet.find(bokstav) + 17) % 30
        kod = kod + alfabet[index]
    return kod

meddelande = input().upper()
print(rot13(meddelande))

meddelande2 = input().upper()
print(decrypt(meddelande2))