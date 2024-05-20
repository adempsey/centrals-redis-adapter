import asyncio
import redis.asyncio as redis
from cerebus import cbpy
from enum import Enum

Commands = Enum("Commands", ["START", "STOP"])
COMMAND_STREAM = "CENTRALS_COMMANDS"

async def listener(channel: redis.client.PubSub):
    while True:
        message = await channel.get_message(ignore_subscribe_messages=True)
        if message is not None:
            command = message["data"].decode()
            print(command)

async def main():
    redis_client = redis.Redis(host="localhost", port=6379)

    async with redis_client.pubsub() as pubsub:
        await pubsub.subscribe(COMMAND_STREAM)
        future = asyncio.create_task(listener(pubsub))
        await future

if __name__ == "__main__":
    asyncio.run(main())