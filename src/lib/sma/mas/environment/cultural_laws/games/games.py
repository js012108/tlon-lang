class AbstractGame(object):
    pass

#####################################################################


class PrisonersDilemma(AbstractGame):
    pass

#####################################################################


class NPrisonersDilemma(AbstractGame):

    pass

#####################################################################


class PublicGoodsGame(AbstractGame):

    pass
#####################################################################


class ColitionalGame(AbstractGame):

    pass
#####################################################################


def join_mas(data,Environment):
    """
    If node is registered then return its Coalition (CS) Id
    If not, then register node as god and wait.

    """
    if data[0] in Environment.nodes_directory:

        coalition_id = Environment.nodes_directory[data[0]]
        cs = Environment.games_directory[coalition_id]
        print("JOIN\nVia Cs.::::", cs.get_agents()[0].community_id)
        print("Via coalition_id::::", coalition_id)

    else:
        cs = Environment.create_control_space(Environment, data[0])
        Environment.nodes_directory[data[0]] = str(cs.get_agents()[0].community_id)
        Environment.games_directory[str(cs.get_agents()[0].community_id)] = cs
        #game = CS.get_agents()[0].play_game(data[0],CS)

    return cs.get_agents()[0].community_id


    #####################################################################
    #                   GAME Functions
    #####################################################################
    # reset_MAS(self, data):
    #
    # Function that erase all MAS data, be carefully when using, only
    # for developing
    # proposes...


def reset_mas(Environment):
    Environment.games_directory = {}
    Environment.agents_directory = {}
    Environment.service_directory = {}
    Environment.environments_directory = {}
    Environment.nodes_directory = {}
    return Environment.print_world()

    #####################################################################
    # Function that executes a run of the "Game as" interpreted system.
    #
    # data should contain the ControlSpace_id of node who is doing the request to
    # play a tournament against and with all other communities, each game
    # will asign a total of workers can work for a coalition
    # .
    #
    #   play_GAME(data) -> {data(ControlSpace_id): score, eachOther_id: score}
    #
    #####################################################################

def play_game(data,Environment):
    i = 0
    data = data[0]

    if len(Environment.games_directory) <= 1:
        return "Error, directorio de juegos vacio"

    scores = []
    print(Environment.games_directory, str(data) in Environment.games_directory)
    print (Environment.games_directory.get(str(data)))
    if (str(data) not in Environment.games_directory):
        return json.dumps("Juego no encontrado")

    coalition = Environment.games_directory.get(str(data))
    ######################################################################
    # For all games check community_id, collude whit equals and be intelligent
    # with others,
    # be intelligent every time-
    #
    print ("Colaicioiionnoinoinoioi",coalition)
    for k in list(Environment.games_directory):
        i += 1
        print("------------------Juego ", i, " ----------------")
        opponent = Environment.games_directory.get(k)
        print ("Opontenerererrereerre", opponent)
        print ("Node", opponent.get_agents()[0].community_id, " vs ", coalition.get_agents()[0].community_id)
        game = coalition.get_agents("coordinator").play_game(opponent, coalition)
        if (not (game["coalition"])):  # deside if collude or not?
             scores.append(json.dumps(game["game"].getScores()))
             coalition.collude(opponent)
        else:
             print ("Same Coalition Game then 'forward'")
             scores.append(game["scores"])
    return json.dumps(scores)

    #####################################################################
    # work(self, data)
    # Start the pool or treads owned by workers pool or the coalition
    #

def work(data,Environment):

    if len(Environment.games_directory) <= 1:
        return "Error, directorio de juegos vacio"

    coalition = Environment.games_directory[str(data[0])]
    result = coalition.work(data)

    return result
