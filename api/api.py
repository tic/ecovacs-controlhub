import sucks
from .config import generate_config as gen_conf

config = gen_conf()
api = sucks.EcoVacsAPI(config['device_id'], config['email'], config['passwd'], config['country'], config['continent'])

try:
    devices = api.devices()
except Exception as err:
    print('failed to load devices')
    print(err)
    devices = []

def get_vacbot(device_id):
    global devices
    for dev in devices:
        if dev['did'] == device_id:
            return sucks.VacBot(api.uid, api.REALM, api.resource, api.user_access_token, dev, config['continent'])
    return None

def list_bots():
    global devices
    return devices

def play_sound(device_id):
    try:
        vacbot = get_vacbot(device_id)
        vacbot.connect_and_wait_until_ready()
        vacbot.run(sucks.PlaySound())
        return True
    except Exception as err:
        print(err)
        return False
    finally:
        vacbot.disconnect()

def battery_state(device_id):
    try:
        vacbot = get_vacbot(device_id)
        if vacbot is None: return None
        vacbot.connect_and_wait_until_ready()
        vacbot.request_all_statuses()
        battery = {
            'battery': vacbot.battery_status,
            'charge': vacbot.charge_status,
            'overall': vacbot.vacuum_status
        }
        print(battery)
        print('done')
        return battery
    except Exception as err:
        print(err)
    finally:
        vacbot.disconnect()

def clean(device_id):
    pass
