# from msilib.schema import File
from PIL import Image
import numpy as np

import ImageCryptography as IC
import Paillier as Pa

publicKey, privateKey = Pa.generate_keys()
# im = Image.open(r"S:\Homomorphic-Image-Encryption-master\Homomorphic-Image-Encryption-master\test-images\lena512gray.bmp")
# im.show()
print(privateKey)

p = Pa.PrivateKey()
p.λ = privateKey.λ
p.μ = privateKey.μ

print(p)

# encrypt_image = IC.ImgEncrypt(publicKey,im)