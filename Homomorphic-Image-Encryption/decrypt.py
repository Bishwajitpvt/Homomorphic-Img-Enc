# from msilib.schema import File
from PIL import Image
import numpy as np

import ImageCryptography as IC
import Paillier as Pa
import pickle


# publicKey, privateKey = Pa.generate_keys()
# print(publicKey.__repr__())

# im = Image.open(r"S:\Homomorphic-Image-Encryption-master\Homomorphic-Image-Encryption-master\test-images\lena512gray.bmp")
# im.show()

in_publickey = int(input("Public Key: "))
in_privateKey = input("Private Key: ")
in_img_path = input("encrypted Image absolute path: ")

publicKey  = Pa.PublicKey(in_publickey)
privateKey = Pa.PrivateKey(key=in_privateKey)

encrypt_image = pickle.load(open(in_img_path,"rb"))
if encrypt_image:
    inc_bright = IC.homomorphicBrightness(publicKey,encrypt_image,30)
    im = IC.ImgDecrypt(publicKey,privateKey,inc_bright)
    # im.save("encrypted-images/demo.png")
    im.show()
    # ij = IC.saveEncryptedImg(inc_bright,"demo.png")