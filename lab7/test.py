from hashtable import Hashtable

tabellen = Hashtable(100001)

tabellen["tranan"] = "bäret"

print(tabellen["tranan"])

print(tabellen.hashfunction("trånb"))
