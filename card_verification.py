import re

def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)][::-1]
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def get_card_brand(card_number):
    patterns = {
        "MasterCard": r"^(5[1-5][0-9]{14}|2(2[2-9][0-9]{12}|[3-6][0-9]{13}|7[01][0-9]{12}|720[0-9]{12}))$",
        "Visa (16 dígitos)": r"^4[0-9]{15}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2}|4[4-9][0-9])[0-9]{12}$",
        "EnRoute": r"^(2014|2149)[0-9]{11}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Voyager": r"^8699[0-9]{11}$",
        "Hipercard": r"^(38[0-9]{17}|60[0-9]{14})$",
        "Aura": r"^50[0-9]{14,17}$"
    }

    for brand, pattern in patterns.items():
        if re.match(pattern, card_number):
            return brand
    return None

def validar_cartao(cartao):
    cartao = re.sub(r"\D", "", cartao)  # Remove espaços e traços
    bandeira = get_card_brand(cartao)

    if not bandeira:
        return "Bandeira não reconhecida."
    
    if luhn_check(cartao):
        return f"Cartão válido. Bandeira: {bandeira}"
    else:
        return f"Cartão inválido pelo algoritmo de Luhn. Bandeira: {bandeira}"

# Exemplos de teste
cartoes = [
    "4111111111111111",  # Visa
    "5500000000000004",  # MasterCard
    "340000000000009",   # American Express
    "6011000000000004",  # Discover
    "201400000000009",   # EnRoute
    "3528000000000000",  # JCB
    "30000000000004",    # Diners Club
    "8699123456789012",  # Voyager
    "6062825624254001",  # Hipercard
    "5078601870000127985"  # Aura
]

for numero in cartoes:
    print(validar_cartao(numero))
