import cv2
import numpy as np
from pynput.mouse import Button, Controller
import time
import mss
import os

# Настройки
template_folder = "/home/follen/1/templates/"  # Укажите правильный путь к вашим шаблонам
template_files = ["template1.png", "template2.png"]  # Имена файлов шаблонов
mouse = Controller()

# Определение рабочей области
x, y, width, height = 257, 117, 437, 947 # Задайте координаты и размеры окна

def capture_screen(x, y, width, height):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screen = np.array(sct.grab(monitor))
        return screen[:, :, :3]  # Убираем альфа-канал

def find_template(screen, template):
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    return max_loc, max_val

def click_at(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)

def main():
    templates = [cv2.imread(os.path.join(template_folder, file), 0) for file in template_files]
    for idx, template in enumerate(templates):
        if template is None:
            print(f"Ошибка: не удалось загрузить шаблон {template_files[idx]}. Проверьте путь к шаблону.")
            return
        if template.shape[0] > height or template.shape[1] > width:
            print(f"Ошибка: шаблон {template_files[idx]} больше рабочего окна. Убедитесь, что размер шаблона меньше или равен размеру окна.")
            return
    
    threshold = 0.8  # Пороговое значение для нахождения шаблона

    while True:
        start_time = time.time()
        screen = capture_screen(x, y, width, height)

        for template in templates:
            loc, val = find_template(screen, template)
            if val >= threshold:
                template_height, template_width = template.shape
                center_x = x + loc[0] + template_width // 2
                center_y = y + loc[1] + template_height // 2
                print(f"Найден шаблон с совпадением {val:.2f} в координатах ({center_x}, {center_y})")
                click_at(center_x, center_y)
                
                # Прерываем поиск, если шаблон найден и клик выполнен
                break
        
        # Вывод времени выполнения цикла для отладки
        end_time = time.time()
        print(f"Cycle time: {end_time - start_time}")

if __name__ == "__main__":
    main()

