# pylint:disable=too-many-public-methods
import ssl
from typing import Any, Dict, List, Optional
import requests
import websocket  # type: ignore
import urllib3
from requests import HTTPError
from urllib3.exceptions import InsecureRequestWarning

from .utils import camelize_dict
from ..devices.device import Device
from .abstract_smart_home_hub import AbstractSmartHomeHub
from ..devices.air_purifier import AirPurifier, dict_to_air_purifier
from ..devices.light import Light, dict_to_light
from ..devices.blinds import Blind, dict_to_blind
from ..devices.controller import Controller, dict_to_controller
from ..devices.outlet import Outlet, dict_to_outlet
from ..devices.environment_sensor import EnvironmentSensor, dict_to_environment_sensor
from ..devices.motion_sensor import MotionSensor, dict_to_motion_sensor
from ..devices.open_close_sensor import OpenCloseSensor, dict_to_open_close_sensor
from ..devices.scene import Action, Info, Scene, SceneType, Trigger, dict_to_scene
from ..devices.water_sensor import WaterSensor, dict_to_water_sensor
from ..devices.occupancy_sensor import OccupancySensor, dict_to_occupancy_sensor
from ..devices.light_sensor import LightSensor, dict_to_light_sensor

urllib3.disable_warnings(category=InsecureRequestWarning)


