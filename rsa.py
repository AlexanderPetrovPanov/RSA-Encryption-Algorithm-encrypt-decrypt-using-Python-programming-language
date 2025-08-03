def char_to_num(c): # Речник за преобразуване на букви в числа
    mapping = {
        'А': 31, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ж': 7, 'З': 8,
        'И': 9, 'Й': 10, 'К': 11, 'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16,
        'Р': 17, 'С': 18, 'Т': 19, 'У': 20, 'Ф': 21, 'Х': 22, 'Ц': 23, 'Ч': 24,
        'Ш': 25, 'Щ': 26, 'Ъ': 27, 'Ь': 28, 'Ю': 29, 'Я': 30
    }
    return mapping.get(c.upper(), c)

def num_to_char(n): # Речник за преобразуване на числа в букви
    mapping = {
        31: 'А', 2: 'Б', 3: 'В', 4: 'Г', 5: 'Д', 6: 'Е', 7: 'Ж', 8: 'З',
        9: 'И', 10: 'Й', 11: 'К', 12: 'Л', 13: 'М', 14: 'Н', 15: 'О', 16: 'П',
        17: 'Р', 18: 'С', 19: 'Т', 20: 'У', 21: 'Ф', 22: 'Х', 23: 'Ц', 24: 'Ч',
        25: 'Ш', 26: 'Щ', 27: 'Ъ', 28: 'Ь', 29: 'Ю', 30: 'Я'
    }
    return mapping.get(n, str(n))
# може и с един речник и различни могики за code / decode

def mod_exp(base, exp, mod): # имплементира бързо модулно степенуване (важно за големи степени)
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def rsa_encrypt(message, e, n): # криптира всеки числов блок от съобщението чрез C = P^E mod N. Не е добавена функционалност като ttn
    # Криптиране на съобщението
    encrypted = []
    for char in message:
        num = char_to_num(char)
        if isinstance(num, int):
            encrypted_num = mod_exp(num, e, n)
            encrypted.append(encrypted_num)
        else:
            encrypted.append(num)
    return encrypted

def rsa_decrypt(ciphertext, d, n): # декриптира всеки блок чрез P = C^D mod N. Не е добавена функционалност като ntt да 
    decrypted = []
    for num in ciphertext:
        if isinstance(num, int):
            decrypted_num = mod_exp(num, d, n)
            decrypted.append(decrypted_num)
        else:
            decrypted.append(num)
    return decrypted

# Параметрите на RSA са статично зададени: P=3, Q=11, N=33, F(N)=20, E=3, D=7
P = 3
Q = 11
N = P * Q
F_N = (P - 1) * (Q - 1)
E = 3
D = 7

# Оригинално съобщение
# message = "дискретнаматематика"
# message = "автобусапълзинагоре"
message = input("Въведете текст: ")
print(f"Оригинално съобщение: {message}")

# Преобразуване на съобщението в числов формат
numeric_message = [char_to_num(c) for c in message]
print(f"Числов формат: {numeric_message}")

# Криптиране на съобщението
encrypted_message = rsa_encrypt(message, E, N)
print(f"Криптирано съобщение: {encrypted_message}")

# Декриптиране на съобщението
decrypted_nums = rsa_decrypt(encrypted_message, D, N)
print(f"Декриптирани числа: {decrypted_nums}")

# Преобразуване обратно в текст
decrypted_message = ''.join([num_to_char(n) for n in decrypted_nums])
print(f"Декриптирано съобщение: {decrypted_message}")
