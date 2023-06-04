# Creaza un program care va cere de la utilizator:
#
# Adresa de email
# Numele de utilizator
# Și va afisa aceasta infromatie in urmatorul format:
#
# Emailul pentru Marius a fost expediat cu succes pe adresa de email mariustricolici@hotmail.com
#
# Pentru adresa de email: mariustricolici@hotmail.com Si numele de utilizator: Marius

#1
utilizator = "Marius"
email = "mariustricolici@hotmail.com"
message = f"Emailul pentru {utilizator} a fost expediat cu succes pe adresa de email {email}."
print(message)

#2
email = input("Introduceți adresa de email: ")
utilizator = input("Introduceți numele de utilizator: ")
message = f"Emailul pentru {utilizator} a fost expediat cu succes pe adresa de email {email}."
print(message)
