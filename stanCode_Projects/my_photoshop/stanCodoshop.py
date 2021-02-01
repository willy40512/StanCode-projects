"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

The file can synchronize the images input by users
to produce a new image which composed the most similar
place.
"""

import os
import sys
from simpleimage import SimpleImage


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
    pixel_dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return pixel_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # total is for counting the nums of pixels
    # total = 0
    img_red = 0
    img_green = 0
    img_blue = 0
    # loop each pixel
    for img in pixels:
        img_red += img.red
        img_green += img.green
        img_blue += img.blue
        # total += 1
    return [img_red//len(pixels), img_green//len(pixels), img_blue//len(pixels)]

    # avg_lis = [int(img_red/total), int(img_green/total), int(img_blue / total)]
    # return avg_lis


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """

    # pix_avg = get_average(pixels)
    # default the pixel of first img was best pixel
    # best_pixel = pixels[0]
    # b_pixel_dist = get_pixel_dist(pixels[0], pix_avg[0], pix_avg[1], pix_avg[2])
    best_color_distance = -1
    best_pixel = 0
    for pixel in pixels:
        color_dist = get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
        # nb_pixel_dist = get_pixel_dist(pixel, pix_avg[0], pix_avg[1], pix_avg[2])
        # if the color distance is the smallest, the pixel is the best pixel
        # if nb_pixel_dist < b_pixel_dist:
        #     b_pixel_dist = nb_pixel_dist
        #     best_pixel = pixel
        if best_color_distance < 0 or best_color_distance > color_dist:
            best_color_distance = color_dist
            best_pixel = pixel
    return best_pixel


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
    # the list to store the pixel of every image
    pixel_lst = []
    for i in range(result.width):
        for j in range(result.height):
            # loop every img at (i,j) and store in the list
            for img in images:
                pixel_lst.append(img.get_pixel(i, j))
            # processing the list of pixel at (i,j)
            best_pixel = get_best_pixel(pixel_lst)
            pixel = result.get_pixel(i, j)
            # paste the best pixel on the blank canvas
            pixel.red = best_pixel.red
            pixel.green = best_pixel.green
            pixel.blue = best_pixel.blue
            # clear the list for next loop
            pixel_lst = []
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
