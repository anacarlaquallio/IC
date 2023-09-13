from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Gerar um par de chaves RSA: e = 65537 e k = 2048
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048)

# Obter a chave pública a partir da chave privada
public_key = private_key.public_key()

# Mensagem para cifrar
message = b"RSA encryption!"

# Cifrar a mensagem com a chave pública
#OAEP inclui uma função de máscara de geração (MGF1) e usa um algoritmo de hash (SHA-256 neste caso) 
# para garantir a segurança do processo de cifragem
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#ciphertext = public_key.encrypt(
#    message,
#    padding.PKCS1v15()  # Esquema de padding
#)

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#plaintext = private_key.decrypt(
#    ciphertext,
#    padding.PKCS1v15()  # Esquema de padding
#)

# Converter as chaves para representações em bytes
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Exibir as chaves e a mensagem original
print("Chave privada:\n", private_pem.decode())
print("\nChave pública:\n", public_pem.decode())
print("Mensagem original:", message.decode())
print("Mensagem decifrada:", plaintext.decode())