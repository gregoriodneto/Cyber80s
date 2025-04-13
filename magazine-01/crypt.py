class Crypt():
    def __init__(self):
        self.ALFABETO = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789çáéíóúâêôãõ!@#$%&*()_+=-[]{};:'\",.<>?/\\|`~ \n"
    
    def encode(self, texto: str) -> list:
        indices = []
        for char in texto:
            if char in self.ALFABETO:
                indices.append(self.ALFABETO.index(char))
            else:
                raise ValueError(f"Caractere '{char}' não está no alfabeto.")
        return indices

    def decode(self, indices: list) -> str:
        texto = ""
        for index in indices:
            texto += self.ALFABETO[index]
        return texto

    def encrypt(self, enc_texto: list, key: int):
        cipher_texto = []
        for enc_char in enc_texto:
            cipher_texto.append((enc_char + key) % len(self.ALFABETO))
        return cipher_texto

    def decrypt(self, cipher_texto: list, key: int):
        enc_text = []
        for cipher_char in cipher_texto:
            enc_text.append((cipher_char - key) % len(self.ALFABETO))
        return enc_text

if __name__ == "__main__":
    a = Crypt()
    texto = "Olá, tudo bem! :)"
    print("Texto:",texto)
    encoded = a.encode(texto)
    print("Encoded:",encoded)
    encrypted = a.encrypt(encoded, 2)
    print("Encrypted:",encrypted)
    print("Decoded:",a.decode(encrypted))
    print()
    decrypted = a.decrypt(encrypted, 2)
    print("Decrypted:",decrypted)
    print("Decrypted and Decoded:",a.decode(decrypted))