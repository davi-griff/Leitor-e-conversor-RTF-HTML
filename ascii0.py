from striprtf.striprtf import rtf_to_text
import html2text

print("-----------------------------SGI-----------------------------")
print("Limpe seu texto do SISP-01 e SISP-02")
continua = ''
linha = " "
sis = ''
while continua != 'n':
    print()
    print()
    print("Qual sistema voce deseja utilizar? (1/2)")
    sis = input()
    if sis == "1":
        print("Voce selecionou SISP 01")
        print("Digite seu codigo RTF: (ao final do texto digite um '.') ")
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
    elif sis == "2":
        print()
        print("Voce selecionou SISP 02")
        print("Digite seu codigo HTML:")
        html = input()
        text = html2text.html2text(html)
        print()
        input()
        print()
        print(text)
        print()
        print()
        print()
        print("Deseja continuar? (s/n)")
        continua = input()
        text = " "
    else:
        print("Voce digitou um valor invalido")
else:
    print()
    print()
    print()
    print("Obrigado por utilizar a limpeza RTF do Griff -- Pressione qualquer tecla para finalizar")
    print("-----------------------------SGI-----------------------------")
    print()
    input()
