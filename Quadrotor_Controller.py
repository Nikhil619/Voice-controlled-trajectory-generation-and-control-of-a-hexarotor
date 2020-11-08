# -*- coding: utf-8 -*-
"""

@author: Nikhil
"""


#function [F, M] = controller(t, state, des_state, params)
def controller(state, des_state, params):   
    
    """
   CONTROLLER  Controller for the planar quadrotor

   state: The current state of the robot with the following fields:
   state = {"pos" : [y z], "vel" : [y_dot, z_dot], "rot" : [phi], "omega" = [phi_dot]}

   des_state: The desired states are:
   des_state = {"pos" : [y z], "vel" : [y_dot, z_dot], "acc" : [y_ddot, z_ddot]}

   params: [mass, gravity, Ixx]
   
   Using these current and desired states, you have to compute the desired
   controls
    """
    u1 = 0
    u2 = 0

    k_vz = 20  # Derivative gains
    k_pz = 800  # Propotional gains
    k_vphi = 20
    k_pphi = 1000
    k_vy = 12
    k_py = 35

    u1 = params[0]*(params[1] + des_state["acc"][1] + k_vz*(des_state["vel"][1]-state["vel"][1]) + k_pz*(des_state["pos"][1]-state["pos"][1]))

    phic = -1/9.81*( des_state["acc"][0] + k_vy*(des_state["vel"][0] - state["vel"][0]) + k_py*(des_state["pos"][0]-state["pos"][0]) )
    phic_dot = 0
    phic_ddot = 0

    u2 = params[2]*(phic_ddot + k_vphi*(phic_dot - state["omega"]) + k_pphi*(phic - state["rot"]))
    
    return u1, u2