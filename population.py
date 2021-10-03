def calc(start_size, end_size, years = 0):
    while start_size < end_size:
        start_size = (start_size + (start_size//3) - (start_size//4))
        years += 1
        continue
    return years
while True:

    start_size = int(input("Start size: "))
    end_size =int(input("End size: "))

    if (start_size < 9) or (end_size < start_size):
        continue
    
    else:
        print("Years: {}".format(calc(start_size, end_size)))
        break
    