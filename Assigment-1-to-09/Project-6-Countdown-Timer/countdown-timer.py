import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = '{:02d}:{:02d}'.format(mins, secs)
        print("⏳ Time left:", timer_display, end='\r')  # \r overwrites the line
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")

seconds = input("Enter the time in seconds: ")

countdown_timer(int(seconds))

