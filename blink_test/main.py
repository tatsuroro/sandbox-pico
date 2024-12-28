from machine import Pin
import time

# グローバル変数
encoder_position = 0
last_encoder_state = 0

# コールバック関数
def rotary_encoder_handler(pin):
    global encoder_position, last_encoder_state
    current_state = (a_pin.value() << 1) | b_pin.value()
    
    if (last_encoder_state == 0b11 and current_state == 0b01) or \
       (last_encoder_state == 0b01 and current_state == 0b00) or \
       (last_encoder_state == 0b00 and current_state == 0b10) or \
       (last_encoder_state == 0b10 and current_state == 0b11):
        encoder_position += 1
        print("CW")
    elif (last_encoder_state == 0b11 and current_state == 0b10) or \
         (last_encoder_state == 0b10 and current_state == 0b00) or \
         (last_encoder_state == 0b00 and current_state == 0b01) or \
         (last_encoder_state == 0b01 and current_state == 0b11):
        encoder_position -= 1
        print("CCW")

    last_encoder_state = current_state

# GPIOピンの設定
a_pin = Pin(14, Pin.IN, Pin.PULL_UP)
b_pin = Pin(15, Pin.IN, Pin.PULL_UP)

# 割り込みの設定
a_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=rotary_encoder_handler)
b_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=rotary_encoder_handler)

# メインループ
while True:
    time.sleep(0.1)