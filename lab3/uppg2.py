from BintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
            
    print("\n")
    with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
        engelska_ord = []
        for rad in engelskfil:
            raden = rad.strip().split()
            engelska_ord = engelska_ord + raden
        engelska = Bintree()
        for ord in engelska_ord:
            if ord in engelska:
                pass
            else:
                if ord in svenska:
                    engelska.put(ord)
                    print(ord, end = " ")
print("\n")