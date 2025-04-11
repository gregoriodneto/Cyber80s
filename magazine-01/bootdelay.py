import time
import sys

def boot():    
    texto = "Iniciando sistema Hacker80s...\nCarregando módulos...\nProduto.\n"
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.05)

if __name__ == "__main__":
    boot()