from __future__ import annotations
from enum import Enum
from typing import Any, Dict
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub

class FanModeEnum(Enum):
    OFF = "off"
    ON = "on"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    AUTO = "auto"

class AirPurifierAttributes(Attributes):
    """canReceive"""
    fan_mode: FanModeEnum
    fan_mode_sequence: str
    motor_state: int
    child_lock: bool
    status_light: bool
    """readOnly"""
    motor_runtime: int
    filter_alarm_status: bool
    filter_elapsed_time: int
    filter_lifetime: int
    current_p_m25: int

class AirPurifier(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: AirPurifierAttributes

    def reload(self) -> AirPurifier:
        pass

    def set_name(self, name: str) -> None:
        pass

    def set_fan_mode(self, fan_mode: FanModeEnum) -> None:
        pass

    def set_motor_state(self, motor_state: int) -> None:
        """
        Sets the fan behaviour.
        Values 0 to 50 allowed.
        0 == off
        1 == auto
        """
        pass

    def set_child_lock(self, child_lock: bool) -> None:
        pass

    def set_status_light(self, light_state: bool) -> None:
        pass

def dict_to_air_purifier(data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub) -> AirPurifier:
    return AirPurifier(
        dirigeraClient=dirigera_client,
        **data
    )
