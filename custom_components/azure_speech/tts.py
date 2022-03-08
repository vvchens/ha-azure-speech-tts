"""Support for the Azure Cognitive Services text to speech service."""
import logging
from typing import Final

import azure.cognitiveservices.speech as speechsdk
import voluptuous as vol

from homeassistant.components.tts import (
    PLATFORM_SCHEMA as BASE_PLATFORM_SCHEMA,
    Provider,
    TtsAudioType,
)
from homeassistant.const import ATTR_CREDENTIALS
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import (
    CONF_FREQUENCY,
    CONF_LANGUAGE,
    CONF_OUTPUT_FORMAT,
    CONF_OUTPUT_FORMAT_DETAILED,
    CONF_REGION,
    CONF_SPEECH_KEY,
    CONF_TEXT_TYPE,
    CONF_VOICE,
    DEFAULT_FREQUENCY,
    DEFAULT_LANGUAGE,
    DEFAULT_OUTPUT_FORMAT,
    DEFAULT_REGION,
    DEFAULT_TEXT_TYPE,
    SUPPORTED_FORMAT_FREQUENCY_MAP,
    SUPPORTED_FREQUENCIES,
    SUPPORTED_LANGUAGES,
    SUPPORTED_OUTPUT_FORMATS,
    SUPPORTED_REGIONS,
    SUPPORTED_TEXT_TYPES,
    SUPPORTED_VOICES,
)

_LOGGER: Final = logging.getLogger(__name__)

PLATFORM_SCHEMA: Final = BASE_PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_REGION, default=DEFAULT_REGION): vol.In(SUPPORTED_REGIONS),
        vol.Inclusive(CONF_SPEECH_KEY, ATTR_CREDENTIALS): cv.string,

        vol.Optional(CONF_LANGUAGE, default=DEFAULT_LANGUAGE): vol.In(SUPPORTED_LANGUAGES),
        vol.Optional(CONF_VOICE): vol.In(SUPPORTED_VOICES),
        vol.Optional(CONF_OUTPUT_FORMAT, default=DEFAULT_OUTPUT_FORMAT): vol.In(
            SUPPORTED_OUTPUT_FORMATS
        ),
        vol.Optional(CONF_FREQUENCY, default=DEFAULT_FREQUENCY): vol.In(
            SUPPORTED_FREQUENCIES
        ),
        vol.Optional(CONF_OUTPUT_FORMAT_DETAILED): vol.In(
            list(speechsdk.SpeechSynthesisOutputFormat.__members__.keys())
        ),
        vol.Optional(CONF_TEXT_TYPE, default=DEFAULT_TEXT_TYPE): vol.In(
            SUPPORTED_TEXT_TYPES
        ),
    }
)


def get_engine(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType = None,
) -> Provider:
    """Set up Azure Cognitive Services speech component."""

    output_format_detailed = config.get(CONF_OUTPUT_FORMAT_DETAILED)
    if output_format_detailed is not None:
        if output_format_detailed not in speechsdk.SpeechSynthesisOutputFormat.__members__:
            _LOGGER.error(
                "%s is not a valid detailed output format", output_format_detailed
            )
            return None
    else:
        output_format = config.get(CONF_OUTPUT_FORMAT)
        if output_format not in SUPPORTED_OUTPUT_FORMATS:
            _LOGGER.error(
                "%s is not a valid output format", output_format
            )
            return None
        
        frequency = config.get(CONF_FREQUENCY, DEFAULT_FREQUENCY)
        if frequency not in SUPPORTED_FREQUENCIES:
            _LOGGER.error(
                "%s is not a valid frequency", frequency
            )
            return None
        output_format_detailed = SUPPORTED_FORMAT_FREQUENCY_MAP.get((output_format, frequency))
        if output_format_detailed is None:
            _LOGGER.error(
                "%s is not a valid frequency for %s", frequency, output_format
            )
            return None
        # Assign detailed format based on simple config settings
        config[CONF_OUTPUT_FORMAT_DETAILED] = output_format_detailed

    speech_language = config.get(CONF_LANGUAGE)
    if speech_language not in SUPPORTED_LANGUAGES:
        _LOGGER.error(
            "%s is not a language supported by Azure Speech", speech_language
        )
        return None
    
    all_voices = list(speechsdk.SpeechSynthesisOutputFormat.__members__.keys())

    return AzureSpeechProvider(config, SUPPORTED_LANGUAGES, all_voices)


class AzureSpeechProvider(Provider):
    """Azure Speech api provider."""

    def __init__(
        self,
        config: ConfigType,
        supported_languages: list[str],
        all_voices: dict[str, dict[str, str]],
    ) -> None:
        """Initialize Azure Speech provider for TTS."""
        self.config = config
        self.supported_langs = supported_languages
        self.all_voices = all_voices
        self.default_voice: str = self.config[CONF_VOICE]
        self.name = "Azure Speech Service"

    @property
    def supported_languages(self) -> list[str]:
        """Return a list of supported languages."""
        return self.supported_langs

    @property
    def default_language(self) -> str:
        """Return the default language."""
        return DEFAULT_LANGUAGE

    @property
    def default_options(self) -> dict[str, str]:
        """Return dict include default options."""
        return {CONF_VOICE: self.default_voice}

    @property
    def supported_options(self) -> list[str]:
        """Return a list of supported options."""
        return [CONF_VOICE]

    def get_tts_audio(
        self,
        message: str,
        language: str = None,
        options: dict[str, str] = None,
    ) -> TtsAudioType:
        """Request TTS file from Azure."""
        if options is None or language is None:
            _LOGGER.debug("language and/or options were missing")
            return None, None

        voice_name = options.get(CONF_VOICE)
        # If voice_name is None then SDK will use default voice for
        # language without additional configuration
        if voice_name is not None and not voice_name.startswith(language):
            _LOGGER.error("%s does not support the %s language", voice_name, language)
            return None, None

        speech_config = speechsdk.SpeechConfig(
            subscription=self.config.get(CONF_SPEECH_KEY),
            region=self.config.get(CONF_REGION))
        
        speech_config.speech_synthesis_language = language
        speech_config.speech_synthesis_voice_name = voice_name

        output_format = self.config[CONF_OUTPUT_FORMAT_DETAILED]
        if 'mp3' in output_format.lower():
            content_type = 'mp3'
        elif 'ogg' in output_format.lower():
            content_type = 'ogg'
        elif 'pcm' in output_format.lower():
            content_type = 'pcm'
        else:
            content_type = 'pcm'
        _LOGGER.debug("Sending TTS for format %s with content type=%s, language=%s, voice=%s",
            output_format, content_type, language, voice_name)
        speech_config.set_speech_synthesis_output_format(
            speechsdk.SpeechSynthesisOutputFormat[output_format])

        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        _LOGGER.debug("Requesting TTS file for text: %s", message)
        if self.config[CONF_TEXT_TYPE] == "ssml":
            resp = synthesizer.speak_ssml(message)
        else:
            resp = synthesizer.speak_text(message)

        _LOGGER.debug("Reply received for TTS: %s", message)
        return (
            content_type,
            resp.audio_data,
        )
