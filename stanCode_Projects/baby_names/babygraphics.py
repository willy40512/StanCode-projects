"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    initial_x = GRAPH_MARGIN_SIZE  # 20
    interval = (width-GRAPH_MARGIN_SIZE*2) / len(YEARS)  # 80
    target_x = initial_x + interval*year_index
    return target_x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # top fixed line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # down fixed line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # straight line for year
    for s_line in range(len(YEARS)):
        # get the certain x for certain year
        s_x = get_x_coordinate(CANVAS_WIDTH, s_line)
        canvas.create_line(s_x, 0, s_x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(s_x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[s_line], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    global COLORS
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    for i in range(len(lookup_names)):

        dic = name_data[lookup_names[i]]    # store {year:rank}

        for k in range(0, len(YEARS)-1):  # (0,11)

            s_x = get_x_coordinate(CANVAS_WIDTH, k)  # x start point of line
            s_x1 = get_x_coordinate(CANVAS_WIDTH, k+1)  # x end point of line

            # the start point of line and the text will be add in this area
            if str(YEARS[k]) not in dic:  # reassign for the miss data
                dic[str(YEARS[k])] = '1001'
                h_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # the y of the bottom line
                # adding the text beside the line
                canvas.create_text(s_x + TEXT_DX, h_rank, text=f'{lookup_names[i]} *',
                                   anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            else:
                if float(dic[str(YEARS[k])]) <= MAX_RANK:
                    rank = dic[str(YEARS[k])]
                    h_rank = (CANVAS_HEIGHT / MAX_RANK) * int(rank) + GRAPH_MARGIN_SIZE
                    # adding the text beside the line
                    canvas.create_text(s_x + TEXT_DX, h_rank, text=f'{lookup_names[i]} {rank}',
                                       anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                else:
                    h_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    # adding the text beside the line
                    canvas.create_text(s_x + TEXT_DX, h_rank, text=f'{lookup_names[i]} *',
                                       anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

            # the end point of line
            if str(YEARS[k+1]) not in dic:  # # reassign for the miss data
                dic[str(YEARS[k+1])] = '1001'  # assign the virtual rank 1001 for it
                h_n_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # the y of the bottom line
                if k + 1 == len(YEARS) - 1:  # the last name and rank
                    canvas.create_text(s_x1 + TEXT_DX, h_n_rank, text=f'{lookup_names[i]} *',
                                       anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            else:
                if float(dic[str(YEARS[k+1])]) <= MAX_RANK:
                    n_rank = dic[str(YEARS[k + 1])]
                    h_n_rank = (CANVAS_HEIGHT / MAX_RANK) * int(n_rank) + GRAPH_MARGIN_SIZE
                    if k + 1 == len(YEARS) - 1:  # the last name and rank
                        canvas.create_text(s_x1 + TEXT_DX, h_n_rank, text=f'{lookup_names[i]} {n_rank}',
                                           anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                else:
                    h_n_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # the y of the bottom line

            canvas.create_line(s_x, h_rank, s_x1, h_n_rank, width=LINE_WIDTH, fill=COLORS[i% len(COLORS)])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
