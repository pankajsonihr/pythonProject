import asyncio
import os
from Speak import speak
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from meross_iot.model.enums import OnlineStatus
import API

EMAIL = os.environ.get(API.meros_email) or API.meros_email
PASSWORD = os.environ.get(API.meros_password) or API.meros_password


async def bulb_color(color_name):
    color_name = color_name.lower()
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "magenta": (255, 0, 255),
        "cyan": (0, 255, 255),
        "black": (0, 0, 0),
        "white": (255, 255, 255),
    }
    if color_name in colors:
        # Setup the HTTP client API from user-password
        http_api_client = await MerossHttpClient.async_from_user_password(email=EMAIL, password=PASSWORD)

        # Setup and start the device manager
        manager = MerossManager(http_client=http_api_client)
        await manager.async_init()

        # Retrieve the MSL120d devices that are registered on this account
        await manager.async_device_discovery()
        plugs = manager.find_devices(device_type="msl120d", online_status=OnlineStatus.ONLINE)

        if len(plugs) < 1:
            print("No online msl120d smart bulbs found...")
        else:
            # Let's play with RGB colors. Note that not all light devices will support
            # rgb capabilities. For this reason, we first need to check for rgb before issuing
            # color commands.
            dev = plugs[0]

            # Update device status: this is needed only the very first time we play with this device (or if the
            #  connection goes down)
            await dev.async_update()
            if not dev.get_supports_rgb():
                print("Unfortunately, this device does not support RGB...")
                # our assistant can speak this
            else:
                # Randomly chose a new color
                rgb = colors[color_name]
                print(f"Chosen random color (R,G,B): {rgb}")
                await dev.async_set_light_color(rgb=rgb)
                print("Color changed!")

        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()
    else:
        print("Sorry we don't know this color")

def bulb_color_change(color_name):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bulb_color(color_name))
    loop.stop()

async def bulb_switch(switch):
     # Setup the HTTP client API from user-password
        http_api_client = await MerossHttpClient.async_from_user_password(email=EMAIL, password=PASSWORD)

        # Setup and start the device manager
        manager = MerossManager(http_client=http_api_client)
        await manager.async_init()

        # Retrieve the MSL120d devices that are registered on this account
        await manager.async_device_discovery()
        plugs = manager.find_devices(device_type="msl120d", online_status=OnlineStatus.ONLINE)

        if len(plugs) < 1:
            print("No online msl120d smart bulbs found...")
        else:
            dev = plugs[0]
            if(switch==True):
                print(f"Turing on {dev.name}")
                await dev.async_turn_on(channel=0)
            if(switch == False):
                print(f"Turing off {dev.name}")
                await dev.async_turn_off(channel=0)
            else:
                print("We didn't got your command")
        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()
def bulb_onoff(switch):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bulb_switch(switch))
    loop.stop()

def bulb_commands(command):
    if 'red' in command:
        bulb_color_change('red')
        speak()
        #'on', 'off', 'red', '', '', '', '', '', '', ''
    elif 'green' in command:
        bulb_color_change('green')
        speak()
    elif 'blue' in command:
        bulb_color_change('blue')
        speak()
    elif 'yellow' in command:
        bulb_color_change('yellow')
        speak()
    elif 'magenta' in command:
        bulb_color_change('magenta')
        speak()
    elif 'cyan' in command:
        bulb_color_change('cyan')
        speak()
    elif 'black' in command:
        bulb_color_change('black')
        speak()
    elif 'white' in command:
        bulb_color_change('white')
        speak()
    elif 'on' in command:
        bulb_onoff(True)
        speak()
    elif 'off' in command:
        bulb_onoff(False)
        speak()
