from sendMail import send_email
from player import *
from player import *

def secret_draw(players):
    pickable = [x.playerName for x in players]
    for player in players:
        player.pick(pickable)
        print(player.getMessagePick())


def send_mail_to_all_players(players):
    title_message = "Check this mail to know your pick for Secret Hannouka!"
    for player in players:
        core_message = player.getMessagePick()
        player_mail = [player.getMail()]
        send_email(title_message, core_message, player_mail)












