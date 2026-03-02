from hashtable import Hashtable

tabellen = Hashtable(101)

tabellen["tranan"] = "bäret"

print(tabellen["tranan"])

print(tabellen.hashfunction("tranbär"))
