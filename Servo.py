import pyfirmata


class Servo:
    def __init__(self, port, pwm):
        self.board = pyfirmata.Arduino(port)
        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()
        self.servo = self.board.get_pin('d:' + str(pwm) + ':s')
        self.input1 = self.board.get_pin('d:2:i')
        self.input2 = self.board.get_pin('d:3:i')

    def run_pwm(self, power):
        self.servo.write(power)

    def set_angle(self, angle):
        self.servo.write(angle)

    def get_option(self):
        value1 = 0
        value2 = 0
        if self.input1.read() == 1:
            value1 = 1
        if self.input2.read() == 1:
            value2 = 2
        option = value1 + value2
        print('option: ' + str(option))
        return option
