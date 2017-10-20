#!/usr/bin/python3
import sys
sys.path.append('..')
from mas.environment import *
from mas.environment import Request


def main():
    """
    #########################################################################
    #                                 Testing - MAS
    #########################################################################

    Available environment requests:

    NODE_INFO: get device information where the environment is running
            Example:
                        create_message(address, Request.NODE_INFO)

    ACTIVE_NODES: get the addresses of active nodes in the ad hoc network
            Example:
                        create_message(address, Request.ACTIVE_NODES

    INFO_ACTIVE_NODES: get device information of all active nodes in the ad hoc
                        network
            Example:
                        create_message(address, Request.INFO_ACTIVE_NODES

    LOCAL_RESOURCES: Get resources information where the environment is running.
                        To obtain detail information of this function you can check
                        the file MAS_TLON/environment/resources.py (line 92)
            Example:
                        create_message(address, Request.LOCAL_RESOURCES)

    VIS_NET_TOPOLOGY: Get network topology in a .dot file. This method uses A.L.F.R.E.D
                        Daemon. Please check  MAS_TLON/network/topology.dot
            Example:
                        create_message(address, Request.VIS_NET_TOPOLOGY)


    SET_ALFRED_DATA: Set information in the A.L.F.R.E.D daemon to flood the network with
                        useful data. You need to pass a list as parameter
                        with data and a datatype > 63
            Example:
                        data = ['data to flood the network', 64]
                        create_message(address, Request.SET_ALFRED_DATA, data)

    GET_ALFRED_DATA: Get information from A.L.F.R.E.D daemon. You need to pass
                        a datatype > 63 as parameter
            Example:
                        data = [64]
                        create_message(address, Request.GET_ALFRED_DATA, data)
    """

    ############################################################
    #               Devices usually used to test MAS
    ############################################################

    #address = 'fe80::5e93:a2ff:fea6:5155'  #  ubuntu-lenovo
    #address = 'fe80::ba27:ebff:fe21:684c'  #  raspberry-3
    #address = 'fe80::ba27:ebff:fe2d:96a3'  #  raspberry-4
    #address = 'fe80::3c07:54ff:fe84:f464'  #  mac
    address = 'fe80::226:82ff:fef2:ff30'  #  Ubuntu-HP-Envy

    ############################################################

    data = list()
    #data.append('Ubuntu')
   # data.append(str(sys.argv[2]))
    functions={"play":Request.PLAY_GAME,
               "join":Request.JOIN_GAME,
               "work":Request.DO_WORK,
               "print":Request.PRINT_WORLD,
               "reset":Request.RESET_GAME}

    if (functions.get(sys.argv[1])):

        data.append(str(sys.argv[2]))
        if (functions.get(sys.argv[1])==Request.RESET_GAME or functions.get(sys.argv[1])==Request.JOIN_GAME or functions.get(sys.argv[1])==Request.PRINT_WORLD):
            print(create_message(address, functions.get(sys.argv[1]), data))
        else:
            community_id = create_message(address, Request.JOIN_GAME, data)
            print(create_message(address, functions.get(sys.argv[1]), [community_id]))


    else:
        for x in range(int(sys.argv[1]), int(sys.argv[2])):
            print("MAC"+str(x))
            community_id=create_message(address,Request.JOIN_GAME,["MAC"+str(x)])
            print("Coalition Number--->",community_id)

        print(create_message(address, Request.PLAY_GAME, [community_id]))
        community_id = create_message(address, Request.JOIN_GAME, ["MAC" + str(x)])
        print(create_message(address, Request.DO_WORK, [community_id]))

if __name__ == "__main__":
    # execute only if run as a script
    main()
