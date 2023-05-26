import aiofiles
import asyncio


async def print_before():
	print("Before")

async def print_after():
	print("After")

async def read_file():
	try:
		async with aiofiles.open("sample.txt", "r") as file:
			data = await file.read()
			await asyncio.sleep(1)
			print(data)
	except Exception as e:
		print(e)

async def main():
	task_1 = asyncio.create_task(print_before())
	task_2 = asyncio.create_task(read_file())
	task_3 = asyncio.create_task(print_after())

	await task_1
	await task_2
	await task_3

if __name__ == "__main__":
	# print("Before read")
	asyncio.run(main())
	# print("After read")

