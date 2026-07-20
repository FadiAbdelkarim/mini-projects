import datetime
import subprocess
import time 

def main():
    print("###########################")
    print("###### Alarm Program ######")
    print("###########################\n")

    alarm_time = get_alarm_time()
    sound_path = get_alarm_sound()

    print(f"\n>>> Alarm has been set successfully for {alarm_time.strftime('%H:%M')}! Please don't close the program! <<<\n")

    wait_and_play(alarm_time, sound_path)


def get_alarm_time():
    while True:
        user_input = input("Set the alarm time (e.g. 01:10): ")
        try:
            alarm_time = datetime.datetime.strptime(user_input, "%H:%M").time()
            return alarm_time
        except ValueError:
            print("Invalid format. Please use HH:MM (e.g. 01:10).")


def get_alarm_sound():
    sound_list = ["Glass", "Ping", "Sosumi", "Hero", "Funk"]
    print("Select any alarm")
    for i, sound in enumerate(sound_list, start=1):
        print(f"{i}. {sound}")
    while True:
        choice = input("Enter the index of the listed musics (e.g. 1): ")
        if choice.isdigit() and 1 <= int(choice) <= len(sound_list):
            chosen_sound = sound_list[int(choice) - 1]
            return f"/System/Library/Sounds/{chosen_sound}.aiff"
        print("Invalid choice. Please enter a valid number.")


def wait_and_play(alarm_time, sound_path):
    while True:
        if alarm_time <= datetime.datetime.now().time():
            subprocess.run(["afplay", sound_path])
            break
        time.sleep(1)




if __name__ == "__main__":
    main()