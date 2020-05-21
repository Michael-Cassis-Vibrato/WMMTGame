import time
import random
import datetime
import sys
#commit test version 2

def endmode():
    print()
    print('Thanks for playing Wangan!')
    print()
    print('Created by AkumaInc')
    sys.exit()

def restart():
    playagain = 0
    while playagain < 1:
        print('Do you want to race again or exit?')
        print('1 for C1outwards')
        print('2 for C1inwards')
        print('3 for Wangan Eastbound')
        print('N to end the game')
        time.sleep(1)
        playagain = input('Play again? Select 1, 2, 3 or N: ')
        if playagain == '1':
            print()
            C1outcourse()
        elif playagain == '2':
            print()
            C1incourse()
        elif playagain == '3':
            print()
            wanganeast()
        elif playagain == 'N':
            endmode()
        else: 
            playagain = 0

def carattr():
    global caraccl
    global cartop
    global carhand
    print('Your new car statistics are as follows')
    print('Acceleration ' + str(int(caraccl)))
    print('Top Speed ' + str(int(cartop)))
    print('Handling ' + str(int(carhand)))
    print()
    restart()

def carupgrademode():
    global caraccl
    global carhand
    global cartop
    carupgrade = 0
    while carupgrade < 1:
        print("Now we've completed your race, it's time to upgrade!")
        print("Which stat would you like to upgrade from?")
        print('Acceleration - Option 1')
        print('Top Speed - Option 2')
        print('Handling - Option 3')
        print('Change nothing - option 4')
        carmodup = input("What option will you upgrade??:")
        if carmodup == '1':
            caraccl += 10
            carupgrade = 1
        elif carmodup == '2':
            cartop += 10
            carupgrade = 1
        elif carmodup == '3':
            carhand += 10
            carupgrade = 1
        elif carmodup == '4':
            carupgrade = 1
        else:
            print('That is not a valid option, please try again')
            carupgrade = 0
        print()
    carattr()

def C1outcourse():
    global courselength
    courselength = 10000
    racechoiceC1out = 0
    while racechoiceC1out <1:
            print("Lets do this, C1 outwards! GO!")
            print()
            trafficsim()
            racechoiceq = 0
            while racechoiceq < 1:
                print('Would you like to race C1 outwards again?')
                racechoiceinput = str(input('Y / N: '))
                if racechoiceinput == "Y":
                    racechoiceC1out - 1
                    racechoiceq = 1
                    print()
                    #break
                elif racechoiceinput == "N":
                    racechoiceC1out = 1
                    racechoiceq = 1
                    carupgrademode()
                    print()
                    #break
                else:
                    print('Invalid choice, please try again')
                    racechoiceq = 0
                    print()

def C1incourse():
    global courselength
    racechoiceC1out = 0
    courselength = 11000
    while racechoiceC1out <1:
            print("Alright, let's do the C1 inwards course!")
            print()
            trafficsim()
            racechoiceq = 0
            while racechoiceq < 1:
                print('Would you like to race C1 inwards again?')
                racechoiceinput = str(input('Y / N: '))
                if racechoiceinput == "Y":
                    racechoiceC1out - 1
                    racechoiceq = 1
                    print()
                    #break
                elif racechoiceinput == "N":
                    racechoiceC1out = 1
                    racechoiceq = 1
                    carupgrademode()
                    print()
                    #break
                else:
                    print('Invalid choice, please try again')
                    racechoiceq = 0
                    print()

def wanganeast():
    global courselength
    racechoice = 0
    courselength = 15000
    while racechoice <1:
            print("Wangan Eastbound, race to 300kmph!")
            print()
            trafficsim()
            print()
            racechoiceq = 0
            while racechoiceq < 1:
                print('Would you like to race Wangan East again?')
                racechoiceinput = str(input('Y / N: '))
                if racechoiceinput == "Y":
                    racechoice - 1
                    racechoiceq = 1
                    print()
                    #break
                elif racechoiceinput == "N":
                    racechoice = 1
                    racechoiceq = 1
                    carupgrademode()
                    print()
                    #break
                else:
                    print('Invalid choice, please try again')
                    racechoiceq = 0
                    print()

