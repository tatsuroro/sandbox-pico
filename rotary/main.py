import sys
sys.path.append('lib')

from rotary_irq_rp2 import RotaryIRQ
import time
from machine import Pin

# プッシュスイッチ用のGPIOピンを設定
sw_right = Pin(16, Pin.OUT)
sw_left = Pin(17, Pin.OUT)

led = Pin('LED', Pin.OUT)

# Initialize the rotary encoder with specific GPIO pins and settings
rotary = RotaryIRQ(
    pin_num_clk=14,
    pin_num_dt=15,
    min_val=0,
    max_val=50,
    reverse=False,
    pull_up=True,
    half_step=True,
    range_mode=RotaryIRQ.RANGE_UNBOUNDED,
)

# Store the initial value of the rotary encoder and button state
val_old = rotary.value()

def pulse_switch(sw, duration_ms=10):
    sw.value(1)
    time.sleep_ms(duration_ms)
    sw.value(0)

# Main loop
while True:
    # Read the current value of the rotary encoder and button state
    val_new = rotary.value()

    # Check if the rotary encoder's value has changed
    if val_old != val_new:
        led.value(1)
        if val_new > val_old:
            pulse_switch(sw_right)  # 時計回りでGPIO 16をパルス
        else:
            pulse_switch(sw_left)   # 反時計回りでGPIO 17をパルス

        val_old = val_new

    # Short delay to prevent debouncing issues
    time.sleep_ms(10)
    led.value(0)