
import numpy as np
from PIL import Image,ImageDraw,ImageFont

def ColorGetPooling(Img):
    wide = Img.size[0]
    high = Img.size[1]
    Array = np.array(Img)
    print(Array)
    Avg = np.arange( (high-1) * (wide-1) *3).reshape(((high-1),(wide-1),3))
    for col in range(high-1):
        for lin in range(wide-1):
            for RGB in range(3):
                Avg[col][lin][RGB] = int((int(Array[col][lin][RGB]) + int(Array[col+1][lin][RGB]) + int(Array[col][lin+1][RGB]) + int(Array[col+1][lin+1][RGB]))/4)
    return np.uint8(Img)

def TransDraw(OriginImg,Text,Size,):
    wide = OriginImg.size[0]
    high = OriginImg.size[1]
    output_image = np.zeros((wide,high,3),np.uint8)
    color_image = ColorGetPooling(OriginImg)
    output_image = Image.fromarray(output_image)
    brush = ImageDraw.Draw(output_image)
    font_style = ImageFont.truetype(font="simsun.ttc",size=Size,encoding="utf-8")

    for col in range(0,high,Size):
        for lin in range(0,wide,Size):
            brush.text(xy=(col,lin), text=Text,fill=tuple(color_image[col][lin]),font=font_style)
    output_image = output_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return output_image.transpose(Image.Transpose.ROTATE_90)
Address = " " #example: "D:/Pic/test3.jpeg"
Img = Image.open(Address)
Img = TransDraw(OriginImg=Img,Text="赢",Size=14)
Img = Image.fromarray(np.uint8(Img))
Img.show()
Img.save("D:/Pic/abc.png")
