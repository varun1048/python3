import os    
import players
def test():
    os.system('cls')
    coin_or_coins = []
    naming = []

    for player in  players.varun['position']:
        print(player)

    def fun(position) -> bool:
        result = False
        for coin in coin_or_coins:
            if (position["direction"] == coin['direction']) and (position["x"] == coin['x']) and  (position["y"] == coin['y']):
                result = True
                break
        
        return result

    print()
    for position in  players.varun['position']:
        if players.varun['position'].index(position) == 0:
            coin_or_coins.append(position)

        if  fun(position):
            naming.append({'names':position['name']})
        else:
            coin_or_coins.append(position)



    for player in  coin_or_coins:
        print(player)

    print()
    print(naming)



