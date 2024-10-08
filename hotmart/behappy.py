def is_happy_number(num):
    seen_numbers = set()
    
    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    
    return num == 1

# Exemplo de uso
numero = 2129
if is_happy_number(numero):
    print("Feliz")
else:
    print("Infeliz")
