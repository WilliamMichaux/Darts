# -*- coding: utf-8 -*-
##########################################
#########Module python fléchettes#########
##########################################

import pprint


def jeux01(nbr_player, elimination=False, begin_score=301):
    """Darts game with 01 Rules.

    Parameters
    ----------
    nbr_player : The number of player, must be in 1-8. (int)
    elimination : Define if you play in elimination mode or not (optional) (Bool)
    score : Must be 101, 201, 301, 401 or 501. (optional) (int)

    """

    game, players = create_dictionnary(nbr_player, begin_score)

    condition = True
    rounds = 0
    turn = 0
    while condition == True:
        print "\nC'est au tour de %s." % (players[rounds])
        class_player(game, rounds, players, turn)
        separated_throw = get_throw()
        pre_throw_score = game[players[rounds]]['score'] # Variable utilisée pour remettre le score comme si 0 est dépassé
        round_score = 0
        score = get_score(separated_throw)

        for element in score:
            if element >= 0 and element <= 60:
                if (game[players[rounds]]['score'] - element) > 0:
                    game[players[rounds]]['score'] -= element
                    if elimination == True:
                        for buddy in players:
                            if game[buddy]['score'] == game[players[rounds]]['score']:
                                decharge = game[players[rounds]]['score']
                                game[buddy]['score'] = begin_score
                                game[players[rounds]]['score'] = decharge
                    round_score += element
                elif game[players[rounds]]['score'] - element == 0:
                    print 'Le gagnant est %s' % players[rounds]
                    condition = False
                else:
                    print 'Score trop eleve'
                    for a_supprimer in score:
                        score.remove(a_supprimer)
                    game[players[rounds]]['score'] = pre_throw_score
        turn += 1
        game[players[rounds]]['last_score'] = round_score
        print 'Vous avez marque %d points\n' % round_score
        confirmation = raw_input("Tape \'Retour\' si tu t'es trompé.\n")
        if confirmation != 'retour' and confirmation != 'Retour':  # Permet au jour de se retracter si il a fait une erreur, c'est comme si le tour n'avait pas eu lieu
            if rounds == nbr_player - 1:
                rounds = 0
            else:
                rounds += 1
        else:
            game[players[rounds]]['score'] = pre_throw_score
def get_throw():
    """Get throw and return them separated in a list)"""

    throw = raw_input('\nEntrez vos lances : ')
    separated_throw = separate_throw(throw)
    for element in separated_throw:
        if element == '':
            separated_throw.remove(element)

    return separated_throw
def get_score(throws):
    """compute and return the score of the player

    Parameters
    ----------
    throws : a list of throws in the form mXX, m is the multiplicator (s, d or t) and XX is a number <20 and 25. (list)

    Return
    ------
    if you are playing X01 game, it is the 3 score that the player made. (list of int)

    """

    scores = []
    possible_score = [25]
    for i in range(0, 21):
        possible_score.append(i)

    for element in throws:
        temp_score = 0
        # Connaitre le multiplicateur qui s'applique à un lancé
        if throws != '':
            multiplicator = element[0]
        if multiplicator == 's':
            multiplicator = 1
        elif multiplicator == 'd':
            multiplicator = 2
        elif multiplicator == 't':
            multiplicator = 3
        elif multiplicator == '' or multiplicator == ' ' or multiplicator == '0':
            multiplicator = 0
            # Savoir si un lancé en composé d'un nombre a trois chiffres ou à deux chiffres
        if len(element) == 2:
            if int(element[1]) in possible_score:
                temp_score = int(element[1])
            else:
                print "Ce score n'est pas vraiment possible"
        elif len(element) == 3:
            if int(element[1] + element[2]) in possible_score:
                temp_score = int(element[1] + element[2])
            else:
                print "Ce score n'est pas vraiment possible"
        else:
            temp_score = 0

        scores.append(temp_score * multiplicator)

    return scores
