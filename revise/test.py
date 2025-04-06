import psutil
import time
import argparse
import os


def test():
    parser=argparse.ArgumentParser()
    parser.add_argument("--interval",type=int,help="sampling interval in seconds",
                        default=1)
    args=parser.parse_args()
    
    if os.path.exists("/home/franz/log") != True:
        return -1  
    else:
        f=open("/home/franz/log/system-log","w")

    while True:
        users_list=psutil.users() #lista di tuple (utenti)
        #ricavare dalla prima tupla il nome (nel nostro caso di un solo utente)
        clock=time.time()
        username=users_list[0][0]
        boot_time=users_list[0][3]
        cpu_usage=psutil.cpu_percent(percpu=True)
        swap_usage=(psutil.swap_memory())[3]
        vm_usage=(psutil.virtual_memory())[2]
        print(f'epoch:{clock} - user:{username} - uptime:{boot_time} : CPU%{cpu_usage}\nVM%{vm_usage},SW%{swap_usage}\n\n')      
        f.write(f'epoch:{clock} - user:{username} - uptime:{boot_time} : CPU%{cpu_usage}\nVM%{vm_usage},SW%{swap_usage}\n\n')      
        time.sleep(args.interval) 
        

if __name__ == "__main__":
    result=test()
    if result == -1:
        print("No /home/franz/log folder")
