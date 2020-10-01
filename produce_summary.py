def melon_delivery_count(day_count,file):

    ''' Taking a day count and delivery file, get delivery report
    Reads the delivery file line by line, process each line and generates report'''

    print("Day", day_count)
    for line in file:
        line = line.rstrip()                #truncates the whitespaces
        words = line.split('|')             #split of string is at '|'

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))                              #string formatting
    file.close()

        
file1 = open("um-deliveries-20140519.txt")
file2 = open("um-deliveries-20140520.txt")
file3 = open("um-deliveries-20140521.txt")

melon_delivery_count(1,file1)                 # calling the function
melon_delivery_count(2,file2)
melon_delivery_count(3,file3)


