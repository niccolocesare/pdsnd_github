import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    cities = ['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nWould you like to see data for Chicago, New York City, or Washington? \n>> ').lower()
            if city in CITY_DATA:
                print('{} is the city you have selected!'.format(city.title()))
                break
            elif city not in CITY_DATA:
                print('\nWrong city value. Please retry.')
        except:
            pass

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('\nBy which month would you like to filter the data? \n(Choose between: All, January, February, March, April, May, June) \n>> ').lower()
            if month in months:
                print(f'{month.title()} is the month value you have selected!')
                break
            elif month not in months:
                print('\nWrong input value. Please try again.')
        except:
            pass

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nBy which day would you like to filter the data? \n(Choose between: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) \n>> ').lower()
            if day in days:
                print(f'{day.title()} is the day value you have selected!\n')
                break
            elif day not in days:
                print('\nWrong input value. Please try again')
        except:
            pass

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe

    # convert the Start Time column to datetime

    # extract month and day of week from Start Time to create new columns

    # filter by month if applicable

        # use the index of the months list to get the corresponding int

        # filter by month to create the new dataframe

    # filter by day of week if applicable

        # filter by day of week to create the new dataframe


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # TO DO: display the most common day of week

    # TO DO: display the most common start hour


    print("\n[This took %s seconds.]\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # TO DO: display most commonly used end station

    # TO DO: display most frequent combination of start station and end station trip


    print("\n[This took %s seconds.]\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # TO DO: display mean travel time


    print("\n[This took %s seconds.]\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # TO DO: Display counts of gender

        # TO DO: Display earliest, most recent, and most common year of birth


    print("\n[This took %s seconds.]\n" % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? \nEnter yes or no.\n>> ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
