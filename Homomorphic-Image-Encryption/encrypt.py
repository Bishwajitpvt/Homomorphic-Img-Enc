# from msilib.schema import File
from PIL import Image
import numpy as np

import ImageCryptography as IC
import Paillier as Pa
import os
publicKey, privateKey = Pa.generate_keys()
im = Image.open(r"S:\Homomorphic-Image-Encryption-master\Homomorphic-Image-Encryption-master\test-images\lena512gray.bmp")
# im.show()

encrypt_image = IC.ImgEncrypt(publicKey,im)
path =  f"{publicKey.n}.png"
inc_bright = IC.homomorphicBrightness(publicKey,encrypt_image,30)
ij = IC.saveEncryptedImg(inc_bright,path)
# im.save(path)
print(f"Public Key: {publicKey.n}")
print(f"Private Key: {privateKey.λ}_{privateKey.μ}")
print(f"Encrypted Image Path: {os.getcwd()}/encrypted-images/{path}")
# print(f"encrypted image: {encrypt_image}")
# # EDF.show_encrypted_image(encrypt_image)
# im = IC.ImgDecrypt(publicKey,privateKey,inc_bright)
# im.show()