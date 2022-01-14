import random
from replit import clear
from art import logo
print('Welcome to Black-Jack game')
ask=input('Do you want to play the game (y/n) :')
def game_play():
    print(logo)
    list=[0,2,3,4,5,6,7,8,9,10,11]
    your_cards=[]
    computer_cards=[]
    for _ in range(2):
        your_cards.append(list[random.randint(0,10)])
        computer_cards.append(list[random.randint(0,10)])
    YSum=0
    CSum=0
    for _ in your_cards:
        YSum+=_
        
    for _ in computer_cards:
        CSum+=_ 
    if CSum==YSum==21:
        return print(f'Your cards are {your_cards},Your score is {YSum}'f'\nComputers cards are {computer_cards},Computer score is {CSum}''\nThis situation is unexpected''\nBlack-Jack for both of you'"\nHence we declare it as 'TIE'")
    elif YSum==21:
        return   print('Black Jack' f'\nYour cards are {your_cards},Your score is {YSum}''\n you won😇') 
    elif CSum==21:
        return  print('Black Jack'f'\ncomputer cards are {computer_cards}''\nYou lost😭')
    print(f'Your cards are {your_cards},Your score is {YSum}')
    print(f'Computers 1st card is {computer_cards[0]}')
    def decision():
        if YSum>21:
            print(f'Your cards are {your_cards},Your score is {YSum}')
            print('Your sum exceeds 21😢''\nYou Lost😭')
        elif CSum==YSum:
            print(f'Your cards are {your_cards},Your score is {YSum}')
            print(f'Computers cards are {computer_cards},Computer score is {CSum}')
            print('TIE🙅‍')
        elif CSum>YSum and CSum<22:
            print(f'Your cards are {your_cards},Your score is {YSum}')
            print(f'Computers cards are {computer_cards},Computer score is {CSum}')
            print('You Lost😱')
        else:
            print(f'Your cards are {your_cards},Your score is {YSum}')
            print(f'Computers cards are {computer_cards},Computer score is {CSum}')
            print('You Win😀')
    loop=True
    while loop==True:
        do_continue=input("Type 'y' to take one more card or 'n' to pass  :")
        if do_continue=='y':
            your_cards.append(list[random.randint(0,10)])
            YSum+=your_cards[-1]
            print(f'Your cards are {your_cards},Your score is {YSum}')
            print(f'Computers 1st card is {computer_cards[0]}')
        else:
            loop=False
            while CSum<17:
                computer_cards.append(list[random.randint(0,10)])
                CSum+=computer_cards[-1]
            decision()
if ask=='y':
    game_play()
    phir_se=True    
    while phir_se:    
        again=input('Do you want to play again (y/n) :')
        if again=='n':
            phir_se=False
            print("Hope, you enjoyed.We will meet again through this game")
        else:
            clear()
            game_play()
else:
    print("Its sad that you are leaving the game before even starting")

         



       
               
                 
                
            
            
           
    