def classementCricket(name_player, game, players):
    """Display the blocked case for cricket

    Parameters
    ----------
    name_player : The score of this player will be display (str)
    game : The main dictionary of the game

    Return
    ------
    No return

    Notes
    -----
    Diplay on the console an array.

    Version 1.0
    """

    score_legit = ['15', '16', '17', '18', '19', '20', '25']
    score_blocked = []
    MAJ_name = name_player.upper()
    for score in score_legit:
        blocking_case = 0
        for player in players:
            if game[player][score] == 3:
                blocking_case += 1
        if len(players) == blocking_case:
            score_blocked.append(score)

    print '%s' % MAJ_name
    for element in score_legit:
        new_lign = '+-----+-----------+\n|'

        if element == '25':
            new_lign += 'Bull ' + '| '
        elif element != '25':
            new_lign += ' ' + element + '  | '
        if game[name_player][element] == 1:
            new_lign += '    X     |'
        elif game[name_player][element] == 2:
            new_lign += '   XX     |'
        elif game[name_player][element] == 3 and element not in score_blocked:
            new_lign += '   XXX    |'
        elif game[name_player][element] == 3 and element in score_blocked:
            new_lign += ' BLOCKED  |'
        else:
            new_lign += '          |'
        print new_lign

    print '+-----+-----------+'
def class_player(game, rounds, players, turn, type = 'X01'):
    """Class and display the classement of the player
    
    Parameters
    ----------
    game: main dict (dict)
    players: list of players (list) (string)
    rounds: round of the game (int)
    turn: nbr of turn in the game
    
    """

    #pprint.pprint(game)
    #print game[players[rounds]]
    #print game[players[rounds]]['score']
    print 'TOUR N°%d' %turn
    if game[players[rounds]]['score'] < 10:
        print "    ,-'\"\"\"`-,    ,-----.\n  ,' \ _|_ / `.  | %d   |"% (game[players[rounds]]['score'])
    elif game[players[rounds]]['score'] >= 10 and game[players[rounds]]['score'] < 100:
        print "    ,-'\"\"\"`-,    ,-----.\n  ,' \ _|_ / `.  |  %d |" % (game[players[rounds]]['score'])
    else:
        print "    ,-'\"\"\"`-,    ,-----.\n  ,' \ _|_ / `.  | %d |" % (game[players[rounds]]['score'])
    print " /`.,'\ | /`.,'\ `-----'  |\n(  /`. \|/ ,'\  )      |  H\n|--|--;=@=:--|--|   |  H  U\n(  \,' /|\ `./  )   H  U  |\n \,'`./ | \,'`./    U  | (|)\n  `. / \"\"\" \ ,'     | (|)"
    
    if game[players[rounds]]['last_score'] < 10:
        print "0%d  '-._|_,-`      (|)\n" %game[players[rounds]]['last_score']
    else:
        print "%d  '-._|_,-`      (|)\n" %(game[players[rounds]]['last_score'])
        
    if type == 'cricket':
        for element in players:
            classementCricket(element, game, players)
    if type == 'X01':
        for element in players:
            difference = game[players[rounds]]['score'] - game[element]['score']
            if element != players[rounds] and difference > 0:
                print '%d points pour rejoindre %s.' %(difference, element)
        if game[players[rounds]]['score'] <= 180:
            print 'Pour finir : %s' %best_throws(game[players[rounds]]['score'])
        
    sorted_players = []    
    sorted_score = []
    for element in players:
        score = game[element]['score']
        sorted_score.append(score)
        sorted_score.sort()
    
    if turn < 2:
        for element in players:
            if players.index(element) == 0:
                print '\n%der -- %s -- %d points.' %(players.index(element)+1, element, game[element]['score'])
            else:
                print '%de  -- %s -- %d points.' %(players.index(element)+1, element, game[element]['score']) 
    else:
        for score in sorted_score:
            for element in players:
                if game[element]['score'] == score and element not in sorted_players:
                    sorted_players.append(element)
        for element in sorted_players:
            if sorted_players.index(element) == 0:
                print '\n%der -- %s -- %d points.' %(sorted_players.index(element)+1, element, game[element]['score'])
            else:
                print '%de  -- %s -- %d points.' %(sorted_players.index(element)+1, element, game[element]['score'])
def create_dictionnary(nbr_players, score=0):
    """Create dictionnary for all function.

    Parameters
    ----------
    nbr_players : number of players (int)
    score : score of the game (int)

    Return
    ------
    game : The main dictionnary (dict)
    players : List of all the players (list)

    """

    players = []
    game = {}

    for i in range(nbr_players):  # Création de la liste de tous les joueurs
        name = raw_input("Quel est le nom du " + str(i + 1) + "e joueur ? ")
        players.append(name)

    for element in players:  # Création du dictionnaire en attribuant le score a chaque joueur
        game[element] = {}
        game[element]['score'] = score
        game[element]['last_score'] = 0

    return game, players

