from imports import *
from win import win
def weather_start(parent):
    import requests
    import time
    from tkinter import messagebox

    win = parent

    font = ('e-Ukraine', 18)
    button_color = '#2147cf'
    button_hover_color = '#0228b0'

    first_url = 'https://api.openweathermap.org/data/2.5/weather?'
    api = '4e2f3528fc6c938da62852ed3cd5a5aa'
    city = 'Ternopil'

    url = first_url + "appid=" + api + '&q=' + city

    server_resp = requests.get(url).json()


    def change_city():
        nonlocal server_resp, city, temp_kelvin
        try:
            info = city_entr.get()

            city = info

            url = first_url + "appid=" + api + '&q=' + city

            server_resp = requests.get(url).json()

            temp_kelvin = server_resp['main']['temp']

        except Exception:
            messagebox.showerror('ERROR!','НЕМАЄ ІНФОРМАЦІЇ ПО ВВЕДЕНИХ ДАНИХ!')
            city = 'Ternopil'
        redownload_func()

    def redownload_func():
        nonlocal temp_kelvin, temp_celsius, temp_fahrenheit, min_temp_kelvin, min_temp_celsius, min_temp_fahrenheit
        nonlocal max_temp_kelvin, max_temp_celsius, max_temp_fahrenheit, description, humidity, wind_speed
        nonlocal  sunrise_time, sunset_time, sunrise_time_seconds, sunset_time_seconds, local_time_seconds, local_time
        url = first_url + "appid=" + api + '&q=' + city

        server_resp = requests.get(url).json()


        city_label.configure(text=city)
        temp_kelvin = server_resp['main']['temp']
        temp_celsius, temp_fahrenheit = from_kelvin(temp_kelvin)

        min_temp_kelvin = server_resp['main']['temp_min']
        min_temp_celsius, min_temp_fahrenheit = from_kelvin(min_temp_kelvin)

        max_temp_kelvin = server_resp['main']['temp_max']
        max_temp_celsius, max_temp_fahrenheit = from_kelvin(max_temp_kelvin)

        description = server_resp['weather'][0]['description']

        humidity = server_resp['main']['humidity']

        wind_speed = server_resp['wind']['speed']

        sunrise_time = time.strftime('%H:%M:%S', time.gmtime(server_resp['sys']['sunrise'] + server_resp['timezone']))
        sunset_time = time.strftime('%H:%M:%S', time.gmtime(server_resp['sys']['sunset'] + server_resp['timezone']))

        descr(description)
        temp_c_l.configure(text=f'{temp_celsius}°C')
        temp_f_l.configure(text=f'{temp_fahrenheit}°F')
        temp_min_c_l.configure(text=f'{min_temp_celsius}°C')
        temp_min_f_l.configure(text=f'{min_temp_fahrenheit}°F')
        temp_max_c_l.configure(text=f'{max_temp_celsius}°C')
        temp_max_f_l.configure(text=f'{max_temp_fahrenheit}°F')
        humidity_n_l.configure(text=f'{humidity}%')
        wind_speed_l.configure(text=f'{wind_speed} м/с')
        sunrise_time_l.configure(text=f'Схід Сонця: {sunrise_time}')
        sunset_time_l.configure(text=f'Захід Сонця: {sunset_time}')
        local_time = time.strftime('%H:%M:%S', time.gmtime(server_resp['dt'] + server_resp['timezone']))

        sunrise_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], sunrise_time.split(":")))
        sunset_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], sunset_time.split(":")))
        local_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], local_time.split(":")))
        descr(description)


    def from_kelvin(kelvin):
        celsius = round(kelvin - 273.15, 2)
        fahrenheit = round(celsius * (9/5) + 32, 2)
        return celsius, fahrenheit

    def descr(description):
        for i in descriptions_list:
            if description == i:
                index = descriptions_list.index(i, 0, 9)
                if sunrise_time_seconds <= local_time_seconds < sunset_time_seconds:
                    ico.configure(image=day_images[index])
                else:
                    ico.configure(image=night_images[index])


    temp_kelvin = server_resp['main']['temp']
    temp_celsius, temp_fahrenheit = from_kelvin(temp_kelvin)

    min_temp_kelvin = server_resp['main']['temp_min']
    min_temp_celsius, min_temp_fahrenheit = from_kelvin(min_temp_kelvin)

    max_temp_kelvin = server_resp['main']['temp_max']
    max_temp_celsius, max_temp_fahrenheit = from_kelvin(max_temp_kelvin)


    description = server_resp['weather'][0]['description']

    humidity = server_resp['main']['humidity']

    wind_speed = server_resp['wind']['speed']

    sunrise_time = time.strftime('%H:%M:%S', time.gmtime(server_resp['sys']['sunrise'] + server_resp['timezone']))
    sunset_time = time.strftime('%H:%M:%S', time.gmtime(server_resp['sys']['sunset'] + server_resp['timezone']))
    local_time = time.strftime('%H:%M:%S', time.gmtime(server_resp['dt'] + server_resp['timezone']))

    sunrise_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], sunrise_time.split(":")))
    sunset_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], sunset_time.split(":")))
    local_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], local_time.split(":")))

    '''sunrise_time = dt.datetime.utcfromtimestamp(server_resp['sys']['sunrise'] + server_resp['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(server_resp['sys']['sunset'] + server_resp['timezone'])'''


    night_images = []
    day_images = []


    clear_sky_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\clear_sky_n.png'), size=(100, 100))
    few_clouds_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\few_clouds_n.png'), size=(100, 100))
    overcast_clouds_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\scattered_clouds.png'), size=(100, 100))
    broken_clouds_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\broken_clouds.png'), size=(100, 100))
    shower_rain_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\shower_rain.png'), size=(100, 100))
    rain_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\rain_n.png'), size=(100, 100))
    thunderstorm_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\thunderstorm.png'), size=(100, 100))
    snow_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\snow.png'), size=(100, 100))
    mist_n = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\night\\mist.png'), size=(100, 100))


    night_images.append(clear_sky_n)
    night_images.append(few_clouds_n)
    night_images.append(overcast_clouds_n)
    night_images.append(broken_clouds_n)
    night_images.append(shower_rain_n)
    night_images.append(rain_n)
    night_images.append(thunderstorm_n)
    night_images.append(snow_n)
    night_images.append(mist_n)


    clear_sky_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\clear_sky_d.png'), size=(100, 100))
    few_clouds_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\few_clouds_d.png'), size=(100, 100))
    overcast_clouds_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\scattered_clouds.png'), size=(100, 100))
    broken_clouds_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\broken_clouds.png'), size=(100, 100))
    shower_rain_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\shower_rain.png'), size=(100, 100))
    rain_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\rain_d.png'), size=(100, 100))
    thunderstorm_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\thunderstorm.png'), size=(100, 100))
    snow_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\snow.png'), size=(100, 100))
    mist_d = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\weather\\day\\mist.png'), size=(100, 100))

    day_images.append(clear_sky_d)
    day_images.append(few_clouds_d)
    day_images.append(overcast_clouds_d)
    day_images.append(broken_clouds_d)
    day_images.append(shower_rain_d)
    day_images.append(rain_d)
    day_images.append(thunderstorm_d)
    day_images.append(snow_d)
    day_images.append(mist_d)

    redownload = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\redownload.png'), size=(30, 30))

    descriptions_list = ['clear sky', 'few clouds', 'overcast clouds', 'broken clouds',
                         'shower rain', 'rain', 'thunderstorm', 'snow', 'mist']



    city_entr = CTkEntry(win, placeholder_text='Введіть місто англійською...', font=('e-Ukraine',16), text_color='#000000',
                         width=300, height=50, fg_color='#d9d9d9', corner_radius=33)
    city_entr.place(x=240, y=26)

    city_button = CTkButton(win, text='Пошук', font=('e-Ukraine', 13), text_color='white', corner_radius=33,
                            width=100, height=50, fg_color=button_color, hover_color=button_hover_color, command=change_city)
    city_button.place(x=566, y=26)

    redownload_button = CTkButton(win, text='', fg_color='#76C95A', width=50, height=50, command=redownload_func, image=redownload, corner_radius=33)
    redownload_button.place(x=130, y=26)

    city_label = CTkLabel(win, text=city, font=('Jomhuria', 96), width=300, height=65, anchor='w')
    city_label.place(x=125, y=111)

    ico = CTkLabel(win, text='', image=broken_clouds_d, width=100, height=100)
    ico.place(x=125, y=240)



    temp_l = CTkLabel(win ,text='Температура:', font=font, text_color='white',width=145, height=30, anchor='w')
    temp_l.place(x=125, y=354)

    temp_c_l = CTkLabel(win, text=f'{temp_celsius}°C', font=font, text_color='white',width=55, height=30, anchor='w')
    temp_c_l.place(x=125, y=396)

    temp_f_l = CTkLabel(win, text=f'{temp_fahrenheit}°F', font=font, text_color='white',width=55, height=30, anchor='w')
    temp_f_l.place(x=125, y=438)


    temp_min_l = CTkLabel(win, text=f'Мінімальна:', font=font, text_color='white',width=130, height=30, anchor='w')
    temp_min_l.place(x=329, y=354)

    temp_min_c_l = CTkLabel(win, text=f'{min_temp_celsius}°C', font=font, text_color='white',width=55, height=30, anchor='w')
    temp_min_c_l.place(x=329, y=396)

    temp_min_f_l = CTkLabel(win, text=f'{min_temp_fahrenheit}°F', font=font, text_color='white',width=55, height=30, anchor='w')
    temp_min_f_l.place(x=329, y=438)

    temp_max_l = CTkLabel(win, text=f'Максимальна:', font=font, text_color='white',width=150, height=30, anchor='w')
    temp_max_l.place(x=518, y=356)

    temp_max_c_l = CTkLabel(win, text=f'{max_temp_celsius}°C', font=font, text_color='white',width=55, height=30, anchor='w')
    temp_max_c_l.place(x=518, y=398)

    temp_max_f_l = CTkLabel(win, text=f'{max_temp_fahrenheit}°F', font=font, text_color='white',width=55, height=30, anchor='w')
    temp_max_f_l.place(x=518, y=438)


    wind_l = CTkLabel(win, text='Швидкість вітру:', font=font, text_color='white', width=180, height=30, anchor='w')
    wind_l.place(x=125, y=522)

    wind_speed_l = CTkLabel(win, text=f'{wind_speed} м/с', font=font, text_color='white', width=70, height=30, anchor='w')
    wind_speed_l.place(x=125, y=564)

    humidity_l = CTkLabel(win, text=f'Вологість', font=font, text_color='white',width=110, height=30, anchor='w')
    humidity_l.place(x=329, y=522)

    humidity_n_l = CTkLabel(win, text=f'{humidity}%', font=font, text_color='white',width=45, height=30, anchor='w')
    humidity_n_l.place(x=329, y=564)

    sunrise_time_l = CTkLabel(win, text=f'Схід Сонця: {sunrise_time}', font=font, text_color='white',width=250, height=30, anchor='w')
    sunrise_time_l.place(x=518, y=522)

    sunset_time_l = CTkLabel(win, text=f'Захід Сонця: {sunset_time}', font=font, text_color='white', width=250, height=30, anchor='w')
    sunset_time_l.place(x=518, y=564)

    descr(description)

    copyright = CTkLabel(win, text='by Dmytro', font=('Arial', 20, 'bold'), width=150, height=50, anchor='center')
    copyright.place(x=600, y=620)