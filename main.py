import Servo
import camera

cam = camera.Camera(0)
servo = Servo.Servo('COM7', 9)
servo.runPwm(0)
servo.setAngle(0)

green, yellow, blue = 1, 2, 3


def main():
    # option = servo.get_option()
    option = yellow
    cam.options(option)
    cam.windows()
    cam.update_frame()
    cam.convert_frame()
    cam.boxing()
    power = cam.set_power()
    servo.setAngle(power)


while True:
    main()
