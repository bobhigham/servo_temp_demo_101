def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P1, 1)
    servos.P0.set_angle(1)
    basic.pause(30)
    pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 1)
    servos.P0.set_angle(180)
    basic.pause(30)
    pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

servos.P0.set_pulse(2000)
servos.P0.set_angle(0)
servos.P0.set_stop_on_neutral(False)