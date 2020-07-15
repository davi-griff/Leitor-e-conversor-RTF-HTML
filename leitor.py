from striprtf.striprtf import rtf_to_text

print("-----------------------------SGI-----------------------------")
print("Limpe seu texto do SISP-01")
continua = ''
while continua != 'n':
    print("Digite seu código RTF:")
    rtf = input()
    text = rtf_to_text(rtf)
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
else:
    print()
    print()
    print()
    print("Obrigado por utilizar a limpeza RTF do Griff -- Pressione qualquer tecla para finalizar")
    print("-----------------------------SGI-----------------------------")
    print()
    input()