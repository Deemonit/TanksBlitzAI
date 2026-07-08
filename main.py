import numpy as np
from PIL import Image
from frame_regions import MY_HEALTH_COORDINATES

import screen_capture as scr_cap

#Переводим его в массив для удобства работы
raw_full_screen = scr_cap.get_raw_full_screen()

full_frame = np.array(raw_full_screen)

#Получаем нужную область массива-кадра. Это нужная область изображения, но всё ещё просто массив
   
#y,x
sliced_image_array = full_frame[MY_HEALTH_COORDINATES]

#Переводим массив пикселей с каналом альфа в изображение
sliced_image = Image.fromarray(sliced_image_array,"RGBA")

#Сохраняем выделеную область изображения в корень проекта
sliced_image.save("кусок.png")

print("готово") 
