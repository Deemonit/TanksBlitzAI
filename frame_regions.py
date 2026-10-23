##MY_HEALTH_COORDINATES = (slice(500,1400),slice(400,1900))
# frame_regions.py
# Разрешение, для которого размечены координаты
NATIVE_RESOLUTION = (2560, 1440)  # (width, height)

# Области интереса: (y_start, y_end, x_start, x_end)
# y — строки (сверху вниз), x — столбцы (слева направо)
ROI = {
    "my_hp":      (slice(1410, 1430), slice(1090, 1470)),  # здоровье моего танка
    "minimap":    (slice(50, 350),    slice(2150, 2500)),  # миникарта
    "reload":     (slice(1350, 1400), slice(1800, 2200)),  # перезарядка
    "timer":      (slice(20, 70),     slice(1200, 1400)),  # таймер
    "score":      (slice(20, 70),     slice(1050, 1200)),  # количество убитых у каждой команды
    "reload_time":(slice(710, 728),   slice(1180, 1225)),  # время перезарядки
    "equipment":  (slice(860, 1032),  slice(2502, 2553)),  # снаряжение
}