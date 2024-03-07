
# 5) Escreva um programa que inverta os caracteres de um string.


# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;
def inverter(s):
    inverted = ""
    for char in s:
        inverted = char + inverted
    return inverted

# Exemplo de uso
string_original = "Hello, World!"
string_invertida = inverter(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)