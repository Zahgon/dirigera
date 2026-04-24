from __future__ import annotations
from typing import Any, Dict, Optional
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub


class OccupancySensorAttributes(Attributes):
    battery_percentage: Optional[int] = None
    is_detected: Optional[bool] = None

class OccupancySensor(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: OccupancySensorAttributes

    def reload(self) -> OccupancySensor:
        pass

    def set_name(self, name: str) -> None:
        pass


def dict_to_occupancy_sensor(
    data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub
) -> OccupancySensor:
    return OccupancySensor(dirigeraClient=dirigera_client, **data)
