
#list with months
monthList = ['January','February','March','April','May','June','July',
          'August','September','October','November','December']

x = True

while x == True:            # testing 
    try:
        for x in range(1,12):       #specifiek range
            monthNum = int(input("Please enter a number of a month: "))-1
            print(monthList[monthNum])
            
    #Handling a specifiek error/ when the input is out of the range specified
    except IndexError:
        monthNum = int(input("Please enter a number between 1 and 12: "))-1
        print(monthList[monthNum])
        
    #hadling multiple errors/ when input is out of the range specified and when the data type is wrong
    except (IndexError,ValueError):
        monthNum = int(input("Please only enter numbers between 1 and 12: "))-1
        print(monthList[monthNum])
        


    
    

