"""
File: Milestone1.py
Name: Charlie Liu
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.
    :param name_data: a dictionary holding name and year and rank data
    :param year: str, the year of the data entry to add
    :param rank: str, the rank of the data entry to add
    :param name: str, the name of the data entry to add
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
# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #


def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
