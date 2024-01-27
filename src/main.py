import time

import streamlit as st

from backend.devices.DeviceBase import DeviceBase
from controller.control import Controller
from core.enums.status import StatusEnum


@st.cache_resource
def get_controller():
    return Controller()

controller = get_controller()

st.title("Smart AC Service")


def state_emoji(status):
    if status == True:
        return ":large_green_circle:"
    elif status == False:
        return ":red_circle:"


def status_emoji(status):
    if status:
        return ":large_green_circle:"
    
    return ":black_circle:"

def device_emoji(device_name):
    if device_name == "TS1":
        return ":thermometer:"
    elif device_name == "AC1":
        return ":snowflake:"
    elif device_name == "AC_SW":
        return "🖲️"

def refresh():

    controller.service.feach_devices()


def on_click_turn_on():
    controller.service.turn_on_switch()



def on_click_turn_off():
    controller.service.turn_off_switch()



st.write("## Device Manager")
for device in controller.service.device_adapter.devices:
    col1, col2, col3 = st.columns([2, 1, 3])
    col1.write(f"{device_emoji(device.name)} {device.name} @ {device.location}")
    col1.write(
        f"Connection {status_emoji(device.is_connected)} Device State {state_emoji(device.is_status_ON)}"
    )

    if device.name == "AC1":
        tempeture = col2.slider("Set the target temperature", 16,30,25)
        controller.service.set_tempreture(tempeture)
        
    if device.name == "TS1" and device.is_connected == True:
        col2.metric(label="Temperature", value=f"{device.last_temp_reading} °C")

    if device.name == "AC_SW":
        if device.is_status_ON == True:
            turn_off_button = col2.button(
                "Turn off",
                key=f"turn_off_switch",
                on_click=on_click_turn_off,

            )
        elif device.is_status_ON == False:
            turn_on_button = col2.button(
                "Turn on",
                key=f"turn_on_switch",
                on_click=on_click_turn_on,

            )
while True:
    if controller.service.is_changed:
        controller.service.is_changed = False
        st.experimental_rerun()
    time.sleep(1)





