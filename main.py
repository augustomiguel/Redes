from clienteUDP import udp
#from clienteRAW import raw


def main():
    while True:
        print("Digite qual solicitação ira ser realizada")
        print("1. Data e hora atual;")
        print("2. Uma mensagem motivacional para o fim do semestre;")
        print("3. A quantidade de respostas emitidas pelo servidor até o momento.")
        print("4. Sair")
        solicitacao=input(">")
        
        print("\nDigite qual requisição vc quer fazer\n")
        print("1. Requisição UDP ")
        print("2. Requisição RAW")
        print("3. Sair")

        opcao = input("\n> ")

        if opcao == "1":
            udp()
        elif opcao == "2":
            raw()
        elif opcao == "3":
            print("\nencerrando programa")
            break
        else:
            print("opcao inválida")



main()