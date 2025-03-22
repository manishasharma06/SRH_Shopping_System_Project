import redis

host = 'redis-15697.c300.eu-central-1-1.ec2.cloud.redislabs.com'
port = 15697
password = 'a2549FFbTE1Aze6TLHImux9HkxbcRwKL'


def get_redis_database():
    return redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)


if __name__ == "__main__":
    pass
