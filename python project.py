import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = [ 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'Saturday', 'all']

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
    city_name = " "
    while city_name.lower() not in CITY_DATA:
        city_name = input('We have 3 cities: Chicago, New york city or Washington, which data do you want to see?').lower()
        if city_name in CITY_DATA:
            city = city_name.lower()
            break
        else:
            print("Invalid input, please re-enter correct city name.")
    

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = " "
    while month_name.lower() not in MONTHS:
        month_name = input("We have data of january to june, How do you want to filter it? Type the month's name or all to apply no filter: ").lower()
        if month_name.lower() in MONTHS:
            month = month_name.lower()
            break
        else: 
            print("Invalid month name, please re-enter correct month name.")

    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = " "
    while day_name.lower() not in DAYS:
        day_name = input('What day of the week? ').lower()
        if day_name.lower() in DAYS:
            day = day_name.lower()
            break
        else:
            print("Invalid day name, please input correct value")


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
  
        
    df = pd.read_csv(CITY_DATA[city])
    
    # converting start time column to date time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extracting month and dow from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filtering by month
    if month != 'all' :
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    # filtering by day
    if day != 'all' :
        
        df = df.loc[df['day_of_week'] == day]
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('The most common month is:',common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of week is:', common_day)
    


    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    print('The most common hour is:',common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start station:', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Frequent End station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    
    df["Start - End"] = df["Start Station"] + " - " +df["End Station"]
    popular_st_en_station = df["Start - End"].mode()[0]
    print('Most Frequent combination of start and end station:', popular_st_en_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Average travel time is:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given fitered data is: \n" + str(user_types))

    # Only access Gender column in this case
    if 'Gender' in df :
    # TO DO: Display counts of genderuser_types = df['User Type'].value_counts()
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))
    else:
        print('Gender stats cannot be calculated because gender does not appear in the dataframe')

  
     
    if 'Birth Year' in df :
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given fitered data is:        {}\n'.format(earliest_birth))
        print('Most recent birth from the given fitered data is:     {}\n'.format(most_recent_birth))
        print('Most common birth from the given fitered data is: {}\n'.format(most_common_birth))
    else:
        print('Earliest birth, most recent birth and most common birth cannot be computed.')
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
