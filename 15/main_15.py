def get_rainfall():
    rainfall = {}
    
    while True:
        city_name = input('Enter city name:')
        
        if not city_name:
            break
        try:
            rain_amount = int(input('Enter the amount of rain:'))
        except ValueError:
            print('you did not enter valid integer') 
            continue
            
        rainfall[city_name] = rainfall.get(city_name,0) + rain_amount
        
        for city,rain in rainfall.items():
            print(f'{city}:{rain}')

get_rainfall()
        
        