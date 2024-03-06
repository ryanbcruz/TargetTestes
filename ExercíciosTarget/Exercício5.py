def inverter_string(s):
    tamanho = len(s)
    string_invertida = ''
    for i in range(tamanho - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Exemplo de uso
entrada = input("Digite uma string para inverter: ")
string_invertida = inverter_string(entrada)
print("String original:", entrada)
print("String invertida:", string_invertida)
