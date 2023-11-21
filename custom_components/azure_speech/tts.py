"""Support for the Microsoft Cognitive Services text-to-speech service."""
import logging

import requests
import voluptuous as vol

from homeassistant.components.tts import PLATFORM_SCHEMA
from homeassistant.components.tts import Provider
import homeassistant.helpers.config_validation as cv

CONF_PATH = "path"
_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_PATH): cv.string,
    }
)


def get_engine(hass, config, discovery_info=None):
    """Set up Microsoft speech component."""
    return MyTTSProvider(
        config[CONF_PATH],
    )


class MyTTSProvider(Provider):
    """The Microsoft speech API provider."""

    def __init__(
        self, path
    ):
        """Init Microsoft TTS service."""
        self._path = path
        self.name = "My TTS"

    def get_tts_audio(self, message, language, options):
        """Load TTS from Microsoft."""

        response = requests.get("http://vvopc.ddns.net:19000/tts?txt=" + message)
        with open(self._path, "wb") as f:
            f.write(response.content)