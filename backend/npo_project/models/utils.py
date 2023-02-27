from yandex_geocoder import Client


def get_coordinates(address):
    client = Client('8d85ce6f-3c2a-430c-b9f4-4702060528e9')
    return client.coordinates(address)
