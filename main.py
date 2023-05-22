import time
from plyer import notifications

if __name__ == "__main__":
    while True:
        notifications.notify(
            title = "Please drink water NOW!",
            message = "Drink atlest 2L of water to stay fit and in a good mood with glowing skin!",
            app_icon = "/Users/dswadha/Desktop/CV/projects/Desktop notification/icon.ico",
            timeout = 5
        )
    time.sleep(60*60)

