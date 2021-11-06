import schedule,time
import threading

def schedule_manager():
    def task():
        print("I'm working...")

    schedule.every(1).seconds.do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)

def start_schedule():
    thread_schedule = threading.Thread(target=schedule_manager)
    thread_schedule.setDaemon(True)
    thread_schedule.start()
