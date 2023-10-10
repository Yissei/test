import schedule
import time

def my_job():
    return "Hello, World!"

job = schedule.every("11:57").seconds.do(my_job)

while True:
    schedule.run_pending()
    result = job.run()
    print("Job Result:", result)
    time.sleep(1)