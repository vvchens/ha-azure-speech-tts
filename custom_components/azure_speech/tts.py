"""Support for the Microsoft Cognitive Services text-to-speech service."""
import logging

import azure.cognitiveservices.speech as speechsdk

from requests.exceptions import HTTPError
import voluptuous as vol

from homeassistant.components.tts import PLATFORM_SCHEMA
from homeassistant.components.tts import Provider
from homeassistant.const import CONF_API_KEY, CONF_REGION
import homeassistant.helpers.config_validation as cv

CONF_PATH = "path"
_LOGGER = logging.getLogger(__name__)

DEFAULT_REGION = "eastus"


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_PATH): cv.string,
        vol.Optional(CONF_REGION, default=DEFAULT_REGION): cv.string,
    }
)


def get_engine(hass, config, discovery_info=None):
    """Set up Microsoft speech component."""
    return CustomMicrosoftProvider(
        config[CONF_API_KEY],
        config[CONF_PATH],
        config[CONF_REGION],
    )


class CustomMicrosoftProvider(Provider):
    """The Microsoft speech API provider."""

    def __init__(
        self, apikey, path, region
    ):
        """Init Microsoft TTS service."""
        self._apikey = apikey
        self._path = path
        self._region = region
        self.name = "Custom Microsoft"
        
        speech_config = speechsdk.SpeechConfig(subscription=apikey, region=region)
        audio_config = speechsdk.audio.AudioOutputConfig(filename=path)
        # speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name='zh-CN-XiaoxiaoNeural'
        speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio48Khz192KBitRateMonoMp3)
        self._sdk = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    def get_tts_audio(self, message, language, options):
        """Load TTS from Microsoft."""
        speech_synthesis_result = self._sdk.speak_text_async(message).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return True
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            _LOGGER.error("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    _LOGGER.error("Error details: {}".format(cancellation_details.error_details))
                    _LOGGER.error("Did you set the speech resource key and region values?")
            return False
