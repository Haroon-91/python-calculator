running = True

while running:
    print("===Calculator===\n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divide")
    print("5.Measurements")
    print("6.Exit")

    option = float(input("Enter a number please: "))
    if option == 6969400:
         print("===Secret Dev Menu===")
         print("1.Easter egg")
         print("2.Help")
         print("3.Developer info")
         sec_dev_menu = float(input("Enter an option: "))
         option_chosen = float(input(f"Good you choosed {sec_dev_menu} Enter password to continue... "))
         password = 777000777
         if option == 12300:
              print("You have found a secret easter egg that does nothin ;-;")
         if option_chosen == password: 
              if sec_dev_menu == 1:
                   print("Every easter egg in calc: ")
                   input("Press enter to continue...")
                   print("press 12300 for a easter egg")
                   print("Sorry... work in progress")
         if option_chosen == 2:
              print("Sorry.. work in progress")  
         if option_chosen == 3:
              print("Made by Haroon Rubbani")
              print("Work in progress")
              print("It was built on Vs studio")
              print("It was made in November 2025")  
    if option == 1: 
        frst_number_add = float(input("Enter your first number for addition: "))
        scnd_number_add = float(input("Enter your second number: "))
        add = frst_number_add + scnd_number_add 
        print(add)
    if option == 2:
        sub_frst = float(input("Enter a number for subtraction: "))
        sub_sec = float(input("Enter a second nummber for subtraction: "))
        sub = sub_frst - sub_sec 
        print(sub)
    if option == 3:
        mul_frst = float(input("Enter a number for multiplication: "))
        mul_sec = float(input("Enter second number for multiplication: "))
        mul = mul_frst*mul_sec
        print(mul)
    if option == 4:
        div_frst = float(input("Enter a number for divide: "))
        div_sec = float(input("Enter second number for divide: "))
        div = div_frst/div_sec
        print(div)
    if option == 5:
        input("Press enter to continue...")
        print("\n1.Length")
        print("2.Mass")
        print("3.Time")
        print("4.Temprature")

        option2 = float(input("Choose an option: "))
        if option2 == 1:
            print("\n1km to meters")
            print("1m to centimeters")
            print("1cm to milli meter")
            print("1 inch to cm")
            print("1 foot to inch")
            print("1 yard to foot")
            print("1 mile to kilometers")

            options = float(input("Pick an option from 1 to 7: "))
            if options == 1:
                km_to_m = float(input("Enter the number kilometers to turn to meters: "))
                km_to_m_an = km_to_m * 1000
                print(km_to_m_an, "meters")
            if options == 2: 
                m_to_cm = float(input("Enter meters to convert to centimeters: "))
                m_to_cm_an = m_to_cm * 100
                print(m_to_cm_an, "centimeters")
            if options == 3: 
                cm_to_mm = float(input("Enter cm to convert to mm: "))
                cm_to_mm_an = cm_to_mm * 10
                print(cm_to_mm_an, "millimeters")
            if options == 4:
                inch_to_cm = float(input("Enter inch to convert to cm: "))
                inch_to_cm_an = inch_to_cm * 2.45
                print(inch_to_cm_an, "centimeters")
            if options == 5:
                ft_to_inc = float(input("Enter number val in foot to convert it to inches: "))
                ft_to_inc_an = ft_to_inc * 12
                print(ft_to_inc_an, "inches")
            if options == 6:
                yrd_to_ft = float(input("Enter yard to conver to foot: "))
                yrd_to_ft_an = yrd_to_ft * 3 
                print(yrd_to_ft_an, "feet")
            if options == 7:
                ml_to_km = float(input("Enter mile in numbers to convert to km: "))
                ml_to_km_an = ml_to_km * 1.609
                print(ml_to_km_an, "kilometers")
        if option2 == 2:
            print("kg to gram")
            print("gram to milligram")
            print("pound to kg")
            print("ounce to g")
            print("ton to kg")   
            optionz = float(input("Select a option from 1-5: "))
            if optionz == 1:
                    kg_to_grm = float(input("Enter kg to covnert to grams: "))
                    kg_to_grm_an = kg_to_grm*1000
                    print(kg_to_grm_an, "grams")
            if optionz == 2:
                    grm_to_mg = float(input("Enter value of gram to turn to mg: "))
                    grm_to_mg_an = grm_to_mg*1000
                    print(grm_to_mg_an, "milligrams")
            if optionz == 3:
                    pnd_to_kg = float(input("Enter pound to convert to kg: "))
                    pnd_to_kg_an = pnd_to_kg*0.4536
                    print(pnd_to_kg_an, "kilograms")
            if optionz == 4:
                    onc_t_g = float(input("Enter value in ounce to convert to grams: "))
                    onc_t_g_an = onc_t_g *28.35
                    print(onc_t_g_an, "grams")
            if optionz == 5:
                    tn_to_kg = float(input("Enter ton to convert to kg: "))
                    tn_to_kg_an = tn_to_kg*1000
                    print(tn_to_kg_an, "kilograms")
        if option2 == 3:
                    print("hour to minutes")
                    print("minute to seconds")
                    print("days to hours")
                    print("weeks to days")
                    print("year to days")
                    option_time = float(input("Enter a option from 1-5: "))  
                    if option_time == 1:
                        hr_t_m = float(input("Enter value in hour to turn to minutes: "))
                        hr_t_m_an = hr_t_m*60
                        print(hr_t_m_an, "minutes")
                    if option_time == 2:
                        m_t_s = float(input("Enter minutes to turn into seconds: "))
                        m_t_s_an = m_t_s * 60
                        print(m_t_s_an, "seconds")
                    if option_time == 3:
                        d_t_hr = float(input("Enter days to convert to hours: "))
                        d_t_hr_an = d_t_hr * 24
                        print(d_t_hr_an, "hours")
                    if option_time == 4:
                        w_t_d = float(input("Enter week to convert to days: "))
                        w_t_d_an = w_t_d*7
                        print(w_t_d_an, "days")
                    if option_time == 5:
                        y_t_d = float(input("Enter years to convert to days: "))
                        y_t_d_an = y_t_d * 365
                        print(y_t_d_an, "days")

        if option2 == 4:
                print("\n1.Celsius to Fahrenheit")
                print("2.Fahrenheit to Celsius")
                print("3.Celsius to Kelvin")
                print("4.Kelvin to Celsius")

                option_temp = float(input("Enter an option (1-4): "))

                if option_temp == 1:
                    c = float(input("Enter Celsius: "))
                    f = (c * 9/5) + 32
                    print(f, "°F")

                if option_temp == 2:
                    f = float(input("Enter Fahrenheit: "))
                    c = (f - 32) * 5/9
                    print(c, "°C")

                if option_temp == 3:
                    c = float(input("Enter Celsius: "))
                    k = c + 273.15
                    print(k, "Kelvin")

                if option_temp == 4:
                    k = float(input("Enter Kelvin: "))
                    c = k - 273.15
                    print(c, "°C")

    if option == 6:
        print("Exiting calculator... Goodbye!")
        running = False
