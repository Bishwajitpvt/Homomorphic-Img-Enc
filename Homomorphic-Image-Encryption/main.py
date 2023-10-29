# from msilib.schema import File
from PIL import Image
import numpy as np

import ImageCryptography as IC
import Paillier as Pa

from PIL import Image

def saveImage(data,filename):
    # Create a Pillow image from the NumPy array
    image = Image.fromarray(data, mode='L')

    # Save the image as a PNG file
    image.save(filename)

publicKey, privateKey = Pa.generate_keys()
print(publicKey.__repr__())

im = Image.open(r"S:\Homomorphic-Image-Encryption-master\Homomorphic-Image-Encryption\test-images\lungcancer.jpg")
# im.show()

encrypt_image = IC.ImgEncrypt(publicKey,im)
inc_bright = IC.homomorphicBrightness(publicKey,encrypt_image,30)
data = inc_bright.astype(dtype=np.float64)
saveImage(data,"encrypted-images/img-enc.bmp")

im = IC.ImgDecrypt(publicKey,privateKey,inc_bright)
im.save("encrypted-images/img-dec.bmp")

im.show()