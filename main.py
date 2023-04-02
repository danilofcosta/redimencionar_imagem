#pip install pil

from PIL import Image
import os

dir=str(input('diretorio da imagem ou pasta com imagems '))
scale_percent = int(input('QUANTOS POR CENTO DA IMAGEM QUER REDUZIR? ')) or 50 # redimensionar para 50% da escala original
def redimencionar(photo):
    photox=os.path.join(dir,photo) if dir != photo else photo
    image = Image.open(photox)
    width, height = image.size
    width = int(width * scale_percent / 100)
    height = int(height * scale_percent / 100)
    image = image.resize((width, height))
    print(f'IMAGEM {photo} REDIMENCIONADA')

def verificar_diretorio(dir):
    try:
        f = open(dir)
        f.close()
        redimencionar(dir)        
    except:
        try:
            photos=os.listdir(dir)
            if photos == list:
                for i in photos:
                    redimencionar(i)
        except:
            pass
