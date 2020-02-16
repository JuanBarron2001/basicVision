import Servo
import camera

cam = camera.Camera(0)
servo = Servo.Servo('COM7', 9)
servo.run_pwm(0)
servo.set_Angle(90)

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
    servo.set_angle(power)


while True:
    main()
