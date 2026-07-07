import mss
import numpy as np
from PIL import Image
from FrameRegions import MyHealthCoordinates 

with mss.MSS() as mssObject:
    
    #Получаем параметры нужного монитора
    monitor = mssObject.monitors[1]

    #Получаем сырой объект-снимок экрана по параметрам нужного монитора
    rawFrame = mssObject.grab(monitor)

    #Переводим его в массив для удобства работы
    fullFrame = np.array(rawFrame)

    #Получаем нужную область массива-кадра. Это нужная область изображения, но всё ещё просто массив
    
    #MyHealthCoordinates = (slice(200,1000),slice(400,1900))
    #y,x
    slicedImageArray = fullFrame[MyHealthCoordinates]

    #Переводим массив пикселей с каналом альфа в изображение
    slicedImage = Image.fromarray(slicedImageArray,"RGBA")

    #Сохраняем выделеную область изображения в корень проекта
    slicedImage.save("кусок.png")

    print("готово") 
