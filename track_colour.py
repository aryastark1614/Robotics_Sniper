from picarx import Picarx
from time import sleep
from vilib import Vilib

px = Picarx()

def clamp_number(num, a, b):
    return max(min(num, max(a, b)), min(a, b))

def main():
    # Start camera
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=False)

    # Activate color detection – e.g., 'blue'
    Vilib.color_detect('blue')

    x_angle = 0
    y_angle = 0

    while True:
        if Vilib.detect_obj_parameter['color_n'] != 0:
            coordinate_x = Vilib.detect_obj_parameter['color_x']
            coordinate_y = Vilib.detect_obj_parameter['color_y']

            # Pan/tilt camera toward the object
            x_angle += (coordinate_x * 10 / 640) - 5
            x_angle = clamp_number(x_angle, -35, 35)
            px.set_cam_pan_angle(x_angle)

            y_angle -= (coordinate_y * 10 / 480) - 5
            y_angle = clamp_number(y_angle, -35, 35)
            px.set_cam_tilt_angle(y_angle)

            # Optional: Move the car forward/backward based on size?
            # You can add distance-based movement later
        else:
            print("No object detected")
        sleep(0.05)

if __name__ == "__main__":
    try:
        main()
    finally:
        px.stop()
        print("Stopped.")