def trafficsim():
    global caraccl
    global cartop
    global carhand
    traffic = random.randint(1,20)
    time.sleep(1)
    if traffic <= 8:
        print("Nani?! Traffic!!!")
    elif traffic <=16:
        print('There is some traffic about...')
    elif traffic <=21:
        print('No traffic! No worry!!')
    cartopadj = (cartop + traffic)
    caraccladj = (caraccl + traffic)
    carhandadj = (carhand +traffic)
    carmod = cartopadj + carhandadj + caraccladj
    time.sleep(1)
    for carloop in range (1):
        dots = 0
        while dots < 40:
            dots = dots + 1
            time.sleep(.1)
            dot = "." * dots
            dot2 = "." * (40 - dots)
            print(dot + '\ō͡≡o˞̶' + dot2 + "|GOAL|")
            
    timetrial = (courselength/carmod*(25))/3.6
    timeconv = (str(datetime.timedelta(seconds=timetrial)))
    print('It took you ' + timeconv + ' to complete this course!')
    time.sleep(1)
    print()
 


#story start
print('Welcome to the world of Wangan')
print('Where dreams begin and end in the road to the fastest in Japan.')
print('Choose your destiny:')
time.sleep(.1)
print('The Subaru WRX GC8 STI')
time.sleep(.1)
print('The Nissan Skyline GTR34')
time.sleep(.1)
print('The Mistubishi Evoluation 9MR')
time.sleep(.1)
print('and the Toyota AE86 Trueno')
time.sleep(.2)
print()

courselength = 0
carchoice = 0
caraccl = 0
cartop = 0
carhand = 0
while carchoice >= 0:
    print('Which of these do you choose for your destiny?')
    print()
    print('1 for Subaru WRX STi GC8')
    print('2 for Nissan Skyline GTR34')
    print('3 for Mistubishi Lancer Evolution 9MR') 
    print('4 for Toyota Trueno AE86')
    myCarChoice = input("Please choose from the above cars: ")
    print() 
    if myCarChoice == '1':
        print('Ahh you choose the GC8, rumble boy!')  
        carname = "Subaru WRX STi GC8"
        caraccl = 90
        cartop = 80
        carhand = 100
        break
    elif myCarChoice == '2':
        print('The Skyline.... The Beast')
        carname = "Nissan Skyline GTR34"
        caraccl = 100
        cartop = 100
        carhand = 70
        break
    elif myCarChoice == '3':
        print('The Evolution is a great choice') 
        carname = "Mistubishi Evolution 9MR" 
        caraccl = 100
        cartop = 80
        carhand = 90
        break
    elif myCarChoice == '4':
        print('The legend itself, I see the drifter in you')
        carname = "Toyota Trueno AE86"
        caraccl = 80
        cartop = 80
        carhand = 100
        break
    else:
        print('Invalid choice, please try again')
        carchoice = carchoice + 1
        print()
print()
time.sleep(.5)        
print('Okay, and what is the name you wish to race under?')
Racername = input("Please enter your name: ")
print()
time.sleep(.1)
print('Alright ' + Racername + ' lets do this!')
time.sleep(.1)
print()
print('The ' + carname + ' has the following stats')
time.sleep(.1)
print('Accerlation = ' + str(int(caraccl)) + ' out of 100')
time.sleep(.1)
print('Top Speed = '+ str(int(cartop)) + ' out of 100')
time.sleep(.1)
print('Handling = '+ str(int(carhand)) + ' out of 100')
time.sleep(.5)
print()
print('Let us begin our journey')
time.sleep(.5)
print("I know, let's test your car out and go to C1 outwards!")
time.sleep(.5)
print()
C1outcourse()




    