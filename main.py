from secretHanoukka import *
from importPlayersFromSpreadSheet import *


def main():

    #Create a list with all instances of a class
    #playerList = [x for x in gc.get_objects() if isinstance(x, Player)]

    #path_l = "/Users/samueltenoudji-cohen/Desktop/SecretHanoukka.xlsx"

    path_l = "SecretHanoukka.xlsx"

    #Extract data from file and creates player objects
    player_list = extract_data_using_openpyxl(path_l)

    #Run Secret draw for all players
    secret_draw(player_list)

    #Update file with last pick

    player_dictionnary = {}
    for player in player_list:
        player_dictionnary[player.playerName] = player

    update_lastpick_in_file(path_l, player_dictionnary)

    #Send mail to each player
    #send_mail_to_all_players(playerList)




main()

