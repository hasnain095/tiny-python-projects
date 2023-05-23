

import asyncio
import websockets


async def consumer_handler(websocket):
	while True:
		in_message = await websocket.recv()
		print(in_message)
		await asyncio.sleep(1)

async def producer_handler(websocket):
	while True:
		out_message = input()
		await websocket.send(out_message)
		await asyncio.sleep(1)


async def handler(websocket):
    consumer_task = asyncio.create_task(consumer_handler(websocket))
    producer_task = asyncio.create_task(producer_handler(websocket))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()


async def hello():
	print("You've entered chat")
	async with websockets.connect("ws://localhost:8001") as websocket:
		await handler(websocket)


asyncio.run(hello())