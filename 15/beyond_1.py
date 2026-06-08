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
            
        if city_name in rainfall:
            rainfall[city_name]['total'] +=  rain_amount
            rainfall[city_name]['days'] += 1
        else:
            rainfall[city_name] = {"total": 0, "days": 1}

                
        
    for city,data in rainfall.items():
        total = data["total"]
        days = data["days"]
        avg = total/days
        print(f'The average rain for {city}: {avg} in {days} days')

get_rainfall()
        
        