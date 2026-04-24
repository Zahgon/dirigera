from __future__ import annotations
from typing import Any, Dict, Optional
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub

class WaterSensorAttributes(Attributes):
    battery_percentage: Optional[int] = None
    water_leak_detected: bool

class WaterSensor(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: WaterSensorAttributes

    def reload(self) -> WaterSensor:
        pass

    def set_name(self, name: str) -> None:
        pass

def dict_to_water_sensor(
    data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub
) -> WaterSensor:
    return WaterSensor(dirigeraClient=dirigera_client, **data)
