
def generate_config():
    from os import getenv
    from hashlib import md5

    return {
        'email': getenv('EMAIL'),
        'passwd': md5(getenv('PASSWD').encode()).hexdigest(),
        'device_id': getenv('DEVICE_ID'),
        'country': getenv('COUNTRY'),
        'continent': getenv('CONTINENT')
    }
