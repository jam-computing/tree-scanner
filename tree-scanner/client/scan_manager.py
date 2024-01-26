import cv2 as cv
import time


class Scanner:
    def __init__(self):
        self.led_locations = list()
        self.cap = cv.VideoCapture(0)

    def scan_frame(self):
        # Get the image
        # This could throw an exception but... who cares
        _, image = self.cap.read()

        # Find the brightest point

        # Grayscale, blur then minmaxloc
        greyscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        cv.waitKey(1000)

        blurs = 20
        for i in range(blurs):
            blurred_image = cv.GaussianBlur(
                    greyscale_image, (9, 9), cv.BORDER_DEFAULT
                    )

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(blurred_image)

        # Draw a circle on the brightest point and save the image for debugging
        image = cv.circle(image, max_loc, 20, (0, 225, 0), 7)

        cv.imwrite(f"images/{str(time.time())}.png", image)

        # Add the normalised led location to the list

        # Get the height width and discard the number of channels
        height, width, _ = image.shape
        normalised_x = max_loc[0] / width
        normalised_y = max_loc[1] / height
        self.led_locations.append((normalised_x, normalised_y))

    def write_to_file(self):
        with open("data.txt", "w") as file:
            for point in self.led_locations:
                file.write(str(point) + "\n")
