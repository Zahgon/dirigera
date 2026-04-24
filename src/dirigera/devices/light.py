from __future__ import annotations
from typing import Any, Optional, Dict
from .device import Attributes, Device, StartupEnum
from ..hub.abstract_smart_home_hub import AbstractSmartHomeHub


class LightAttributes(Attributes):
    startup_on_off: Optional[StartupEnum] = None
    is_on: bool
    light_level: Optional[int] = None
    color_temperature: Optional[int] = None
    color_temperature_min: Optional[int] = None
    color_temperature_max: Optional[int] = None
    color_hue: Optional[float] = None
    color_saturation: Optional[float] = None


class Light(Device):
    dirigera_client: AbstractSmartHomeHub
    attributes: LightAttributes

    def reload(self) -> Light:
        pass

    def set_name(self, name: str) -> None:
        pass

    def set_light(self, lamp_on: bool) -> None:
        pass

    def set_light_level(self, light_level: int) -> None:
        pass

    def set_color_temperature(self, color_temp: int) -> None:
        pass

    def set_light_color(self, hue: float, saturation: float) -> None:
        pass

    def set_startup_behaviour(self, behaviour: StartupEnum) -> None:
        """
        Sets the behaviour of the lamp in case of a power outage.
        When set to START_ON the lamp will turn on once the power is back.
        When set to START_OFF the lamp will stay off once the power is back.
        When set to START_PREVIOUS the lamp will resume its state at power outage.
        When set to START_TOGGLE, a sequence of power-off -> power-on, will toggle the lamp state
        """
        pass


def dict_to_light(data: Dict[str, Any], dirigera_client: AbstractSmartHomeHub) -> Light:
    return Light(
        dirigeraClient=dirigera_client,
        **data,
    )
