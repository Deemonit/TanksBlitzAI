#Данный файл отвечает только за получение сырого кадра

import mss

def get_raw_full_screen():
    with mss.MSS() as mss_object:
        #Получаем параметры нужного монитора
        monitor = mss_object.monitors[1]

        #Получаем сырой объект-снимок экрана по параметрам нужного монитора
        rawFrame = mss_object.grab(monitor)
        return rawFrame