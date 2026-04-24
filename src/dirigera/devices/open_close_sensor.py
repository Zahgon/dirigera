from __future__ import annotations
from typing import Any, Dict, Optional
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub


class OpenCloseSensorAttributes(Attributes):
    is_open: bool
    battery_percentage: Optional[int] = None

class OpenCloseSensor(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: OpenCloseSensorAttributes

    def reload(self) -> OpenCloseSensor:
        pass

    def set_name(self, name: str) -> None:
        pass


def dict_to_open_close_sensor(
    data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub
) -> OpenCloseSensor:
    return OpenCloseSensor(dirigeraClient=dirigera_client, **data)
