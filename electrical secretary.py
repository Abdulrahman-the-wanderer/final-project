needed_things = []
needed_things2 = []
needed_things3 = []
xaa = []
xeo = input("What can I help you with today?[school,trips,appointments]")
if xeo == "school" :
    needed_things.insert(0,input("What are the things that you need?"))
    needed_things2.insert(1,input("What is the second thing?"))
    needed_things3.insert(2,input("What is the third thing?"))
    xaa.append(needed_things)
    xaa.append(needed_things2)
    xaa.append(needed_things3)
    print(xaa)

    for xeo in needed_things :
        if xeo != "hhh":
            print(f"""you can buy [{needed_things[0]}] from these places:
              from amazon for 1.750kd
              from alipapa for 1.5kd
              from the mall for 2 kd""")

    for xem in needed_things2:
        if xem != "hhhh":
            print(f"""you can buy [{needed_things2[0]}] from:
              amazon for 3kd
              alipapa for 2.5kd
              the book shop for 4kd""")
    for xea in needed_things3:
        if xea != 'hhhh':
            print(f"""you can buy [{needed_things3[0]}] from:
              amazon for 5kd
              alipapa for 3.5kd
              the book shop for 4kd""")

things_for_theseatrip = ["swimming_clothes" , "sunscreen", "towel ", "friends"]
things_for_themountaintrip = ["warm_clothes", "first_aid_kit" , "backpack" , "friends"]
things_for_thedeserttrip = ["light_clothes" , "first_aid_kit" , "reuseable_water_bottle" , "friends"]
if xeo == "trips":
    type_of_the_trip = input("Where are you going to?[sea,mountain,desert]")
    if type_of_the_trip == "sea":
        print("""If your destination is the sea then you should prepare the following things:""")
        print(things_for_theseatrip)
        print(f"""you can buy these thing from:
          {things_for_theseatrip[0]}: from amazon for 6kd.
           {things_for_theseatrip[1]}: from pharmaciy for 3kd.
          {things_for_theseatrip[2]}: from the mall for 2kd 
          {things_for_theseatrip[3]}: well go find them!""")

    if type_of_the_trip == "mountain":
        print("""If your destination is the montain then you should prepare the following things:""")
        print(things_for_themountaintrip)
        print(f"""you can buy these thing from:
          {things_for_themountaintrip[0]}: from amazon for 9kd.
          {things_for_themountaintrip[1]}: from pharmacy for 4kd.
          {things_for_themountaintrip[2]}: from the mall for 6kd 
          {things_for_themountaintrip[3]}: well go find them!""")
    
    if type_of_the_trip == "desert":
        print("""If your destination is the desert then you should prepare the following things:""")
        print(things_for_thedeserttrip)
        print(f"""you can buy these thing from:
          {things_for_thedeserttrip[0]}: from amazon for 6kd.
          {things_for_thedeserttrip[1]}: from pharmaciy for 4kd.
          {things_for_thedeserttrip[2]}: from the mall for 3kd 
          {things_for_thedeserttrip[3]}: well go find them!""")
schedule = []
timing = []
if xeo == "appointments":
    schedule.insert(0,input("What is your first appointment?"))
    timing.insert(0,int(input("When will your first appointment start?")))
    schedule.insert(1,input("What is your second appointment?"))
    timing.insert(1,int(input("When will your second appointment start?")))
    schedule.insert(2,input("What is your third appointment?"))
    timing.insert(2,int(input("When will your third appointment start?")))
    schedule.insert(3,input("What is your last appointment?"))
    timing.insert(3,int(input("When will your last appointment start?")))
    print(f"""you have 4 appointments today:
      first appointment is {schedule[0]} at {timing[0]} o'clock
      second appointment is {schedule[1]} at {timing[1]} o'clock
      third appointment is {schedule[2]} at {timing[2]} o'clock
      last appointment is {schedule[3]} at {timing[3]} o'clock""")