import asyncio
import websockets


connections = set()


async def handler(websocket):
	remote_address_port = websocket.remote_address[1]
	message = f"User{remote_address_port} just connceted"
	print(message)
	global connections
	connections.add(websocket)
	await websocket.send(message)
	for conn in connections:
		await conn.send(message)

	while True:
		recv_message = await websocket.recv()
		out_message = f"User{remote_address_port} says: {recv_message}"
		print(out_message)
		for conn in connections:
			await conn.send(out_message)


async def main():
	async with websockets.serve(handler, "localhost", 8001):
		await asyncio.Future()


if __name__ == "__main__":
	asyncio.run(main())





