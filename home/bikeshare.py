import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
          try:
              city_selection = input('would you like to see data for US bikeshare, type\n (a) for chicago\n (b) for new york city\n (c) for washington\n').lower()
              if city_selection in ('a','b','c') :
                 break 
          except KeyboardInterrupt :
            print('invalid input')
            
    if city_selection =='a':
        city = 'chicago'
    elif city_selection == 'b':
        city = 'new york city'
    elif city_selection == 'c':
        city = 'washington' 
        
         # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = [' saturday', 'sunday', 'monday','tuesday', 'wednesday','thursday','friday']

    while True :
         try :
              time_frame = input('\n\n would you like to filter {}\'s data by month , day , both or not at all ? type month or day or both or none: \n'.format(city.title())).lower()
              if time_frame in ('month' , 'day', 'both' , 'none' ) :
                    break
         except KeyboardInterrupt :
                   print('invalid input')
                
    if time_frame == 'none':
      print('\n filtering for {} for 6 months period \n'.format(city.title()))
      month = 'all'
      day = 'all'
    
    elif time_frame == 'both' :
          month_selection = input('write the month name :january, february, march, april, may, june\n').lower()
          while month_selection not in months:
               print('invalid choice')  
               month_selection = input('write the month name :january, february, march, april, may, june\n').lower() 
          if month_selection in months:
             month = month_selection
             day_selection = input('write the day name :saturday, sunday, monday,tuesday, wednesday,thursday,friday\n').lower()
          while day_selection not in days:
              print('invalid choice')
              day_selection = input('write the day name :saturday, sunday, monday,tuesday, wednesday,thursday,friday\n').lower()
          if day_selection in days :
             day = day_selection 
             month = 'all' 
   
    elif time_frame == 'month':
         month_selection = input('write the month name :january, february, march, april, may, june\n').lower()
         while month_selection not in months:
              print('invalid choice')  
              month_selection = input('write the month name :january, february, march, april, may, june\n').lower()
         month = month_selection
         day = 'all'
        
    elif time_frame == 'day':
         day_selection = input('write the day name :saturday, sunday, monday,tuesday, wednesday,thursday,friday\n').lower()
         while day_selection not in days:
               print('invalid choice')
               day_selection = input('write the day name :saturday, sunday, monday,tuesday, wednesday,thursday,friday\n').lower()
        
         day = day_selection 
         month = 'all' 
            
       
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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
    
filters = get_filters()
city, month, day = filters

print("the user input are as follows: \n")
print(city, "\n")
print(month, "\n")
print(day)

df = load_data('washington','june', 'saturday')
print(df.head())

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('most start time:', common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_s_e_station = df['Start Station'].mode()[0] + "-" + df['End Station'].mode()[0]
    print('Most frequent s e station:', most_frequent_s_e_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
station_stats(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('total trip duration:', total_trip_duration)
    
    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('Average trip duration:', average_trip_duration)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

trip_duration_stats(df)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of each user type', user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print(' counts of bike riders gender' ,gender_count)
        #Display earliest, most recent, and most common year of birth
        earliest_yob = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode()[0])
        print('\n Earliest birth year :  ',earliest_yob)
        print('\n Most recent birth year :  ',most_recent_yob)
        print('\n Most common birth year :  ',most_common_yob)
        # dealing with Washington
    except KeyError :
            print('This data is not available for Washington')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

user_stats(df)

def display_raw_data(city):
    ''' displays raw data of bikeshare in cities'''
    
    print(' your data is availble to check ...\n')
    display_raw = input(' may you have to look on the raw data ? Type yes or no.\n')
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
              print(chunk)  
              display_raw = input(' may you have to look on the raw data ? Type yes or no.\n')
              if display_raw != 'yes':
                 print('Thank You.')
                 break
            break       
        except KeyboardInterrupt:
            print('Thank You.')

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
display_raw_data(city)   

def main():

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)    # the display_raw_data

        while True:
             restart = input('\nWould you like to restart? Enter yes or no.\n')
             if restart.lower() != 'yes':
                  break

if _name_ == "_main_":
    main()