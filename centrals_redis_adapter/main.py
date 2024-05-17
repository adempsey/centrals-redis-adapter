import redis
from cerebus import cbpy

def main():
    redis_client = redis.Redis("localhost", 6379)
    # redis_client.xadd("CENTRALS_COMMANDS", {"key": "value"})
    while True:
        result = redis_client.xread({"CENTRALS_COMMANDS": b"0-0"})
        print(result[0])

if __name__ == "__main__":
    main()