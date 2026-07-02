import playsound3
import sys
import platform
import sys
import ctypes
import subprocess
from pygame import mixer
import time

player_names = []
player_num = 0

mixer.init()


def trigger_fatal_error(error_message):
    current_os = platform.system()

    if current_os == "Windows":
        # Trigger the native Windows 'BING' and red X
        ctypes.windll.user32.MessageBoxW(0, error_message, "FATAL ERROR", 0x10)

    elif current_os == "Darwin":
        # Trigger the native Mac bouncing icon and warning
        apple_script = f'display dialog "{error_message}" with title "FATAL ERROR" buttons {{"OK"}} default button "OK" with icon stop'
        subprocess.run(["osascript", "-e", apple_script])

    else:
        # Fallback for Linux or anything else
        print(f"\n[FATAL ERROR] {error_message}\n")

    # Kill the game after the popup is closed
    sys.exit()


def Title_Screen():
    print("KILLER PRIEST: RE-BAPTISED", end="\n")
    playsound3.playsound("Sounds and Music/FLESH STAB.mp3", block=False)
    playsound3.playsound("Sounds and Music/Orchestra.mp3", block=False)
    time.sleep(1.5)
    mixer.music.load("Sounds and Music/MAIN THEME.mp3")
    mixer.music.set_volume(1)
    mixer.music.play(loops=-1)


def custom_input(input_text, data_type):
    while True:
        try:
            if data_type == "int":
                data_2_be_returned = int(input(input_text))
            elif data_type == "float":
                data_2_be_returned = float(input(input_text))
            else:
                data_2_be_returned = input(input_text)
            break

        except ValueError:
            print("Wrong data type. Try again.")
    return data_2_be_returned


def setup_contestants():
    global player_names
    global player_num
    player_names = []
    response = 0
    while player_num < 1 or player_num > (9):
        data_holder = custom_input("\nHow many suspects?   ", "int")
        player_num = int(data_holder)
        if player_num < 1:
            playsound3.playsound("Sounds and Music/EVERYTHING BREAKS DOWN.mp3")
            trigger_fatal_error("NUMERICAL ERROR. ZERO DOES NOT EXIST.")
        if player_num > 8:
            print("Max Limit of 8.")
    for i in range(player_num):
        player_names.append(input(f"Name of Contestant {i + 1}?   "))
    contestant_check()


def contestant_check():
    global player_num
    global player_names

    print(f"\nThere are {player_num} Contestants.")
    if player_num == 1:
        response = input(
            "Unfortunately, there is only 1 Contestant. You LONELY BASTARD. Are you sure you want to play alone?(Y/n)   "
        )
        if response == "Y":
            print("Understood.")
            main_game()
        elif response == "n":
            print("... Okay?")
            setup_contestants()
        else:
            print("... really? Nonsense? BACK TO THE BEGINNING YOU GO!")

    print("Their names are:")
    for i in range(player_num):
        print(f"{i + 1}) {player_names[i]}")

    response = "FUCKING NOTHING MUTHER-FUCKER"
    while response != "Y" or response != "n":
        response = input("Are you happy with all your selection?(Y/n)   ")
        if response == "Y" or response == "n":
            break

    if response == "n":
        while response != "1" or response != "2":
            response = input(
                "Understood. Press [1] for complete contestant reset, Press [2] for changing a name."
            )
            if response == "1" or response == "2":
                break
        if response == "1":
            setup_contestants()
        if response == "2":
            print(f"There are currently {player_num} Contestants.")
            response2 = "n"
            while response2 != "Y":
                response = 0
                while response < 1 or response > (player_num + 1):
                    response = int(
                        input(
                            f"From Contestants (1-{player_num}), whose name do you wish to Change? "
                        )
                    )
                    try:
                        if response < 1 or response > (player_num + 1):
                            return
                    except:
                        print("Whoops! Typo!")
                player_names[response - 1] = input(
                    f"What is the name of former Contestant {player_names[response - 1]}?   "
                )
                response2 = input("Are you done?(Y/n)   ")
                if response2 != "Y" and response2 != "n":
                    response2 = "n"

                if response2 == "Y":
                    contestant_check()

    elif response == "Y":
        main_game()


def main_game():
    mixer.music.stop()
    playsound3.playsound("Sounds and Music/MORE TRANSITION THAN ME.mp3")
    mixer.music.load("Sounds and Music/MAINER THEME.mp3")
    mixer.music.set_volume(1)
    mixer.music.play(loops=-1)
    print("Amongst You, One of you, is not what they seem.")
    time.sleep(1)
    print("One of you... is The killer Priest.")
    time.sleep(999999999)


Title_Screen()
setup_contestants()
