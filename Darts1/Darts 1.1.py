# -*- coding: utf-8 -*-
##########################################
#########Module python fléchettes#########
##########################################

def jeux01(nbr_player, elimination = False, begin_score = 301):
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
        print "\nC'est au tour de %s." %(players[rounds])
        class_player(game, rounds, players, turn)            
        separated_throw = get_throw()
        pre_throw_score = game[players[rounds]]['score'] #Variable utilisée pour remettre le score comme si 0 est dépassé
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
                    print 'Le gagnant est %s' %players[rounds]
                    condition =False
                else:
                    print 'Score trop eleve'
                    game[players[rounds]]['score'] = pre_throw_score      
        turn += 1
        game[players[rounds]]['last_score'] = round_score
        print 'Vous avez marque %d points\n' %round_score
        if rounds == nbr_player - 1:
            rounds = 0
        else: 
            rounds += 1
            
def get_throw():
    """Get throw and return them separated in a list)"""
    
    throw = raw_input('Entrez vos lances : ')
    return separate_throw(throw)

def get_score(throws):
    """compute and return the score of the player"""
    scores = []
    possible_score = [25]	
    for i in range(0, 21):
	possible_score.append(i)

    print possible_score
	
    for element in throws:
        temp_score = 0
        #Connaitre le multiplicateur qui s'applique à un lancé
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
        #Savoir si un lancé en composé d'un nombre a trois chiffres ou à deux chiffres
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

       
            
def class_player(game, rounds, players, turn):
    """Class and display the classement of the player
    
    Parameters
    ----------
    game: main dict (dict)
    players: list of players (list) (string)
    rounds: round of the game (int)
    turn: nbr of turn in the game
    
    """
    print game[players[rounds]]['score']
    print "    ,-'\"\"\"`-,    ,-----.\n  ,' \ _|_ / `.  | %d |\n /`.,'\ | /`.,'\ `-----'  |\n(  /`. \|/ ,'\  )      |  H\n|--|--;=@=:--|--|   |  H  U\n(  \,' /|\ `./  )   H  U  |\n \,'`./ | \,'`./    U  | (|)\n  `. / \"\"\" \ ,'     | (|)" % (game[players[rounds]]['score'])
    
    if game[players[rounds]]['last_score'] < 10:
        print "0%d  '-._|_,-`      (|)\n" %game[players[rounds]]['last_score']
    else:
        print "%d  '-._|_,-`      (|)\n" %(game[players[rounds]]['last_score'])
        
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
        
def create_dictionnary(nbr_players, score = 0):
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
    
    for i in range(nbr_players): #Création de la liste de tous les joueurs
        name = raw_input("Quel est le nom du " + str(i+1) +"e joueur ? ")
        players.append(name)
        
    for element in players: #Création du dictionnaire en attribuant le score a chaque joueur
        game[element] = {}
        game[element]['score'] = score 
        game[element]['last_score']= 0
        
    return game, players

def jeux_cricket(nbr_players):
    """Dart game with cricket rules.
    
    Parameters
    ----------
    nbr_players : number of players (int)
    
    """

	#Initialiser le dictionnaire.

	#Rajouter dans le dictionnaire les cases du cricket, dont aucune n'est touchée au départ.

	#Commencer les lancers.

    
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
            elif score >= 2 *  throw:
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

        if score != 0:#Cette condition permet d'éviter des lancers supplémentaires inutiles si le score est déjà à 0
            best_throws += letter + str(best_throw) + ' - '
            score -= initial_multi * best_throw

    #Cas particulier:
    if initial_score == 50:
        best_throws = 'd25' + ' - '
    elif initial_score == 25:
        best_throws = 's25' + ' - '
        
    return best_throws[0 : len(best_throws)-3]
    
    if score > 0:
        print "It will remain %d to do" %score

    
    
            
def start_game():
    """Start the game and initialise every setting"""
    
    print '				 ____             _\n 				|  _ \  __ _ _ __| |_ ___ \n   /M\\\M|||M//.  		| | | |/ _` | \'__| __/ __|\n  /MMM\\\|||///M:. 		| |_| | (_| | |  | |_\__ \ \n /MMMMM\\ | //MMMM:.   		|____/ \__,_|_|   \__|___/\n(=========+======<]]]]::::::::::<|||_|||_|||_|||_|||_|||>=========-\n \#MMMM// | \\MMMM:\'\n  \#MM///|||\\\M:\'\n   \M///M|||M\\\'' 
    
    score = 0
    while score != 301 and score != 101 and score != 201 and score != 401 and score != 501 and score != 601 and score != 701 and score != 801 and score != 901 :
        score = input('A quel 01 voulez vous jouer ? (101 - 901) ')
    elimination = raw_input('Voulez vous jouer avec elimination ? (Oui/Non) ')
    nbr_player = input('Nombre de joueurs : ')
    
    if elimination == 'Oui' or elimination == 'oui':
        elimination = True
    elif elimination == 'Non' or elimination == 'non':
        elimination = False
    
    replay = 'oui'
    while replay == 'oui' or replay == 'Oui':
        jeux01(nbr_player, elimination, score)
        replay = raw_input('Voulez-vous rejouer ? (Oui/Non) ')
        if replay == 'non' or replay == 'Non':
            print 'Merci d\'avoir joue !'           

start_game()
     
     
      