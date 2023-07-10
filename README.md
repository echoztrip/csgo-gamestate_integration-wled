# CS:GO to WLED gamestate integration (С4)    
Displays С4 status    
Green - can defuse    
Yellow - can defuse (only with defuse kit)    
Red - run!     
[Example video from original author](https://youtu.be/Oddy42e71_c)

## Dependencies
* [WLED](https://github.com/Aircoookie/WLED "WLED") for ESP8266/ESP32
* [Python 3.7](https://www.python.org/downloads/ "Python 3.7") (to run source code if necessary)
 * If you run the source, you may need to "pip3 install requests" 


##  Use
Download the ZIP from the repository.   
Place the unzipped "dist" folder in any directory.    
Copy "gamestate_integration_wled.cfg" to "csgo/cfg" directory.    
For example `D:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\gamestate_integration_wled.cfg`   
Adjust the IP address in the config.json to point to your WLED IP (dist/config.json)   
Run csgoWled.exe (from original developer)
Alternatively you can run the source python script with "python -i app.py"

[Counter-Strike: Global Offensive Game State Integration](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration)
