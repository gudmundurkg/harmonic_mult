#Höfundur: Guðmundur Kristján

choice_str = input("(h)armonic, (m)ultiplication or (q)uit: ")

harmonic_base = 1
harmonic_sum = 1
denominator = 1
egyptian_sum = 0
 
while choice_str != "q":
    #Harmonic Series:
    if choice_str == "h":
        length_int = int(input("Series length: "))
        print(float(harmonic_base))
        for number in range(1,length_int):
            denominator += 1
            harmonic = float((harmonic_base/denominator))
            harmonic_sum += harmonic
            print(round(harmonic,4))
        print("Sum of series:", round(harmonic_sum,4))
    #Ancient Egyptian Multiplication
    elif choice_str == "m":
        first_int = int(input("First integer: "))
        second_int = int(input("Second integer: "))
        #Continue ef second_int er slétt tala
        if second_int % 2 == 0:
            None
        #Summu bætt við egyptian_sum ef second_int er oddatala
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
    else:
        print("Illegal choice!")
    #Gefum breytum upprunalegt gildi svo hægt sé að keyra kóða aftur
    egyptian_sum = 0
    harmonic_sum = 1
    denominator = 1
    
    choice_str = input("(h)armonic, (m)ultiplication or (q)uit: ")



