import json
import logging
import time
from collections.abc import Callable, Mapping
from typing import Any

from mpu6050 import mpu6050
from senspi.constants import NUMBER_PARAMETERS
from senspi.readconfig import get_logger

"""
Read MPU6050 data

Based on mpu6550-exampler.py from https://github.com/m-rtijn/mpu6050

Released under the MIT License
Copyright 2015, 2016 MrTijn/Tijndagamer
"""

ACCEL_KEY = "acceleration"
GIRO_KEY = "giroscope"
TEMP_KEY = "temperature"
X_KEY = "x"
Y_KEY = "y"
Z_KEY = "z"
NUMBER = {"@type": "float", "@defaults": NUMBER_PARAMETERS}

SCHEMA = {
    "@type": "map",
    ACCEL_KEY: {"@type": "map", X_KEY: NUMBER, Y_KEY: NUMBER, Z_KEY: NUMBER},
    GIRO_KEY: {"@type": "map", X_KEY: NUMBER, Y_KEY: NUMBER, Z_KEY: NUMBER},
    TEMP_KEY: NUMBER,
}

log = get_logger(__name__)


def initialize(parameters: Mapping[str, Any] = {}) -> Callable[[], dict[str, Any]]:
    channel = parameters.get("channel", 0x68)
    sensor = mpu6050(channel)

    def read() -> dict[str, Any]:
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        temp = sensor.get_temp()
        raw_values = {ACCEL_KEY: accel_data, GIRO_KEY: gyro_data, TEMP_KEY: temp}
        return raw_values

    return read


if __name__ == "__main__":
    r = initialize()
    while True:
        v = r()
        time.sleep(0.3)
        print(json.dumps(v, indent=2))
