"""

CHARLY is my personal assistant 

"""

import var
import sensor
import command
import stt
import tts


var.keyword_ok = False

def main():
    """Main prog"""
    
    #init default sensors
    sens = sensor.Sensor()
    
    debug=var.debug
   
    done=False    
    
    wk=stt.Stt("keyword")
    voice=tts.Tts()
    voice.say("charly fait pouet pouet")

    done = False
    
    #main loop
    while not done:
        #waiting someone putting the magic button or someone saying magical word
	#TODO
        if (var.keyword_ok==True):
            var.keyword_ok = False
            wk.stop()
            #someone is here
            #so we try to recognise him/her with camera and ask what to do
            #if recognise
            #speak to recognised people
            voice.say("bonjour brice")
            text = font.render("Bonjour", True, (250, 250, 250))
            wk=stt.Stt("keyword")
            #else speak to unknown
            
            wk.stop()
            

            
            #after delay without more restart thread
        #else:
            #sleep mode ?
            #if (debug):
            #    print("no one")
            

    exit()
if __name__ == '__main__':
    main()
