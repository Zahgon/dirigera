from __future__ import annotations
from typing import Any, Optional, Dict
from .device import Attributes, Device
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub


class BlindAttributes(Attributes):
    blinds_current_level: Optional[int] = None
    blinds_target_level: Optional[int] = None
    blinds_state: Optional[str] = None
    battery_percentage: Optional[int] = None


class Blind(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: BlindAttributes

    def reload(self) -> Blind:
        pass

    def set_name(self, name: str) -> None:
        pass

    def set_target_level(self, target_level: int) -> None:
        pass


def dict_to_blind(data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub) -> Blind:
    return Blind(dirigeraClient=dirigera_client, **data)
