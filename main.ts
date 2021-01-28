input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    servos.P0.setAngle(20)
    basic.pause(30)
    pins.digitalWritePin(DigitalPin.P1, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    servos.P0.setAngle(171)
    basic.pause(30)
    pins.digitalWritePin(DigitalPin.P1, 0)
})
basic.forever(function () {
    basic.pause(10000)
    servos.P0.setAngle((input.temperature() - 6) * 3)
    basic.showNumber(input.temperature() - 6)
})
