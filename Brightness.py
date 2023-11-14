import screen_brightness_control as sbc

print(sbc.get_brightness())

sbc.set_brightness(50)

print(sbc.get_brightness())
sbc.set_brightness(75, display=0)

print(sbc.get_brightness())