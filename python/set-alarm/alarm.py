import datetime

def main():
    get_alarm_time()
    get_alarm_sound()



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

if __name__ == "__main__":
    main()