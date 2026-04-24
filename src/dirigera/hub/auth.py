import string
import hashlib
import random
import socket
import base64
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3

urllib3.disable_warnings(category=InsecureRequestWarning)

# requests.packages.urllib3.disable_warnings(  # pylint: disable=no-member
#     category=InsecureRequestWarning
# )

ALPHABET = f"_-~.{string.ascii_letters}{string.digits}"
CODE_LENGTH = 128


def random_char(alphabet: str) -> str:
    pass


def random_code(alphabet: str, length: int) -> str:
    pass


def code_challenge(code_verifier: str) -> str:
    pass


def send_challenge(ip_address: str, code_verifier: str) -> str:
    pass


def get_token(ip_address: str, code: str, code_verifier: str) -> str:
    pass


def main() -> None:
    pass
