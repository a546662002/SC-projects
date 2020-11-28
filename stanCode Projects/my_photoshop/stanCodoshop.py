"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    red_squ = (red - pixel.red) * (red - pixel.red)                 # calculate the red part
    green_squ = (green - pixel.green) * (green - pixel.green)       # calculate the green part
    blue_squ = (blue - pixel.blue) * (blue - pixel.blue)            # calculate the blue part
    color_dis_squ = red_squ + green_squ + blue_squ                  # calculate the square of color distance
    color_dis = math.sqrt(color_dis_squ)                            # get the square root
    return color_dis                                                # return color distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_total = 0                          # set variable for calculate total value for pixel in red
    green_total = 0                        # set variable for calculate total value for pixel in green
    blue_total = 0                         # set variable for calculate total value for pixel in blue
    rgb = []                               # set a list for storage the average value
    for ele in pixels:                     # for each element in pixel
        red_total += ele.red               # calculate total value for pixel in red
        green_total += ele.green           # calculate total value for pixel in green
        blue_total += ele.blue             # calculate total value for pixel in blue
    red = red_total / len(pixels)          # calculate average for red
    green = green_total / len(pixels)      # calculate average for green
    blue = blue_total / len(pixels)        # calculate average for blue
    rgb.append(int(red))                   # add average value of red in list
    rgb.append(int(green))                 # add average value of green in list
    rgb.append(int(blue))                  # add average value of blue in list
    return rgb                             # return the list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb_list = get_average(pixels)                     # get the average list of RGB
    blue = rgb_list.pop()                              # separate the blue average
    green = rgb_list.pop()                             # separate the green average
    red = rgb_list.pop()                               # separate the red average
    short_dis = 0                                      # set short distance variable
    best_pixel = pixels.pop()                          # assume the best pixel is the first one
    time = 1                                           # set a time variable for count how many pixel in pixels
    for pixel in pixels:                               # for every pixel in pixels
        dis = get_pixel_dist(pixel, red, green, blue)  # get the color distance for pixel
        """
        for the 1st time, assume we all get the best value for color distance and pixel
        for the second time and others, use to compare it
        """
        if time == 1:
            short_dis = dis                            # get shortest distance
            best_pixel = pixel                         # get best pixel
        else:
            if dis < short_dis:                        # if we find the other shortest distance
                short_dis = dis                        # replace the distance
                best_pixel = pixel                     # replace the best pixel
        time += 1                                      # for the next one pixel
    return best_pixel                                  # return the result


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for y in range(height):                       # for the every pixel
        for x in range(width):
            pixels = []                           # set a list called pixels
            for image in images:                  # for every image in images
                pixel = image.get_pixel(x, y)     # get the same position pixel in every image
                pixels.append(pixel)              # add it to the pixels
            best = get_best_pixel(pixels)         # get the best pixel in the pixels
            solve_pixel = result.get_pixel(x, y)  # for the every pixel in the result
            solve_pixel.red = best.red            # assign the value to the solve_pixel
            solve_pixel.green = best.green        # assign the value to the solve_pixel
            solve_pixel.blue = best.blue          # assign the value to the solve_pixel
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
