import statistics

with open("provpoäng.txt", "r") as file: # öppnar filen i read mode
    content = file.read() # läser filens information
    numbers = content.split() #delar upp informationen i en lista med nummer
    for number in numbers: # gå igenom innehållet i filen och printa varje siffra
        print(number)
    
    print("antal nummer i filen:",len(numbers))

 #konvertera allt i filen till int
    int_numbers = []
    for number in numbers:
        int_numbers.append(int(number))

    #beräkna medelvärdet
    medelvarde = sum(int_numbers) / len(int_numbers)

    #printa medelvärdet
    print("medelvärdet är:", medelvarde)

#beräknar medianet
    print(statistics.median(numbers))