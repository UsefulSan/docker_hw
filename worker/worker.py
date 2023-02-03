import redis

client = redis.Redis(host="redis", port=6379)

while True:
    request = client.brpop("queue")[1]
    print('Ответ: ', eval(request))
