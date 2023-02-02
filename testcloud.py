import subprocess
import os 


# color
color_reset = "\033[0m"
color_green = "\33[32m"
color_yellow = "\033[33m"
color_red = "\33[91m"
color_bold = "\033[1m"

main_path=os.path.expanduser("~/CloudFlare")
check_path = os.system(f"ls {main_path} &> /dev/null")
if check_path != 0:
    os.mkdir(main_path)
else:
    print(f"{color_red}Project PATH Already Exist ... {color_reset}")


def find_fast_server():
    print(f"{color_bold}Testing the Servers ... {color_reset}")
    list_server = subprocess.check_output(f"cat {main_path}/servers.txt",shell=True,encoding='utf-8').replace(" ",'').split()

    avrs = []
    for i in list_server:
        if os.system(f"ping -c1 {i} &> /dev/null") == 0:            
            a = subprocess.check_output(f"ping -c 3 {i} | tail -n1 | cut -d' ' -f4 | cut -d'/' -f2",shell=True,encoding="utf-8").replace("\n" , "")
            avrs.append(float(a))
            print(f"{i} {color_green}OK{color_reset}   Speed:{color_yellow} {a} {color_reset}ms")
        else:
            print(f"{i} {color_red} Not Working!{color_reset}")
            list_server.remove(i)
    print(color_reset)

    # global fast_server
    # fast_server = list_server[0]
    # min = avrs[0]
    # for i in range(1, len(avrs)):
    #     if avrs[i] < min:
    #         min = avrs[i]
    #         fast_server = list_server[i]


find_fast_server()