from __future__ import annotations
from typing import Any, Optional, Dict
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub


class ControllerAttributes(Attributes):
    is_on: Optional[bool] = None
    battery_percentage: Optional[int] = None
    switch_label: Optional[str] = None


class Controller(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: ControllerAttributes

    def reload(self) -> Controller:
        pass

    def set_name(self, name: str) -> None:
        pass


def dict_to_controller(
    data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub
) -> Controller:
    return Controller(dirigeraClient=dirigera_client, **data)
