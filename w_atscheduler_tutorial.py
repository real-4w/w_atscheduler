from apscheduler.schedulers.background import BackgroundScheduler

w_sched = BackgroundScheduler(daemon=True)

w_sched.add_job(lambda : w_sched.print_jobs(),'interval',seconds=5)