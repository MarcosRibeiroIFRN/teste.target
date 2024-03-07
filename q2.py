# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
def fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

def main():
    num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    
    if fibonacci(num):
        print("O número {} pertence à sequência de Fibonacci.".format(num))
    else:
        print("O número {} não pertence à sequência de Fibonacci.".format(num))

if __name__ == "__main__":
    main()