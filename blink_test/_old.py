from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")


while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")

# from machine import Pin
# from utime import sleep

# # Pin 16と17を出力モードで設定
# pin = Pin("LED", Pin.OUT)

# pin16 = Pin(16, Pin.OUT)
# pin17 = Pin(17, Pin.OUT)

# print("LED starts flashing...")

# while True:
#     try:
#         # Pin 16をON、Pin 17をOFF
#         pin16.on()
#         pin17.on()
#         pin.on()

#         sleep(5)

#         pin16.off()
#         pin17.off()
#         pin.off()
#         sleep(3)
#     except KeyboardInterrupt:
#         break

# print("Finished.")
