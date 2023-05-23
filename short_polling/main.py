from time import sleep
from random import randrange

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

jobs = dict()


def update_job(job_id: str, status: int):
	jobs[job_id] = status
	if status == 100:
		return
	else:
		sleep(3)
		update_job(job_id, status+10)


@app.post("/create_job")
async def create_job(backgroundtasks: BackgroundTasks):
	job_id = str(randrange(0,10000,1))
	status = 0
	global jobs
	jobs[job_id] = status
	backgroundtasks.add_task(update_job, job_id, status)
	return {"job_id": job_id}


@app.get("/get_status")
async def get_status(job_id: str):
	status = jobs[job_id]
	return {"status": status}