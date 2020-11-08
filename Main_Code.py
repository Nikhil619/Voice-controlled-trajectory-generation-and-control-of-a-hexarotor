# -*- coding: utf-8 -*-
"""

@author: Nikhil
"""

import speech_recognition as sr
import pyttsx3
import datetime 
import os
import numpy as np
import matplotlib.pyplot as plt

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)


def speak(audio): 
	engine.say(audio) 
	engine.runAndWait() 

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning mister nikhil !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon mister nikhil !")    
   
    else: 
        speak("Good Evening mister nikhil !")   
   
    assname =("my name is Jarvis") 
    speak("I am your Drone sir") 
    speak(assname)
    speak("in which direction should i move")


def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query 


def desired_state_traj(t):
    v_max = 2
    a_max = 2
    if t <= v_max/a_max:
        dt = t
        acc = np.asarray([a_max, 0])
        vel = acc*dt
        pos = 0.5*acc*dt**2
    elif t <= 2*v_max/a_max:
        dt = t - v_max/a_max
        acc = np.asarray([0, 0])
        vel = np.asarray([v_max, 0])
        pos = np.asarray([v_max**2/(2*a_max), 0]) + np.asarray([v_max*dt, 0])
    elif t <= 3*v_max/a_max:
        dt = t - 2*v_max/a_max
        acc = np.asarray([-a_max, 0])
        vel = np.asarray([v_max, 0]) + acc*dt
        pos = np.asarray([3*v_max**2/(2*a_max), 0]) + np.asarray([v_max, 0])*dt + 0.5*acc*dt**2
    else:
        acc = np.asarray([0, 0])
        vel = np.asarray([0, 0])
        pos = np.asarray([2*v_max**2/a_max, 0])
    return acc, vel, pos

desired_state = {"pos" : np.asarray([0, 0]), "vel" : np.asarray([0, 0]), "acc" : np.asarray([0, 0])}
initial_pos = np.asarray([0,0])
pos = np.asarray([0,0])


if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
      
    # This Function will clean any 
    # command before execution of this python file 
    clear()
    wishMe() 
    
    
    t = 5    # Total time steps
    t = int(t)        
    y = []
    z = []
    
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command 
        if 'go forward' in query:
            speak("going forward")
            
            for i in range(0, t):
                acc, vel, pos = desired_state_traj(i)
                desired_state["pos"][0] = desired_state["pos"][0] + (pos[0])
                initial_pos = pos
                desired_state["vel"] = vel
                desired_state["acc"] = acc
                print(desired_state["pos"])
                y.append(desired_state["pos"][0])
                z.append(desired_state["pos"][1])
                
            """
                add the below 3 lines of code(controller function) before running the drone
            
                state = \add location where the state parameters are recorded\
                params = [mention the drone mass, mention the planet's gravity, mention Ixx]
                u1, u2 =  controller(state, des_state, params)
            
                give u1 and u2 to the drone
            """
            
             
            
  
        elif 'go right' in query:
            speak("going right")
            
            for i in range(0, t):
                acc, vel, pos = desired_state_traj(i)
                desired_state["pos"][1] = desired_state["pos"][1] + (pos[0])
                initial_pos = pos
                desired_state["vel"] = vel
                desired_state["acc"] = acc
                print(desired_state["pos"])
                y.append(desired_state["pos"][0])
                z.append(desired_state["pos"][1])
                
            """
                add the below 3 lines of code(controller function) before running the drone
            
                state = \add location where the state parameters are recorded\
                params = [mention the drone mass, mention the planet's gravity, mention Ixx]
                u1, u2 =  controller(state, des_state, params)
            
                give u1 and u2 to the drone
            """
            
            
             
  
        elif 'go left' in query: 
            speak("going leftt")
            
            for i in range(0, t):
                acc, vel, pos = desired_state_traj(i)
                desired_state["pos"][1] = desired_state["pos"][1] - (pos[0])
                initial_pos = pos
                desired_state["vel"] = vel
                desired_state["acc"] = acc
                print(desired_state["pos"])
                y.append(desired_state["pos"][0])
                z.append(desired_state["pos"][1])
                
            """
                add the below 3 lines of code(controller function) before running the drone
            
                state = \add location where the state parameters are recorded\
                params = [mention the drone mass, mention the planet's gravity, mention Ixx]
                u1, u2 =  controller(state, des_state, params)
            
                give u1 and u2 to the drone
            """
            
            
            
  
        elif 'come back' in query:
            speak("coming back")
            
            for i in range(0, t):
                acc, vel, pos = desired_state_traj(i)
                desired_state["pos"][0] = desired_state["pos"][0] - (pos[0])
                initial_pos = pos
                desired_state["vel"] = vel
                desired_state["acc"] = acc
                print(desired_state["pos"])
                y.append(desired_state["pos"][0])
                z.append(desired_state["pos"][1])
            
            """
                add the below 3 lines od code(controller function) before running the drone
            
                state = \add location where the state parameters are recorded\
                params = [mention the drone mass, mention the planet's gravity, mention Ixx]
                u1, u2 =  controller(state, des_state, params)
            
                give u1 and u2 to the drone
            """
            
            
            
  
        elif 'stop' in query: 
            speak("stop")
            
            for t in range(0, t):
                desired_state["pos"] = desired_state["pos"]
                initial_pos = pos
                desired_state["vel"] = 0
                desired_state["acc"] = 0
                print(desired_state["pos"])
                y.append(desired_state["pos"][0])
                z.append(desired_state["pos"][1]) 
                
            """
                add this code line below(controller function) before running the drone
            
                state = \add location where the state parameters are recorded\
                params = [mention the drone mass, mention the planet's gravity, mention Ixx]
                u1, u2 =  controller(state, des_state, params)
            
                give u1 and u2 to the drone
            """
            
            
    
        
        elif "sleep" in query:
            speak("okay im sleeping")
            speak("have a nice day sir")
            speak("it is an honour to be built by you")
            plt.plot(z,y, label = "desired path")
            plt.title('Path followed by the drone')
            plt.xlabel('z axis (meters)')
            plt.ylabel('y axis (meters)')
            plt.legend()
            plt.grid(True)
            plt.savefig('S.png',dpi = 1200)
            break
        
        else:
            speak("unable to recognize your voice sir")
            desired_state["pos"] = desired_state["pos"]
            initial_pos = pos
            desired_state["vel"] = 0
            desired_state["acc"] = 0
            print(desired_state["pos"])
            y.append(desired_state["pos"][0])
            z.append(desired_state["pos"][1])
                
            """
            add this code line below(controller function) before running the drone
            
            state = \add location where the state parameters are recorded\
            params = [mention the drone mass, mention the planet's gravity, mention Ixx]
            u1, u2 =  controller(state, des_state, params)
            
            give u1 and u2 to the drone
            """
         