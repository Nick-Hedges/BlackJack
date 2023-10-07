import random
import time
import os

bold_escape_code = "\x1B[1m"    
reset_escape_code = "\x1B[0m"

blackJackDeck = {
    "Ace Of Spades": [1, 11],
    "Two Of Spades": 2,
    "Three Of Spades": 3,
    "Four Of Spades": 4,
    "Five Of Spades": 5,
    "Six Of Spades": 6,
    "Seven Of Spades": 7,
    "Eight Of Spades": 8,
    "Nine Of Spades": 9,
    "Ten Of Spades": 10,
    "Jack Of Spades": 10,
    "Queen Of Spades": 10,
    "King Of Spades": 10,
    "Ace Of Hearts": [1, 11],
    "Two Of Hearts": 2,
    "Three Of Hearts": 3,
    "Four Of Hearts": 4,
    "Five Of Hearts": 5,
    "Six Of Hearts": 6,
    "Seven Of Hearts": 7,
    "Eight Of Hearts": 8,
    "Nine Of Hearts": 9,
    "Ten Of Hearts": 10,
    "Jack Of Hearts": 10,
    "Queen Of Hearts": 10,
    "King Of Hearts": 10,
    "Ace Of Diamonds": [1, 11],
    "Two Of Diamonds": 2,
    "Three Of Diamonds": 3,
    "Four Of Diamonds": 4,
    "Five Of Diamonds": 5,
    "Six Of Diamonds": 6,
    "Seven Of Diamonds": 7,
    "Eight Of Diamonds": 8,
    "Nine Of Diamonds": 9,
    "Ten Of Diamonds": 10,
    "Jack Of Diamonds": 10,
    "Queen Of Diamonds": 10,
    "King Of Diamonds": 10,
    "Ace Of Clubs": [1, 11],
    "Two Of Clubs": 2,
    "Three Of Clubs": 3,
    "Four Of Clubs": 4,
    "Five Of Clubs": 5,
    "Six Of Clubs": 6,
    "Seven Of Clubs": 7,
    "Eight Of Clubs": 8,
    "Nine Of Clubs": 9,
    "Ten Of Clubs": 10,
    "Jack Of Clubs": 10, 
    "Queen Of Clubs": 10,
    "King Of Clubs": 10
}

def blackJackMoves(totalSum, playerCards, dealerRandChoice, dealerChoice, faceDownCardVal, totalBet):
    totalBet = float(totalBet)
    
    randomHitCard = random.choice(list(blackJackDeck.keys()))
    randomHitCardVal = blackJackDeck[randomHitCard]

    playerMove = input("Do you want to hit, stay, or split?: ")

    randomDealerCardVal = None

    if playerMove == "hit":
        if isinstance(randomHitCardVal, list):  
            aceValue = chooseAceVal(randomHitCard)
            totalSum += aceValue
            time.sleep(.8)
            print(f"Hit Card: {randomHitCard} ({aceValue} or 11)")
            time.sleep(.8)
        else:
            totalSum += randomHitCardVal
            time.sleep(.8)
            print(f"Hit Card: {randomHitCard}")
            time.sleep(.8)
            print(f"Your Total Hand Value: {totalSum}")
                
            if totalSum > 21:
                print("Sorry! You busted!")
                time.sleep(2)
                os.system("cls")
                print(f"You lost ${totalBet}")
                return 0
                
            if totalSum == 21:
                print(f"You Won! {totalBet * float(1.5)} is returned")
                time.sleep(.5)
                return 0
            else:
                blackJackMoves(totalSum, playerCards, dealerRandChoice, dealerRandChoice, faceDownCardVal, totalBet)

    if playerMove == "stay":
        randomDealerCardChoice = random.choice(list(blackJackDeck.keys())) 
        randomDealerCard = blackJackDeck[randomDealerCardChoice]

        print(f"Dealers Face Down Card Was: {dealerRandChoice}")
        time.sleep(.8)
        
        randomDealerCardVal = randomDealerCard
        dealersTotalHandVal = 0

        while dealersTotalHandVal < 17:
            randomDealerCardChoice = random.choice(list(blackJackDeck.keys())) 
            card_value = blackJackDeck[randomDealerCardChoice]

            if isinstance(card_value, list):
                aceValue = chooseAceVal(randomDealerCardChoice)
                dealersTotalHandVal += aceValue
            else:
                dealersTotalHandVal += card_value

            print(f"Dealers Total {dealersTotalHandVal}")
            print(f"Dealers Cards: {randomDealerCardChoice}")
            time.sleep(0.8)
        
        print(f"Dealers Total Hand: {dealersTotalHandVal}")

        if dealersTotalHandVal > 21:
            print("Dealer Bust! You won!")
            print(f"You won {totalBet * 1.5}")

        if dealersTotalHandVal > totalSum and dealersTotalHandVal < 21 or dealersTotalHandVal == 21:
            print("Dealer Won!")
            time.sleep(.8)
            print(f"You lost ${totalBet}")

    if playerMove == "Split": 
        pass

    return totalSum, randomDealerCardVal, dealerChoice

def dealersDeal():
    dealerRandChoice = random.choice(list(blackJackDeck.keys()))
    dealerChoice = blackJackDeck[dealerRandChoice]

    dealerFaceDownCard = random.choice(list(blackJackDeck.keys()))
    faceDownCardVal = blackJackDeck[dealerFaceDownCard]

    print(f"{bold_escape_code}Dealers Card: {dealerRandChoice} {reset_escape_code}")
    time.sleep(0.8)
    print(f"{bold_escape_code}Face down Card (Dealer): 🃲 {reset_escape_code}")
    time.sleep(0.8)

    return dealerRandChoice, dealerChoice, faceDownCardVal

def chooseAceVal(randomChoice):
    aceCardVal = input("Choose Value 1 or 11 for Ace: ").lower()
    if aceCardVal == "1":
        return 1
    else:
        return 11

def playerDeal():
    randomChoice1 = random.choice(list(blackJackDeck.keys()))
    randomCard1 = blackJackDeck[randomChoice1]
    print(f"Your Cards Are: {bold_escape_code}{randomChoice1}{reset_escape_code}")
    time.sleep(0.8)

    randomChoice2 = random.choice(list(blackJackDeck.keys()))
    randomCard2 = blackJackDeck[randomChoice2]
    print(f"Your Cards Are: {bold_escape_code}{randomChoice2}{reset_escape_code}")
    time.sleep(0.8)

    randomChoiceVal1 = randomCard1
    randomChoiceVal2 = randomCard2

    if "Ace" in randomChoice1:
        randomChoiceVal1 = chooseAceVal(randomChoice1)

    if "Ace" in randomChoice2:
        randomChoiceVal2 = chooseAceVal(randomChoice2)

    totalSum = randomChoiceVal1 + randomChoiceVal2
    playerCards = [randomChoice1, randomChoice2]

    print("Cards value:", totalSum)

    return totalSum, playerCards

def main():
    bet = input("What is your total bet amount?: ")
    totalbet = float(bet)

    print(f"{bold_escape_code}You are betting ${bet} on this hand 💰{reset_escape_code}")
    time.sleep(0.8)

    totalSum, playerCards = playerDeal()
    time.sleep(0.8)
    dealerRandChoice, dealerChoice, faceDownCardVal = dealersDeal()
    time.sleep(0.8)
    totalSum = blackJackMoves(totalSum, playerCards, dealerRandChoice, dealerChoice, faceDownCardVal, totalbet)

main()




     






























    

