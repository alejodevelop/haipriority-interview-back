import random


def generate_card_number():
    def luhn_check(number):
        """Verifica si el número de tarjeta es válido según el algoritmo de Luhn."""

        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))

        return checksum % 10 == 0

    def generate_luhn_number(prefix, length):
        """Genera un número de tarjeta válido con un prefijo específico y longitud dada."""
        number = [int(d) for d in prefix]
        while len(number) < length - 1:
            number.append(random.randint(0, 9))

        checksum = 0
        for i, digit in enumerate(reversed(number)):
            if i % 2 == 0:
                checksum += digit
            else:
                doubled = digit * 2
                checksum += doubled if doubled < 10 else doubled - 9

        checksum = (10 - (checksum % 10)) % 10
        number.append(checksum)

        return ''.join(map(str, number))

    # Prefijo para tarjetas de débito (por ejemplo, 16 dígitos con prefijo 4 para Visa)
    prefix = '4'
    length = 16  # La longitud total de la tarjeta es generalmente 16 dígitos

    return generate_luhn_number(prefix, length)