def check_blocked(game, players, score):
    """This function will check if the score can be add to the score of the player

    Parameters
    ---------
    game : The main dict of the game (dict)
    players : List of all the players (list)
    score : the score that the player made (int)

    Return
    ------
    True/False if the score can or can't be changed (bool)
    """

    checking_list = []

    for element in players:
        if game[element][str(score)] == 3:
            checking_list.append(1)
        else:
            checking_list.append(0)

    if 0 in checking_list:
        return True
    else:
        return False

def jeu_cricket(nbr_players):
    """Darts counter with cricket rules.

    Parameters
    ----------
    nbr_players : the number of player for this game (int)

    """

    # initialize the dictionary
    game, players = create_dictionnary(nbr_players)
    # Add the cricket case in the dictionnary
    for element in players:
        game[element]['25'] = 0
        for i in range(15, 21):
            game[element][str(i)] = 0
    pprint.pprint(game)
    # Begin the throwing
    turn = 1
    counter_strike = 0
    rounds = 0
    verification = True
    while verification == True:
        good_case = [15, 16, 17, 18, 19, 20, 25]
        print '\nC\'est au tour de %s' % players[rounds]
        class_player(game, rounds, players, turn, 'cricket')
        separated_throw = get_throw()
        pre_throw_score = game
        # Here we check if a case can always be shooted, because while all player have blocked it, she can't give points anymore.
        for element in separated_throw:
            for score in good_case:
                blocking_case = 0
                for player in players:
                    if game[player][str(score)] == 3:
                        blocking_case += 1
                if len(players) == blocking_case:
                    good_case.remove(score)

            # check if the throw can be good (len == 3)
            if len(element) == 3:
                # Get the score
                score = int(element[1] + element[2])
                # check if the throw is in the good range (15-20 && 25)
                if score in good_case:
                    # get the multiplicator
                    multiplicator = 0
                    if element[0] == 's':
                        multiplicator = 1
                    elif element[0] == 'd':
                        multiplicator = 2
                    elif element[0] == 't':
                        multiplicator = 3
                    else:
                        print 'ERROR MAGGLE'

                    # add score or block case
                    youcan = True
                    actual_player = players[rounds]
                    if game[actual_player][str(score)] == 0:
                        game[actual_player][str(score)] = multiplicator
                    elif game[actual_player][str(score)] == 1:
                        if multiplicator == 1:
                            game[actual_player][str(score)] = 2
                        elif multiplicator == 2:
                            game[actual_player][str(score)] = 3
                            print 'Case bloquée !'
                        else:
                            game[actual_player][str(score)] = 3
                            youcan = check_blocked(game, players, score)
                            if youcan == True:
                                game[actual_player]['score'] += score
                            print 'Case bloquée !'
                    elif game[actual_player][str(score)] == 2:
                        if multiplicator == 1:
                            game[actual_player][str(score)] = 3
                            print 'Case bloquée !'
                        elif multiplicator == 2:
                            game[actual_player][str(score)] = 3
                            youcan = check_blocked(game, players, score)
                            if youcan == True:
                                game[actual_player]['score'] += score
                            print 'Case bloquée !'
                        else:
                            game[actual_player][str(score)] = 3
                            youcan = check_blocked(game, players, score)
                            if youcan == True:
                                game[actual_player]['score'] += 2 * score
                            print 'Case bloquée'
                    else:
                        youcan = check_blocked(game, players, score)
                        if youcan == True:
                            game[actual_player]['score'] += multiplicator * score

        confirmation = raw_input("Tape \'Retour\' si tu t'es trompé.\n")
        if confirmation != 'retour' and confirmation != 'Retour':  # Permet au jour de se retracter si il a fait une erreur, c'est comme si le tour n'avait pas eu lieu
            if rounds == nbr_players - 1:
                rounds = 0
                counter_strike += 1
            else:
                rounds += 1
                counter_strike += 1
        else:
            game = pre_throw_score

        if counter_strike % (len(players)) == 0:
            turn += 1

        #on regarde si le joueur qui vient de jouer a bloqué toutes les cases et si il est premier en score
        beaten_player = 0
        blocked_case = 0
        for element in players:
            if game[element]['score'] < game[players[rounds]]['score']:
                beaten_player += 1
        for element in good_case:
            if game[players[rounds]][str(element)] == 3:
                blocked_case += 1
        if beaten_player == len(players)-1 and blocked_case == len(good_case):
            verification = False
            "Le gagnant est %s" %players[rounds]


        if turn == 25:
            verification = False
            for element in players:
                for second_element in players:
                    if game[element]['score'] >= game[second_element]['score']:
                        winner = element
                    else:
                        winner = second_element
            print 'Le gagnant est.. celui qui a le plus de points mdrrr\nNon mais en vrai je dois corriger ça parce que ça bug <3'
