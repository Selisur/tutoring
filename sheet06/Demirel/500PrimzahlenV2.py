count = 0
n = 2
primes = []

# Füge 2 gleich hinzu, da es die erste Primzahl ist
primes.append("2")
count += 1
n = 3  # Starte von 3, da 2 bereits hinzugefügt wurde

while count < 500:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(str(n))
        count += 1
    n += 2  # Nur ungerade Zahlen werden überprüft

# Speichere die Primzahlen in einer Datei
with open("primzahl.txt", "w") as file:
    for s in primes:
        file.write(s + "\n")