class Hub(AbstractSmartHomeHub):
    def __init__(
        self,
        token: str,
        ip_address: str,
        port: str = "8443",
        api_version: str = "v1",
    ) -> None:
        """
        Initializes a new instance of the Hub class.

        Args:
            token (str): The authentication token for the hub.
            ip_address (str): The IP address of the hub.
            port (str, optional): The port number for the hub API. Defaults to "8443".
            api_version (str, optional): The version of the API to use. Defaults to "v1".
        """
        self.api_base_url = f"https://{ip_address}:{port}/{api_version}"
        self.websocket_base_url = f"wss://{ip_address}:{port}/{api_version}"
        self.token = token
        self.wsapp: Any = None

    def headers(self) -> Dict[str, Any]:
        pass

    def create_event_listener(
        self,
        on_open: Any = None,
        on_message: Any = None,
        on_error: Any = None,
        on_close: Any = None,
        on_ping: Any = None,
        on_pong: Any = None,
        on_data: Any = None,
        on_cont_message: Any = None,
        ping_intervall: int = 60,
        dispatcher: Any = None,
        reconnect: int = None,
    ) -> None:
        """
        Create an event listener.

        Args:
            on_open (Any, optional)
            on_message (Any, optional)
            on_error (Any, optional)
            on_close (Any, optional)
            on_ping (Any, optional)
            on_pong (Any, optional)
            on_data (Any, optional)
            on_cont_message (Any, optional)
            ping_intervall (int, optional): Ping interval in Seconds. Defaults to 60.
            dispatcher (Any, optional)
            reconnect (int, optional)
        """
        pass

    def stop_event_listener(self) -> None:
        pass

    def patch(self, route: str, data: List[Dict[str, Any]]) -> Any:
        pass

    def get(self, route: str) -> Any:
        pass

    def post(self, route: str, data: Optional[Dict[str, Any]] = None) -> Any:
        pass

    def delete(self, route: str, data: Optional[Dict[str, Any]] = None) -> Any:
        pass

    def _get_device_data_by_id(self, id_: str) -> Dict:
        """
        Fetches device data by its id
        """
        pass

    def get_air_purifiers(self) -> List[AirPurifier]:
        """
        Fetches all air purifiers registered in the Hub
        """
        pass

    def get_air_purifier_by_id(self, id_: str) -> AirPurifier:
        pass

    def get_lights(self) -> List[Light]:
        """
        Fetches all lights registered in the Hub
        """
        pass

    def get_light_by_name(self, lamp_name: str) -> Light:
        """
        Fetches all lights and returns first result that matches this name
        """
        pass

    def get_light_by_id(self, id_: str) -> Light:
        """
        Fetches a light by its id if that light does not exist or is a device of another type raises ValueError
        """
        pass

    def get_outlets(self) -> List[Outlet]:
        """
        Fetches all outlets registered in the Hub
        """
        pass

    def get_outlet_by_name(self, outlet_name: str) -> Outlet:
        """
        Fetches all outlets and returns first result that matches this name
        """
        pass

    def get_outlet_by_id(self, id_: str) -> Outlet:
        """
        Fetches an outlet by its id if that outlet does not exist or is a device of another type raises ValueError
        """
        pass

    def get_environment_sensors(self) -> List[EnvironmentSensor]:
        """
        Fetches all environment sensors registered in the Hub
        """
        pass

    def get_environment_sensor_by_id(self, id_: str) -> EnvironmentSensor:
        pass

    def get_motion_sensors(self) -> List[MotionSensor]:
        """
        Fetches all motion sensors registered in the Hub
        """
        pass

    def get_motion_sensor_by_name(self, motion_sensor_name: str) -> MotionSensor:
        """
        Fetches all motion sensors and returns first result that matches this name
        """
        pass

    def get_motion_sensor_by_id(self, id_: str) -> MotionSensor:
        pass

    def get_open_close_sensors(self) -> List[OpenCloseSensor]:
        """
        Fetches all open/close sensors registered in the Hub
        """
        pass

    def get_open_close_by_id(self, id_: str) -> OpenCloseSensor:
        pass

    def get_blinds(self) -> List[Blind]:
        """
        Fetches all blinds registered in the Hub
        """
        pass

    def get_blind_by_name(self, blind_name: str) -> Blind:
        """
        Fetches all blinds and returns first result that matches this name
        """
        pass

    def get_blinds_by_id(self, id_: str) -> Blind:
        pass

    def get_controllers(self) -> List[Controller]:
        """
        Fetches all controllers registered in the Hub
        """
        pass

    def get_controller_by_name(self, controller_name: str) -> Controller:
        """
        Fetches all controllers and returns first result that matches this name
        """
        pass

    def get_controller_by_id(self, id_: str) -> Controller:
        """
        Fetches a controller by its id
        if that controller does not exist or is a device of another type raises ValueError
        """
        pass

    def get_scenes(self) -> List[Scene]:
        """
        Fetches all scenes
        """
        pass

    def get_scene_by_id(self, scene_id: str) -> Scene:
        """
        Fetches a specific scene by a given id
        """
        pass

    def get_scene_by_name(self, scene_name: str) -> Scene:
        """
        Fetches all scenes and returns the first result that matches scene_name
        """
        pass

    def get_water_sensors(self) -> List[WaterSensor]:
        """
        Fetches all water sensors registered in the Hub
        """
        pass

    def get_water_sensor_by_id(self, id_: str) -> WaterSensor:
        """
        Fetches a water sensor by its id
        if that water sensors does not exist or is a device of another type raises ValueError
        """
        pass

    def get_light_sensors(self) -> List[LightSensor]:
        """
        Fetches all light sensors registered in the Hub
        """
        pass

    def get_light_sensor_by_id(self, id_: str) -> LightSensor:
        """
        Fetches a light sensor by its id
        if that light sensor does not exist or is a device of another type raises ValueError
        """
        pass

    def get_occupancy_sensors(self) -> List[OccupancySensor]:
        """
        Fetches all occupancy sensors registered in the Hub
        """
        pass

    def get_occupancy_sensor_by_id(self, id_: str) -> OccupancySensor:
        """
        Fetches an occupancy sensor by its id
        if that occupancy sensor does not exist or is a device of another type raises ValueError
        """
        pass

    def get_all_devices(self) -> List[Device]:
        """
        Fetches all devices registered in the Hub
        """
        pass

    def create_scene(
        self,
        info: Info,
        scene_type: SceneType = SceneType.USER_SCENE,
        triggers: Optional[List[Trigger]] = None,
        actions: Optional[List[Action]] = None,
    ) -> Scene:
        """Creates a new scene.

        Note:
        To create an empty scene leave actions and triggers None.

        Args:
            info (Info): Name & Icon
            type (SceneType): typically USER_SCENE
            triggers (List[Trigger]): Triggers for the Scene (An app trigger will be created automatically)
            actions (List[Action]): Actions that will be run on Trigger

        Returns:
            Scene: Returns the newly created scene.
        """
        pass

    def delete_scene(self, scene_id: str) -> None:
        pass
