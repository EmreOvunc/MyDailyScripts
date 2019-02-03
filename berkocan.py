#Emre
from PIL import ImageGrab
from time import sleep

path = "C:\\Users\\root\\Desktop\\"
x = 0

while True:
    x += 1
    snapshot = ImageGrab.grab()
    save_path = path + "berko" + str(x) + ".jpg"
    snapshot.save(save_path)
    sleep(2)
