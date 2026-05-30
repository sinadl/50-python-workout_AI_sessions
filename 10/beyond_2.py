def sum_numberic(*items):
    
    output = items[0]
    for item in items[1:]:
        try:
            output += int(item)
        except (TypeError,ValueError):
            print('non numeric value ')
            pass
        
    return output

#test case
print(sum_numberic(23,41,'a','10',32))