def separate_throw(throw):
    """Separate the throw

    Parameters
    ----------
    throw : string with all throw in form m00 m00 m00

    Return
    ------
    separate_throw : separated throw (list of int)

    """

    return throw.split(' ')
def best_throws(score):
    """
    Define the best throw to do to finish the game.

    Parameters
    ----------
    score: The score that left to complete the game. (int)

    Note
    ----
    If the score is to high or cannot be do, the function display nothing.

    Implémentation : William Polet

    """

    best_throws = ''
    initial_score = score

    possible_throws = []
    for throw in range(20, 0, -1):
        possible_throws.append(throw)

    for dart in range(0, 3):
        initial_multi = 0
        for throw in possible_throws:
            multi = 0
            if score >= 3 * throw and throw != 25:
                multi = 3
            elif score >= 2 * throw:
                multi = 2
            elif score >= throw:
                multi = 1

            if multi > initial_multi:
                initial_multi = multi
                best_throw = throw

        if initial_multi == 1:
            letter = 's'
        elif initial_multi == 2:
            letter = 'd'
        elif initial_multi == 3:
            letter = 't'

        if score != 0:  # Cette condition permet d'éviter des lancers supplémentaires inutiles si le score est déjà à 0
            best_throws += letter + str(best_throw) + ' - '
            score -= initial_multi * best_throw

    # Cas particulier:
    if initial_score == 50:
        best_throws = 'd25' + ' - '
    elif initial_score == 25:
        best_throws = 's25' + ' - '

    return best_throws[0: len(best_throws) - 3]

    if score > 0:
        print "It will remain %d to do" % score
def get_nbr():
    """This function will get a number from the user and will uncesur the type"""
    condition = False
    while condition == False:
        nbr_player = raw_input('Nombre de joueurs: ')
        try:
            int(nbr_player)
            condition = True
        except:
            condition = False

    return int(nbr_player)
def get_type():
    """return if the game is with elimination or not"""

    condition = 0
    while condition == 0:
        elimination = raw_input('Voulez vous jouer avec elimination ? (Oui/Non) ')
        if elimination != 'non' and elimination != 'Non' and elimination != 'NOn' and elimination != 'NON' and elimination != 'oui' and elimination != 'Oui' and elimination != 'OUi' and elimination != 'OUI':
            condition = 0
        else:
            condition = 1

    if elimination == 'Oui' or elimination == 'oui' or elimination == 'OUi' or elimination == 'OUI':
        return True
    elif elimination == 'Non' or elimination == 'non' or elimination == 'NOn' or elimination == 'NON':
        return False
def start_game():
    """Start the game and initialise every setting"""

    print '				 ____             _\n 				|  _ \  __ _ _ __| |_ ___ \n   /M\\\M|||M//.  		| | | |/ _` | \'__| __/ __|\n  /MMM\\\|||///M:. 		| |_| | (_| | |  | |_\__ \ \n /MMMMM\\ | //MMMM:.   		|____/ \__,_|_|   \__|___/\n(=========+======<]]]]::::::::::<|||_|||_|||_|||_|||_|||>=========-\n \#MMMM// | \\MMMM:\'\n  \#MM///|||\\\M:\'\n   \M///M|||M\\\''

    score = 0
    reponse = 'TA MERE LA CHIENNE'
    jeu = 0
    while reponse != 'X01' and reponse != 'x01' and reponse != 'Cricket' and reponse != 'cricket':
        reponse = raw_input('A quel jeu voulez vous jouez ? (X01/Cricket): ')
    if reponse == 'X01' or reponse == 'x01':
        while score != 301 and score != 101 and score != 201 and score != 401 and score != 501 and score != 601 and score != 701 and score != 801 and score != 901:
            score = input('A quel 01 voulez vous jouer ? (101 - 901) ')
        elimination = get_type()
        nbr_player = get_nbr()
        jeu = 1

    elif reponse == 'Cricket' or reponse == 'cricket':
        nbr_player = get_nbr()
        jeu = 2

    replay = 'oui'
    while replay == 'oui' or replay == 'Oui':
        if jeu == 1:
            jeux01(nbr_player, elimination, score)
        elif jeu == 2:
            jeu_cricket(nbr_player)
        replay = raw_input('Voulez-vous rejouer ? (Oui/Non) ')
        if replay == 'non' or replay == 'Non':
            print 'Merci d\'avoir joue !'



start_game()
     
     
      