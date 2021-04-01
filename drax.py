#import mechanize as mz
#import time as t
from pyfiglet import Figlet
import sys
from importlib import import_module as im

try:
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('Drax'))
except:
    print("Drax")   
print("\nBrute force with a mind")     
print("\nAuthor: radioactvt\n")
cmd_disp = {
    'about':'./about.txt',
    'help':'./help.txt',
}
cmd_disp_set=cmd_disp.keys()
cmd_exec = {
    'fetch proxy':'modules.proxy_fetch',
    'start bruteforcing':'modules.bruteforce'
}
cmd_exec_set=cmd_exec.keys()
while(True):
    cmd=input('drax> ')
    if cmd=='exit' or cmd=='quit':
        print("Exiting Drax...")
        sys.exit()

    if cmd in cmd_disp_set:
        try:    
            print(open(cmd_disp[cmd],'r').read())
        except Exception as e:
            print(f"Error occured while trying to execute command {cmd}. Error message: {e}")    
        continue

    if cmd in cmd_exec_set:
        try:    
            #exec(open(cmd_exec[cmd],'r').read())
            im(cmd_exec[cmd]).run()
        except Exception as e:
            print(f"Error occured while trying to execute command {cmd}. Error message: {e}")
        continue
