"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.py
to draw the line base on the data
Name: Charlie Liu
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
    years = len(YEARS)                                                   # get the length of list of YEARS
    line_length = width - (2 * GRAPH_MARGIN_SIZE)                        # the whole length of the line
    """
    calculate the x position base on the length of the list of YEARS, year index, the whole length of the line, and the 
    GRAPH_MARGIN_SIZE
    """
    x_position = GRAPH_MARGIN_SIZE + (line_length * (year_index/years))
    return x_position                                                    # return the x position


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
    # add the horizontal line on the top of the window
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       fill='black')
    # add the horizontal line on the bottom of the window
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, fill='black')
    for i in range(len(YEARS)):                               # for loop to draw line for each year
        x = get_x_coordinate(CANVAS_WIDTH, i)                 # get the x position using year index and length of line
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill='black')  # draw the vertical line
        canvas.create_text((x+TEXT_DX), (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), text=YEARS[i],
                           fill='black', anchor=tkinter.NW, font='Times 10')  # add the year text on the intersection


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
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_index = 1                                # use to calculate which color is should be for text and line
    color = ''                                     # empty string for storage the color we get
    for name_ele in lookup_names:                  # for every name element in lookup_names
        if name_ele in name_data:                  # check if the name is in name_data dictionary
            """
            use two loop to get two point to draw a line
            """
            for i in range(len(YEARS)-1):          # for loop 1 to get a point
                j = i + 1                          # use to create the other for loop to get the other point
                # first point
                year_a = YEARS[i]                  # get the year value from YEARS list
                x_position_a = get_x_coordinate(CANVAS_WIDTH, i)  # get the x position for point-a
                """
                if year in the year rank dictionary, mean the rank is not excess 1000
                if not in dictionary, mean excess 1000, and there will no record
                """
                if str(year_a) in name_data[name_ele]:
                    rank_a = name_data[name_ele][str(year_a)]  # get the rank and use the rank to calculate y position
                    y_position_a = (int(rank_a) / 1000) * (CANVAS_HEIGHT - (2 * GRAPH_MARGIN_SIZE)) + GRAPH_MARGIN_SIZE
                else:
                    # there is no record, so y position is on bottom line
                    y_position_a = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                # second point
                year_b = YEARS[j]                                    # get the year value from YEARS list
                x_position_b = get_x_coordinate(CANVAS_WIDTH, j)     # get the x position for point-a
                """
                if year in the year rank dictionary, mean the rank is not excess 1000
                if not in dictionary, mean excess 1000, and there will no record                
                """
                if str(year_b) in name_data[name_ele]:
                    rank_b = name_data[name_ele][str(year_b)]   # get the rank and use the rank to calculate y position
                    y_position_b = (int(rank_b) / 1000) * (CANVAS_HEIGHT - (2 * GRAPH_MARGIN_SIZE)) + GRAPH_MARGIN_SIZE
                else:
                    # there is no record, so y position is on bottom line
                    y_position_b = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                # decide the color of line and text
                if color_index % 4 == 1:     # if the reminder is 1
                    color = COLORS[0]        # assign red
                elif color_index % 4 == 2:   # if the reminder is 2
                    color = COLORS[1]        # assign purple
                elif color_index % 4 == 3:   # if the reminder is 3
                    color = COLORS[2]        # assign green
                elif color_index % 4 == 0:   # if the reminder is 0
                    color = COLORS[3]        # assign blue
                # add line, using two point data to draw a line
                canvas.create_line(x_position_a, y_position_a, x_position_b, y_position_b, fill=color, width=LINE_WIDTH)
                # add text
                """
                if year in the year rank dictionary, mean the rank is not excess 1000, so it will have rank data,
                so we can add on text.                
                if not in dictionary, mean excess 1000, and there will no record, so it won't have rank data, so we add
                * on the text                  
                """
                if str(year_a) in name_data[name_ele]:
                    canvas.create_text(x_position_a + TEXT_DX, y_position_a,
                                       text=f'{name_ele},{name_data[name_ele][str(year_a)]}',
                                       fill=color, anchor=tkinter.NW, font='Times 10')
                else:
                    canvas.create_text(x_position_a + TEXT_DX, y_position_a,
                                       text=f'{name_ele},*', fill=color, anchor=tkinter.NW,
                                       font='Times 10')
                """
                add the text of the last point
                """
                if j == (len(YEARS)-1):
                    if str(year_b) in name_data[name_ele]:
                        canvas.create_text(x_position_b + TEXT_DX, y_position_b,
                                           text=f'{name_ele},{name_data[name_ele][str(year_b)]}', fill=color,
                                           anchor=tkinter.NW, font='Times 10')
                    else:
                        canvas.create_text(x_position_b + TEXT_DX, y_position_b,
                                           text=f'{name_ele},*', fill=color, anchor=tkinter.NW,
                                           font='Times 10')
        color_index += 1                  # use to change the color


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
