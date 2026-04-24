from __future__ import annotations
from typing import Any, Dict, Optional
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub


class LightSensorAttributes(Attributes):
    battery_percentage: Optional[int] = None
    illuminance: Optional[int] = None
    max_illuminance: Optional[int] = None
    min_illuminance: Optional[int] = None

class LightSensor(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: LightSensorAttributes

    def reload(self) -> LightSensor:
        pass

    def set_name(self, name: str) -> None:
        pass


def dict_to_light_sensor(
    data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub
) -> LightSensor:
    return LightSensor(dirigeraClient=dirigera_client, **data)
