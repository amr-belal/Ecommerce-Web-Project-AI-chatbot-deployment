######################################################
############### FOR Testing Purpose ##################
######################################################



# import geocoder  
# import requests 
# import os
# from dotenv import load_dotenv
# load_dotenv()


# g = geocoder.ip('me')

# print(g.latlng)
# print(g.address)
# print(g.country)
# print(g.city) 

# latLangList = g.latlng

# lat = latLangList[0]

# long = latLangList[1]

# userCountry = g.country
# userCity = g.city
# userAddress = g.address
# # getting location from latitude and longitude and User data location
# print(f'latitude {lat} , longitude {long} , city {userCity} , country {userCountry} , address {userAddress}')


# # get Api Weather key 
# API_KEY = os.environ.get("WEATHER_API_KEY")

# # print(API_KEY)

# # url = f"http://api.openweathermap.org/data/2.5/weather?q={userCountry}&appid={API_KEY}&units=metric"


# # response= requests.get(url)
# # data = response.json()
# # print(data)
# # print(f"Weather: {data['weather'][0]['description']}")
# # print(f"Temperature: {data['main']['temp']}°C")


# def get_current_location():
#     latLangList = g.latlng

#     lat = latLangList[0]

#     long = latLangList[1]

#     userCountry = g.country
#     userCity = g.city
#     userAddress = g.address
#     return [lat , long , userCity , userCountry , userAddress]

# def get_current_weather(loc):
#     API_KEY = os.environ.get("WEATHER_API_KEY")
#     url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={loc}"
#     response= requests.get(url)
#     data = response.json()
#     return [data["current"]["temp_c"] , data["current"]["condition"]["text"]]

# userCityAPI = get_current_location()
# print(get_current_weather(userCityAPI[2]))


# import requests

# def get_weather(city):
#     api_key = os.environ.get("WEATHER_API_KEY_2")
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     res = requests.get(url).json()
#     return res['weather'][0]['description']

# print(get_weather(g.city))




######################################################
############### FOR Testing Purpose ##################
######################################################







# import yake 
# def yake_keywords(text , lang="en" , top_n=5):
#     kw_extractor = yake.KeywordExtractor(lang=lang , n=2 ,top = top_n)
    
#     keywords = kw_extractor.extract_keywords(text)
#     return [kw for kw,score in keywords]


# msg = "I want to learn Python for data science and machine learning."
# print(yake_keywords(msg))



# # from keybert import KeyBERT 

# # kw_model  = KeyBERT()

# # def extract_keywords(text, top_n=5):
# #     keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')
# #     return [kw for kw, score in keywords]

# # msg = "I want to learn Python for data science and machine learning."
# # print(extract_keywords(msg))


# #  it seems that the yake is similar to keybert in performance and  slightly better



import json

with open('FrontEnd_React\server\data.json') as f:
    data = json.load(f)

print(data["products"][0])

