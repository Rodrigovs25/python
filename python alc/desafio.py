print("Today's date?")
dia = input()
print("Breakfast calories?")
bcalo = int(input())
print("Dinner calories?")
dcalo = int(input())
print("Snack calories?")
scalo = int(input())

soma = bcalo + dcalo + scalo

print("Calors content for " + dia + ": " + str(soma))
