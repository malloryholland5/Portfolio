"""
Check the Weather
"""

import requests


def zip_code_function():
    # request location with zip code
    zip_code = input('What is your zip code: ')
    # look up city information with zip code
    zip_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid=340bda0c87bc556c2ccd107f1ab40b7a'
    # get city information from openweather
    zip_url = requests.request('GET', zip_url)
    # put information in json format
    data = zip_url.json()
    # get latitude and longitude from city information
    latitude = data['lat']
    longitude = data['lon']
    # get weather from latitude and longitude
    weather(latitude, longitude)


def city_function():
    # request location with city and state
    city_name = input('What city would you like to look up?: ')
    state = input('What state is the city located in? ')
    city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state},US&appid=340bda0c87bc556c2ccd107f1ab40b7a'
    # get city information from openweather
    city_url = requests.request('GET', city_url)
    # load information into a json format
    data = city_url.json()
    # get latitude and longitude from nested dic to get city information
    latitude = set(city.get('lat') for city in data).pop()
    longitude = set(city.get('lon') for city in data).pop()
    # get weather from latitude and longitude
    weather(latitude, longitude)


def weather(latitude, longitude):
    # pull the temp units into the function
    units = temp_units()
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=340bda0c87bc556c2ccd107f1ab40b7a&units={units}'
    # get weather
    lat_lon_url = requests.request('GET', url)
    # load information into a json format
    lat_lon_data = lat_lon_url.json()
    # print format
    pretty_print(lat_lon_data, units)


def temp_units():
    while True:
        # Ask user what unit of measure they would like to receive the temp weather
        units = input('What unit of measurement would you like to view the temperature?\n "F" for Fahrenheit or "C" for Celsius\n Preferred Temp: ').upper()
        try:
            if units == "F":
                return 'imperial'
            elif units == "C":
                return 'metric'
            else:
                print('\nPlease enter "F" or "C"\n')
        except KeyboardInterrupt:
            print('\n The program has been stopped. Thank you for your for using OpenWeather.')
        except Exception as e:
            # print reason for error
            print('Error:', e)


def pretty_print(lat_lon_data, units):
    # put unit measurement letter after temp weather
    if units == 'imperial':
        f_c_unit = 'F'
    else:
        f_c_unit = 'C'
    # put degree symbol after temp weather
    degree = u'\xb0'
    try:
        # print the weather, round the result and format second column
        print('--------------------------------')
        print(f"\tWeather for {lat_lon_data['name']}")
        print(f"{'Description:':25s}{lat_lon_data['weather'][0]['description']}")
        print(f"{'Temperature:':25s}{round(lat_lon_data['main']['temp'])}{degree}{f_c_unit}")
        print(f"{'Feels like:':25s}{round(lat_lon_data['main']['feels_like'])}{degree}{f_c_unit}")
        print(f"{'High:':25s}{round(lat_lon_data['main']['temp_max'])}{degree}{f_c_unit}")
        print(f"{'Low:':25s}{round(lat_lon_data['main']['temp_min'])}{degree}{f_c_unit}")
        print(f"{'Pressure:':25s}{round(lat_lon_data['main']['pressure'])}")
        print(f"{'Humidity:':25s}{round(lat_lon_data['main']['humidity'])}%")
        print('--------------------------------')
    except KeyboardInterrupt:
        print('\n The program has been stopped. Thank you for your for using OpenWeather.')
    except Exception as e:
        # print reason for error
        print('Error:', e)
    if_more_weather()


def if_more_weather():
    while True:
        another_location = input('Would you like to look up weather for another city? Enter "yes" or "no"\n Answer: ').lower()
        try:
            # find location from user input answer in lower case, if answer does not meet requirement loop back around
            if another_location == 'yes'.lower():
                more_weather()
            elif another_location == 'no'.lower():
                print('Thank you for using OpenWeather, Goodbye.')
                exit()
            else:
                print('\nPlease ONLY enter "yes" or "no" \n')
        except KeyboardInterrupt:
            print('\n The program has been stopped. Thank you for your for using OpenWeather.')
        except Exception as e:
            # Any other error
            print('Error:', e)


def more_weather():
    while True:
        zip_city = input('Would you like to enter your "zip", "city" or "no" to end the program?').lower()
        try:
            # find location from user input answer in lower case, if answer does not meet requirement loop back around
            if zip_city == 'zip'.lower():
                zip_code_function()
            elif zip_city == 'city'.lower():
                city_function()
            elif zip_city == 'no'.lower():
                print('Thank you for your time.')
                break
            else:
                print('\nPlease enter "city", "zip" or "no".\n')
        except KeyError:
            # print reason for error
            print('\nEither the zip, city or state is incorrect. Please enter accurate information.\n')
        except KeyboardInterrupt:
            print('\n The program has been stopped. Thank you for your for using OpenWeather.')
        except Exception as e:
            # Any other error
            print('Error:', e)


def main():
    # Ask how they want to look up the location
    print('Welcome to OpenWeather: ')

    while True:
        # ask for user input
        zip_city = input('Would you like to enter your "zip", "city" or "no" to end the program?').lower()
        try:
            # find location from user input answer in lower case, if answer does not meet requirement loop back around
            if zip_city == 'zip'.lower():
                zip_code_function()
            elif zip_city == 'city'.lower():
                city_function()
            elif zip_city == 'no'.lower():
                print('Thank you for your time.')
                break
            else:
                print('\nPlease enter "city", "zip" or "no".\n')
        except KeyError:
            # print reason for error
            print('\nEither the zip, city or state is incorrect. Please enter accurate information.\n')
        except KeyboardInterrupt:
            print('\n The program has been stopped. Thank you for your for using OpenWeather.')
        except Exception as e:
            # Any other error
            print('Error:', e)


if __name__ == '__main__':
    main()
