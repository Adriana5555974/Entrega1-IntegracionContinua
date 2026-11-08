import redis

r = redis.Redis(host='redis', port=6379)
r.set('mensaje', 'Docker funciona')
print(r.get('mensaje').decode())