#Request input (h)armonic, (m)ultiplication or (q)uit
    #if (q)
        #Quit
    #elif (h)
        #print first n numbers in Harmonc Series
        #One result per line
        #sum at bottom (edit)
        #All numbers rounded with 4 extra digits
    #elif (m)
        #print ancient egyption multiplication
        #print every step along the way
    #else
        #print ("Illegal Choice")

choice_str = input("(h)armonic, (m)ultiplication or (q)uit: ")

harmonic_base = 1
harmonic_sum = 1
denominator = 1
egyptian_sum = 0


while choice_str == "m" or choice_str == "h" or choice_str == "q":
    if choice_str == "q":
        break
    elif choice_str == "h":
        length_int = int(input("Series length: "))
        print(float(harmonic_base))
        for number in range(1,length_int):
            denominator += 1
            harmonic = float((harmonic_base/denominator))
            harmonic = round(harmonic,4)
            harmonic_sum += harmonic
            print(harmonic)
        print("Sum of series:", harmonic_sum)
    elif choice_str == "m":
        first_int = int(input("First integer: "))
        second_int = int(input("Second integer: "))
        if second_int % 2 == 0:
            continue
        else: 
            egyptian_sum += first_int
        print(first_int, second_int)
        while second_int > 1:
            first_int = (first_int *2)
            second_int = (second_int//2)
            print(first_int,second_int)
            if second_int % 2 == 0:
                continue
            else:
                egyptian_sum += first_int
        print("Product:",egyptian_sum)
    egyptian_sum = 0
    choice_str = input("(h)armonic, (m)ultiplication or (q)uit: ")




