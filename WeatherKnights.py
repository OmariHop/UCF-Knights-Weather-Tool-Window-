

import requests 
from tkinter import *
import math 
from PIL import ImageTk, Image 
import tweepy 

city_name = "   Alafaya,US "
api_key = "xxx"
icon = "aa89cd043b72209dd43c108c1d66afff.png"
choice = ""

# function that authenticates the OpenWeather API using my personal key and uses the city of Alafaya as parameter to grab its weather stats
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()
    
    # Grabs the temperture, feels like, and humidity values from the request list and stores them inton their respective variables 

    temp = response["main"]["temp"]
    
    # Changes temp from Kelvins to Farrinheit 
    temp = math.floor((temp * 1.8) - 459.67)

    feelsLike = response["main"]["feels_like"]
    feelsLike = math.floor((feelsLike * 1.8) - 459.67)
    
    humidity = response["main"]["humidity"]


    return {
        'temp': temp,
        'feelsLike' : feelsLike,
        'humidity' : humidity
    }

# Calls the function get_Weather by using the our API Key and the name of the city we typed and returns respective values 
finalWeather = get_weather(api_key, city_name)  


# Creates Tab that pops up when ran with specificed dimensions 
root = Tk()
root.geometry("300x300")
# Prints out the name of city_name while disregarding the country 
root.title(f'{city_name[:-3]} Weather')


def display_cityName(city):
    cityLabel = Label(root, text=f"University of Central Florida")
    cityLabel.config(font = ("Helvetica", 14))
    cityLabel.pack(side = 'top')

# function created to display the temperature, feels like temp, and humidity on the serperate window
def displayStats(finalWeather):
    temp = Label(root, text=f" The temperature is {finalWeather['temp']} F at UCF. Go Knights!")
    feelsLike = Label(root, text=f" It feels like {finalWeather['feelsLike']} F")
    humidity = Label(root, text=f" The humidity is {finalWeather['humidity']} %")

    temp.config(font = ("Helvetica", 11))
    feelsLike.config(font = ("Helvetica", 10))
    humidity.config(font = ("Helvetica", 9))

    temp.pack(side = 'top')
    feelsLike.pack(side = 'top')
    humidity.pack(side = 'top')


# Was intended to place a png of the ucf icon on tkinter window but could not get it to show 
def displayIcons(picture):
    img = ImageTk.PhotoImage(Image.open(icon))

    logo = Label(root, text = img)
    logo.pack(side = 'top')
    


# Gives user option to  decide whether or not they want the weather stats at ucf to be displayed, if they enter exit the window closes
while choice != "exit":    
    choice = input("Do you want to display the weather at the UCF? If so press any key, if you would like to leave enter exit ")
    choice = choice.lower()
    if choice == "exit":
        print("Ok, thank you for your time")
    else:
        display_cityName(city_name)
        displayStats(finalWeather)
        mainloop()
        print("The weather has been displayed!")




