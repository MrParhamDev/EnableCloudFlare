import subprocess
import os 
import sys

# color
color_reset = "\033[0m"
color_green = "\33[32m"
color_yellow = "\033[33m"
color_red = "\33[91m"
color_bold = "\033[1m"

PROG_NAME="testcloud.py"

def help():
    print(\
f"""{color_bold}Usage:{color_reset} {PROG_NAME} [FILE]...
Find servers that are working or down
""", end='')

def find_fast_server(arg):
    print(f"{color_bold}Testing the Servers ... {color_reset}")
    list_server = subprocess.check_output(f"cat {arg}",shell=True,encoding='utf-8').replace(" ",'').split()

    for i in list_server:
        space = (20 - len(i)) * ' '


        cmd = "curl -s -o /dev/null -w '%{http_code}' " + f"http://{i}"
        response = int(subprocess.check_output(cmd, shell=True, encoding='utf-8'))

        if os.system(f"ping -c1 {i} &> /dev/null") == 0 and (response >= 200 and response <= 399) :            
            a = subprocess.check_output(f"ping -c 3 {i} | tail -n1 | cut -d' ' -f4 | cut -d'/' -f2",shell=True,encoding="utf-8").replace("\n" , "")
            print(f"{i} {color_green}OK{color_green} {space}Speed:{color_yellow} {a}{color_reset}ms {color_green}Response: {color_reset}{response}")

        else:
            print(f"{i}    {space}{color_red}Not Working!{color_reset} {color_yellow}    Response: {color_reset}{response}")
        print("-"*55)

    print(color_reset)


if len(sys.argv) > 1:
    find_fast_server(sys.argv[1]) 
else:
    help()