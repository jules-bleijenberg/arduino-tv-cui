from default_ir import *

commands = [
    Command("home", 1),
    Command("off", 2),
    Command("volume up", 7),
    Command("volume down", 11),
    Command("mute", 15),
    Command("settings", 26),
    Command("source", 31),
    Command("display", 40),
    Command("sound", 43),
    Command("return", 88),
    Command("up", 96),
    Command("down", 97),
    Command("right", 98),
    Command("left", 101),
    Command("ok", 104),
] 

while True:
    data = ser.readline().decode("utf-8")
    if data == "":
        user_command = input()
        for i in range(len(commands)):
            if user_command == commands[i].get_name():
                Send(str(commands[i].get_code()))
                time.sleep(0.5)
        else:
            if user_command.isdigit():
                Send(user_command)
                time.sleep(0.5)
    else:
        print(data)