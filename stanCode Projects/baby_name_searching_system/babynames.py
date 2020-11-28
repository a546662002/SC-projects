"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
read and add the data to the dictionary
Name: Charlie Liu
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.
    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add
    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.
    """
    year_rank_d = {}                                   #  a dictionary, key is year and value is rank
    year_rank_d[year] = rank                           # put to key value pair
    if name in name_data:                              # if name exist in dictionary
        if year in name_data[name]:                    # if year exist in year_rank_dictionary
            rank_temp = name_data[name][year]           # set a variable - rank_temp, use it to compare rank
            if int(rank_temp) > int(rank):              # if rank is smaller
                name_data[name][year] = rank            # assign rank to value
            else:                                       # if rank_temp is smaller
                name_data[name][year] = rank_temp       # assign rank_temp to value
        else:                                          # if year do not exist
            name_data[name][year] = rank                # add year rank to dictionary
    else:
        name_data[name] = year_rank_d                  # if name do not exist, add name and year_rank_dictionary pair


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """

    with open(filename, 'r') as f:
        year = ''                                                # a string to storage year
        for line in f:                                           # for every line in the file
            data_list = line.split(',')                          # separate line using ","
            if len(data_list) == 1:                              # if the length og the line is 1
                year = data_list[0]                              # get the value
                year = year.strip()                              # erase all the spacing
            else:
                rank = data_list[0]                              # get the rank value
                rank = rank.strip()                              # erase all the spacing
                name1 = data_list[1]                             # get the name value
                name1 = name1.strip()                            # erase all the spacing
                name2 = data_list[2]                             # get the name value
                name2 = name2.strip()                            # erase all the spacing
                add_data_for_name(name_data, year, rank, name1)  # add the name, rank, year to name_data dictionary
                add_data_for_name(name_data, year, rank, name2)  # add the name, rank, year to name_data dictionary


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}                    # create a dictionary for storage name year rank data
    for ele in filenames:             # for every element in filenames
        add_file(name_data, ele)      # add the text in the element (filename in filenames) to dictionary
    return name_data                  # return name_data dictionary


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    names = []                     # a list storage name fit target
    target = target.lower()        # convert target into lower alphabet
    for ele in name_data:          # for every element in name_data dictionary
        ele_lower = ele.lower()    # convert element into lower alphabet
        if target in ele_lower:    # if target in element
            names.append(ele)      # add the element to the names list
    return names                   # return the list


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
