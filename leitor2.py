from striprtf.striprtf import rtf_to_text

print("-----------------------------SGI-----------------------------")
print("Limpe seu texto do SISP-01")
continua = ''
linha = " "

while continua != 'n':
    print("Digite seu código RTF: (ao final da cola digite um '.') ")
    while True:
        print("> ", end="")
        line = input()
        if line == ".":
            break
        linha += line
    text = rtf_to_text(linha)
    print()
    print()
    print()
    print()
    print(text)
    print()
    print()
    print()
    print("Deseja continuar? (s/n)")
    continua = input()
    linha = " "
else:
    print()
    print()
    print()
    print("Obrigado por utilizar a limpeza RTF do Griff -- Pressione qualquer tecla para finalizar")
    print("-----------------------------SGI-----------------------------")
    print()
    input()