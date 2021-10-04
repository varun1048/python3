from ludo_layout import Lodu
import playes
def main():
    ludo = Lodu(playes.varun)
    # print(ludo.player_points())
    ludo.logic()

if __name__ == '__main__':
    import os
    os.system('cls')
    main()
    print()