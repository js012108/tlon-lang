#!/usr/bin/python3
from mas.environment.agent_factory.abstract_agent import *
from mas.environment.agent_factory.agents.programmed import *

from mas.environment import *


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

    # address = 'localhost'
    address = '::1'  # Localhost
    #address = 'fe80::5e93:a2ff:fea6:5155'  #  ubuntu-lenovo
    # address = 'fe80::ba27:ebff:fe21:684c'  #  raspberry-3
    #address = 'fe80::ba27:ebff:fe2d:96a3'  #  raspberry-4
    # address = 'fe80::3c07:54ff:fe84:f464'  #  mac

    ################### Environment Request #####################

    data = list()
    #data.append('ubuntu')
    data.append(65)
    # print(data)
    create_message(address, Request.NODE_INFO, data)

    ################### Single Action Agent #####################

    p = SingleActionAgent("action", 1)
    p.start()
    #p.clone()
    p.join()

    print('###################################################')
    ################### Periodic Agent ##########################

    a = CycleAgent('cycle', 1)
    a.start()
    a.join()

    print('###################################################')
    #################### TimeOut Agent ##########################

    t = TimeOutAgent("time_out", 1)
    t.start()
    t.join()

if __name__ == "__main__":
    # execute only if run as a script
    #main()

    r = ABCFSM("reactiveFSM", 1)
    r.run()
    #p.clone()
    
