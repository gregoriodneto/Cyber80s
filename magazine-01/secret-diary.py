from datetime import datetime

def diary():
    while True:
        secret = input("Digite uma senha: ")
        if secret == "123456":
            print("Senha correta! Continue para digitar o seu texto diário...\n")
            texto = input("Digite um texto:")
            diario_arquivo = "diario_" + str(datetime.today().date()) + ".txt"
            hora = datetime.now().strftime("%H:%M:%S")
            with open(diario_arquivo, "a") as arquivo:
                arquivo.write(f"[{hora}] {texto}\n")
        else:
            print("Senha incorreta. Encerrando o programa.")
            break

if __name__ == "__main__":
    diary()