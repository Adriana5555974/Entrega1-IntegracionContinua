import os
import redis


def main():
    client = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        password=os.getenv("REDIS_PASSWORD"),
        decode_responses=True,
        socket_connect_timeout=5,
        socket_timeout=5,
    )
    key = "mensaje"
    message = os.getenv("APP_MESSAGE", "La aplicación se comunica con Redis")

    client.set(key, message)
    result = client.get(key)
    if result != message:
        raise RuntimeError(f"La lectura no coincide: {result!r}")

    print(f"Escritura en Redis: {key}={message}", flush=True)
    print(f"Lectura desde Redis: {key}={result}", flush=True)


if __name__ == "__main__":
    main()
