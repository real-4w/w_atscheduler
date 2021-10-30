from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time,os 

def tick():
    print(f"Tick! The time is: {datetime.now()}.")
    w_sched.print_jobs()

w_sched = BackgroundScheduler(daemon=True)


w_sched.add_job(tick,'interval',seconds=5, id='w_sched')

w_sched.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    # This is here to simulate application activity (which keeps the main thread alive).
    while True:
       time.sleep(10)
except (KeyboardInterrupt, SystemExit):
    # Not strictly necessary if daemonic mode is enabled but should be done if possible
    w_sched.shutdown() 




