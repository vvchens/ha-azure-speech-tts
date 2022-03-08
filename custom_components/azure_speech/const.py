from typing import Final, Tuple

CONF_REGION: Final = "region"
CONF_SPEECH_KEY: Final = "azure_speech_key"

DEFAULT_REGION: Final = "eastus"
# https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-custom-subdomains#is-there-a-list-of-regional-endpoints
SUPPORTED_REGIONS: Final[list[str]] = [
    "eastus",
    "brazilsouth",
    "canadacentral",
    "centralus",
    "eastasia",
    "eastus2",
    "francecentral",
    "centralindia",
    "japaneast",
    "koreacentral",
    "northcentralus",
    "northeurope",
    "southafricanorth",
    "southcentralus",
    "southeastasia",
    "uksouth",
    "westcentralus",
    "westeurope",
    "westus",
    "westus2",
    "virginia",  # US Gov
    "chinaeast2",
    "chinanorth",
]

CONF_LANGUAGE: Final = "language"
CONF_VOICE: Final = "voice"
CONF_OUTPUT_FORMAT: Final = "output_format"
CONF_FREQUENCY: Final = "frequency"
CONF_OUTPUT_FORMAT_DETAILED: Final = 'output_format_detailed'
CONF_TEXT_TYPE: Final = "text_type"

SUPPORTED_LANGUAGES: Final[list[str]] = [
    "af-ZA",
    "am-ET",
    "ar-AE",
    "ar-BH",
    "ar-DZ",
    "ar-EG",
    "ar-IQ",
    "ar-JO",
    "ar-KW",
    "ar-LY",
    "ar-MA",
    "ar-QA",
    "ar-SA",
    "ar-SY",
    "ar-TN",
    "ar-YE",
    "bg-BG",
    "bn-BD",
    "bn-IN",
    "ca-ES",
    "cs-CZ",
    "cy-GB",
    "da-DK",
    "de-AT",
    "de-CH",
    "de-DE",
    "el-GR",
    "en-AU",
    "en-CA",
    "en-GB",
    "en-HK",
    "en-IE",
    "en-IN",
    "en-KE",
    "en-NG",
    "en-NZ",
    "en-PH",
    "en-SG",
    "en-TZ",
    "en-US",
    "en-ZA",
    "es-AR",
    "es-BO",
    "es-CL",
    "es-CO",
    "es-CR",
    "es-CU",
    "es-DO",
    "es-EC",
    "es-ES",
    "es-GQ",
    "es-GT",
    "es-HN",
    "es-MX",
    "es-NI",
    "es-PA",
    "es-PE",
    "es-PR",
    "es-PY",
    "es-SV",
    "es-US",
    "es-UY",
    "es-VE",
    "et-EE",
    "fa-IR",
    "fi-FI",
    "fil-PH",
    "fr-BE",
    "fr-CA",
    "fr-CH",
    "fr-FR",
    "ga-IE",
    "gl-ES",
    "gu-IN",
    "he-IL",
    "hi-IN",
    "hr-HR",
    "hu-HU",
    "id-ID",
    "is-IS",
    "it-IT",
    "ja-JP",
    "jv-ID",
    "kk-KZ",
    "km-KH",
    "kn-IN",
    "ko-KR",
    "lo-LA",
    "lt-LT",
    "lv-LV",
    "mk-MK",
    "ml-IN",
    "mr-IN",
    "ms-MY",
    "mt-MT",
    "my-MM",
    "nb-NO",
    "nl-BE",
    "nl-NL",
    "pl-PL",
    "ps-AF",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "si-LK",
    "sk-SK",
    "sl-SI",
    "so-SO",
    "sr-RS",
    "su-ID",
    "sv-SE",
    "sw-KE",
    "sw-TZ",
    "ta-IN",
    "ta-LK",
    "ta-SG",
    "te-IN",
    "th-TH",
    "tr-TR",
    "uk-UA",
    "ur-IN",
    "ur-PK",
    "uz-UZ",
    "vi-VN",
    "zh-CN",
    "zh-HK",
    "zh-TW",
    "zu-ZA",
]

# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#prebuilt-neural-voices
SUPPORTED_VOICES: Final[list[str]] = [
    "af-ZA-AdriNeural",  # af-ZA, Female, Afrikaans (South Africa), General
    "af-ZA-WillemNeural",  # af-ZA, Male, Afrikaans (South Africa), General
    "am-ET-AmehaNeural",  # am-ET, Male, Amharic (Ethiopia), General
    "am-ET-MekdesNeural",  # am-ET, Female, Amharic (Ethiopia), General
    "ar-AE-FatimaNeural",  # ar-AE, Female, Arabic (United Arab Emirates), General
    "ar-AE-HamdanNeural",  # ar-AE, Male, Arabic (United Arab Emirates), General
    "ar-BH-AliNeural",  # ar-BH, Male, Arabic (Bahrain), General
    "ar-BH-LailaNeural",  # ar-BH, Female, Arabic (Bahrain), General
    "ar-DZ-AminaNeural",  # ar-DZ, Female, Arabic (Algeria), General
    "ar-DZ-IsmaelNeural",  # ar-DZ, Male, Arabic (Algeria), General
    "ar-EG-SalmaNeural",  # ar-EG, Female, Arabic (Egypt), General
    "ar-EG-ShakirNeural",  # ar-EG, Male, Arabic (Egypt), General
    "ar-IQ-BasselNeural",  # ar-IQ, Male, Arabic (Iraq), General
    "ar-IQ-RanaNeural",  # ar-IQ, Female, Arabic (Iraq), General
    "ar-JO-SanaNeural",  # ar-JO, Female, Arabic (Jordan), General
    "ar-JO-TaimNeural",  # ar-JO, Male, Arabic (Jordan), General
    "ar-KW-FahedNeural",  # ar-KW, Male, Arabic (Kuwait), General
    "ar-KW-NouraNeural",  # ar-KW, Female, Arabic (Kuwait), General
    "ar-LY-ImanNeural",  # ar-LY, Female, Arabic (Libya), General
    "ar-LY-OmarNeural",  # ar-LY, Male, Arabic (Libya), General
    "ar-MA-JamalNeural",  # ar-MA, Male, Arabic (Morocco), General
    "ar-MA-MounaNeural",  # ar-MA, Female, Arabic (Morocco), General
    "ar-QA-AmalNeural",  # ar-QA, Female, Arabic (Qatar), General
    "ar-QA-MoazNeural",  # ar-QA, Male, Arabic (Qatar), General
    "ar-SA-HamedNeural",  # ar-SA, Male, Arabic (Saudi Arabia), General
    "ar-SA-ZariyahNeural",  # ar-SA, Female, Arabic (Saudi Arabia), General
    "ar-SY-AmanyNeural",  # ar-SY, Female, Arabic (Syria), General
    "ar-SY-LaithNeural",  # ar-SY, Male, Arabic (Syria), General
    "ar-TN-HediNeural",  # ar-TN, Male, Arabic (Tunisia), General
    "ar-TN-ReemNeural",  # ar-TN, Female, Arabic (Tunisia), General
    "ar-YE-MaryamNeural",  # ar-YE, Female, Arabic (Yemen), General
    "ar-YE-SalehNeural",  # ar-YE, Male, Arabic (Yemen), General
    "bg-BG-BorislavNeural",  # bg-BG, Male, Bulgarian (Bulgaria), General
    "bg-BG-KalinaNeural",  # bg-BG, Female, Bulgarian (Bulgaria), General
    "bn-BD-NabanitaNeural",  # bn-BD, Female, Bangla (Bangladesh), General
    "bn-BD-PradeepNeural",  # bn-BD, Male, Bangla (Bangladesh), General
    "bn-IN-BashkarNeural New",  # bn-IN, Male, Bengali (India), General
    "bn-IN-TanishaaNeural New",  # bn-IN, Female, Bengali (India), General
    "ca-ES-AlbaNeural",  # ca-ES, Female, Catalan (Spain), General
    "ca-ES-EnricNeural",  # ca-ES, Male, Catalan (Spain), General
    "ca-ES-JoanaNeural",  # ca-ES, Female, Catalan (Spain), General
    "cs-CZ-AntoninNeural",  # cs-CZ, Male, Czech (Czech), General
    "cs-CZ-VlastaNeural",  # cs-CZ, Female, Czech (Czech), General
    "cy-GB-AledNeural",  # cy-GB, Male, Welsh (United Kingdom), General
    "cy-GB-NiaNeural",  # cy-GB, Female, Welsh (United Kingdom), General
    "da-DK-ChristelNeural",  # da-DK, Female, Danish (Denmark), General
    "da-DK-JeppeNeural",  # da-DK, Male, Danish (Denmark), General
    "de-AT-IngridNeural",  # de-AT, Female, German (Austria), General
    "de-AT-JonasNeural",  # de-AT, Male, German (Austria), General
    "de-CH-JanNeural",  # de-CH, Male, German (Switzerland), General
    "de-CH-LeniNeural",  # de-CH, Female, German (Switzerland), General
    "de-DE-ConradNeural",  # de-DE, Male, German (Germany), General
    "de-DE-KatjaNeural",  # de-DE, Female, German (Germany), General
    "el-GR-AthinaNeural",  # el-GR, Female, Greek (Greece), General
    "el-GR-NestorasNeural",  # el-GR, Male, Greek (Greece), General
    "en-AU-NatashaNeural",  # en-AU, Female, English (Australia), General
    "en-AU-WilliamNeural",  # en-AU, Male, English (Australia), General
    "en-CA-ClaraNeural",  # en-CA, Female, English (Canada), General
    "en-CA-LiamNeural",  # en-CA, Male, English (Canada), General
    "en-GB-LibbyNeural",  # en-GB, Female, English (United Kingdom), General
    "en-GB-RyanNeural",  # en-GB, Male, English (United Kingdom), General
    "en-GB-SoniaNeural",  # en-GB, Female, English (United Kingdom), General
    "en-HK-SamNeural",  # en-HK, Male, English (Hongkong), General
    "en-HK-YanNeural",  # en-HK, Female, English (Hongkong), General
    "en-IE-ConnorNeural",  # en-IE, Male, English (Ireland), General
    "en-IE-EmilyNeural",  # en-IE, Female, English (Ireland), General
    "en-IN-NeerjaNeural",  # en-IN, Female, English (India), General
    "en-IN-PrabhatNeural",  # en-IN, Male, English (India), General
    "en-KE-AsiliaNeural",  # en-KE, Female, English (Kenya), General
    "en-KE-ChilembaNeural",  # en-KE, Male, English (Kenya), General
    "en-NG-AbeoNeural",  # en-NG, Male, English (Nigeria), General
    "en-NG-EzinneNeural",  # en-NG, Female, English (Nigeria), General
    "en-NZ-MitchellNeural",  # en-NZ, Male, English (New Zealand), General
    "en-NZ-MollyNeural",  # en-NZ, Female, English (New Zealand), General
    "en-PH-JamesNeural",  # en-PH, Male, English (Philippines), General
    "en-PH-RosaNeural",  # en-PH, Female, English (Philippines), General
    "en-SG-LunaNeural",  # en-SG, Female, English (Singapore), General
    "en-SG-WayneNeural",  # en-SG, Male, English (Singapore), General
    "en-TZ-ElimuNeural",  # en-TZ, Male, English (Tanzania), General
    "en-TZ-ImaniNeural",  # en-TZ, Female, English (Tanzania), General
    "en-US-AmberNeural",  # en-US, Female, English (United States), General
    "en-US-AnaNeural",  # en-US, Kid, English (United States), General
    "en-US-AriaNeural",  # en-US, Female, English (United States), General, multiple voice styles available using SSML
    "en-US-AshleyNeural",  # en-US, Female, English (United States), General
    "en-US-BrandonNeural",  # en-US, Male, English (United States), General
    "en-US-ChristopherNeural",  # en-US, Male, English (United States), General
    "en-US-CoraNeural",  # en-US, Female, English (United States), General
    "en-US-ElizabethNeural",  # en-US, Female, English (United States), General
    "en-US-EricNeural",  # en-US, Male, English (United States), General
    "en-US-GuyNeural",  # en-US, Male, English (United States), General, multiple voice styles available using SSML
    "en-US-JacobNeural",  # en-US, Male, English (United States), General
    "en-US-JennyNeural",  # en-US, Female, English (United States), General, multiple voice styles available using SSML
    "en-US-MichelleNeural",  # en-US, Female, English (United States), General
    "en-US-MonicaNeural",  # en-US, Female, English (United States), General
    "en-US-SaraNeural",  # en-US, Female, English (United States), General, multiple voice styles available using SSML
    "en-ZA-LeahNeural",  # en-ZA, Female, English (South Africa), General
    "en-ZA-LukeNeural",  # en-ZA, Male, English (South Africa), General
    "es-AR-ElenaNeural",  # es-AR, Female, Spanish (Argentina), General
    "es-AR-TomasNeural",  # es-AR, Male, Spanish (Argentina), General
    "es-BO-MarceloNeural",  # es-BO, Male, Spanish (Bolivia), General
    "es-BO-SofiaNeural",  # es-BO, Female, Spanish (Bolivia), General
    "es-CL-CatalinaNeural",  # es-CL, Female, Spanish (Chile), General
    "es-CL-LorenzoNeural",  # es-CL, Male, Spanish (Chile), General
    "es-CO-GonzaloNeural",  # es-CO, Male, Spanish (Colombia), General
    "es-CO-SalomeNeural",  # es-CO, Female, Spanish (Colombia), General
    "es-CR-JuanNeural",  # es-CR, Male, Spanish (Costa Rica), General
    "es-CR-MariaNeural",  # es-CR, Female, Spanish (Costa Rica), General
    "es-CU-BelkysNeural",  # es-CU, Female, Spanish (Cuba), General
    "es-CU-ManuelNeural",  # es-CU, Male, Spanish (Cuba), General
    "es-DO-EmilioNeural",  # es-DO, Male, Spanish (Dominican Republic), General
    "es-DO-RamonaNeural",  # es-DO, Female, Spanish (Dominican Republic), General
    "es-EC-AndreaNeural",  # es-EC, Female, Spanish (Ecuador), General
    "es-EC-LuisNeural",  # es-EC, Male, Spanish (Ecuador), General
    "es-ES-AlvaroNeural",  # es-ES, Male, Spanish (Spain), General
    "es-ES-ElviraNeural",  # es-ES, Female, Spanish (Spain), General
    "es-GQ-JavierNeural",  # es-GQ, Male, Spanish (Equatorial Guinea), General
    "es-GQ-TeresaNeural",  # es-GQ, Female, Spanish (Equatorial Guinea), General
    "es-GT-AndresNeural",  # es-GT, Male, Spanish (Guatemala), General
    "es-GT-MartaNeural",  # es-GT, Female, Spanish (Guatemala), General
    "es-HN-CarlosNeural",  # es-HN, Male, Spanish (Honduras), General
    "es-HN-KarlaNeural",  # es-HN, Female, Spanish (Honduras), General
    "es-MX-DaliaNeural",  # es-MX, Female, Spanish (Mexico), General
    "es-MX-JorgeNeural",  # es-MX, Male, Spanish (Mexico), General
    "es-NI-FedericoNeural",  # es-NI, Male, Spanish (Nicaragua), General
    "es-NI-YolandaNeural",  # es-NI, Female, Spanish (Nicaragua), General
    "es-PA-MargaritaNeural",  # es-PA, Female, Spanish (Panama), General
    "es-PA-RobertoNeural",  # es-PA, Male, Spanish (Panama), General
    "es-PE-AlexNeural",  # es-PE, Male, Spanish (Peru), General
    "es-PE-CamilaNeural",  # es-PE, Female, Spanish (Peru), General
    "es-PR-KarinaNeural",  # es-PR, Female, Spanish (Puerto Rico), General
    "es-PR-VictorNeural",  # es-PR, Male, Spanish (Puerto Rico), General
    "es-PY-MarioNeural",  # es-PY, Male, Spanish (Paraguay), General
    "es-PY-TaniaNeural",  # es-PY, Female, Spanish (Paraguay), General
    "es-SV-LorenaNeural",  # es-SV, Female, Spanish (El Salvador), General
    "es-SV-RodrigoNeural",  # es-SV, Male, Spanish (El Salvador), General
    "es-US-AlonsoNeural",  # es-US, Male, Spanish (US), General
    "es-US-PalomaNeural",  # es-US, Female, Spanish (US), General
    "es-UY-MateoNeural",  # es-UY, Male, Spanish (Uruguay), General
    "es-UY-ValentinaNeural",  # es-UY, Female, Spanish (Uruguay), General
    "es-VE-PaolaNeural",  # es-VE, Female, Spanish (Venezuela), General
    "es-VE-SebastianNeural",  # es-VE, Male, Spanish (Venezuela), General
    "et-EE-AnuNeural",  # et-EE, Female, Estonian (Estonia), General
    "et-EE-KertNeural",  # et-EE, Male, Estonian (Estonia), General
    "fa-IR-DilaraNeural",  # fa-IR, Female, Persian (Iran), General
    "fa-IR-FaridNeural",  # fa-IR, Male, Persian (Iran), General
    "fi-FI-HarriNeural",  # fi-FI, Male, Finnish (Finland), General
    "fi-FI-NooraNeural",  # fi-FI, Female, Finnish (Finland), General
    "fi-FI-SelmaNeural",  # fi-FI, Female, Finnish (Finland), General
    "fil-PH-AngeloNeural",  # fil-PH, Male, Filipino (Philippines), General
    "fil-PH-BlessicaNeural",  # fil-PH, Female, Filipino (Philippines), General
    "fr-BE-CharlineNeural",  # fr-BE, Female, French (Belgium), General
    "fr-BE-GerardNeural",  # fr-BE, Male, French (Belgium), General
    "fr-CA-AntoineNeural",  # fr-CA, Male, French (Canada), General
    "fr-CA-JeanNeural",  # fr-CA, Male, French (Canada), General
    "fr-CA-SylvieNeural",  # fr-CA, Female, French (Canada), General
    "fr-CH-ArianeNeural",  # fr-CH, Female, French (Switzerland), General
    "fr-CH-FabriceNeural",  # fr-CH, Male, French (Switzerland), General
    "fr-FR-DeniseNeural",  # fr-FR, Female, French (France), General
    "fr-FR-HenriNeural",  # fr-FR, Male, French (France), General
    "ga-IE-ColmNeural",  # ga-IE, Male, Irish (Ireland), General
    "ga-IE-OrlaNeural",  # ga-IE, Female, Irish (Ireland), General
    "gl-ES-RoiNeural",  # gl-ES, Male, Galician (Spain), General
    "gl-ES-SabelaNeural",  # gl-ES, Female, Galician (Spain), General
    "gu-IN-DhwaniNeural",  # gu-IN, Female, Gujarati (India), General
    "gu-IN-NiranjanNeural",  # gu-IN, Male, Gujarati (India), General
    "he-IL-AvriNeural",  # he-IL, Male, Hebrew (Israel), General
    "he-IL-HilaNeural",  # he-IL, Female, Hebrew (Israel), General
    "hi-IN-MadhurNeural",  # hi-IN, Male, Hindi (India), General
    "hi-IN-SwaraNeural",  # hi-IN, Female, Hindi (India), General
    "hr-HR-GabrijelaNeural",  # hr-HR, Female, Croatian (Croatia), General
    "hr-HR-SreckoNeural",  # hr-HR, Male, Croatian (Croatia), General
    "hu-HU-NoemiNeural",  # hu-HU, Female, Hungarian (Hungary), General
    "hu-HU-TamasNeural",  # hu-HU, Male, Hungarian (Hungary), General
    "id-ID-ArdiNeural",  # id-ID, Male, Indonesian (Indonesia), General
    "id-ID-GadisNeural",  # id-ID, Female, Indonesian (Indonesia), General
    "is-IS-GudrunNeural New",  # is-IS, Female, Icelandic (Iceland), General
    "is-IS-GunnarNeural New",  # is-IS, Male, Icelandic (Iceland), General
    "it-IT-DiegoNeural",  # it-IT, Male, Italian (Italy), General
    "it-IT-ElsaNeural",  # it-IT, Female, Italian (Italy), General
    "it-IT-IsabellaNeural",  # it-IT, Female, Italian (Italy), General
    "ja-JP-KeitaNeural",  # ja-JP, Male, Japanese (Japan), General
    "ja-JP-NanamiNeural",  # ja-JP, Female, Japanese (Japan), General
    "jv-ID-DimasNeural",  # jv-ID, Male, Javanese (Indonesia), General
    "jv-ID-SitiNeural",  # jv-ID, Female, Javanese (Indonesia), General
    "kk-KZ-AigulNeural New",  # kk-KZ, Female, Kazakh (Kazakhstan), General
    "kk-KZ-DauletNeural New",  # kk-KZ, Male, Kazakh (Kazakhstan), General
    "km-KH-PisethNeural",  # km-KH, Male, Khmer (Cambodia), General
    "km-KH-SreymomNeural",  # km-KH, Female, Khmer (Cambodia), General
    "kn-IN-GaganNeural New",  # kn-IN, Male, Kannada (India), General
    "kn-IN-SapnaNeural New",  # kn-IN, Female, Kannada (India), General
    "ko-KR-InJoonNeural",  # ko-KR, Male, Korean (Korea), General
    "ko-KR-SunHiNeural",  # ko-KR, Female, Korean (Korea), General
    "lo-LA-ChanthavongNeural New",  # lo-LA, Male, Lao (Laos), General
    "lo-LA-KeomanyNeural New",  # lo-LA, Female, Lao (Laos), General
    "lt-LT-LeonasNeural",  # lt-LT, Male, Lithuanian (Lithuania), General
    "lt-LT-OnaNeural",  # lt-LT, Female, Lithuanian (Lithuania), General
    "lv-LV-EveritaNeural",  # lv-LV, Female, Latvian (Latvia), General
    "lv-LV-NilsNeural",  # lv-LV, Male, Latvian (Latvia), General
    "mk-MK-AleksandarNeural New",  # mk-MK, Male, Macedonian (Republic of North Macedonia), General
    "mk-MK-MarijaNeural New",  # mk-MK, Female, Macedonian (Republic of North Macedonia), General
    "ml-IN-MidhunNeural New",  # ml-IN, Male, Malayalam (India), General
    "ml-IN-SobhanaNeural New",  # ml-IN, Female, Malayalam (India), General
    "mr-IN-AarohiNeural",  # mr-IN, Female, Marathi (India), General
    "mr-IN-ManoharNeural",  # mr-IN, Male, Marathi (India), General
    "ms-MY-OsmanNeural",  # ms-MY, Male, Malay (Malaysia), General
    "ms-MY-YasminNeural",  # ms-MY, Female, Malay (Malaysia), General
    "mt-MT-GraceNeural",  # mt-MT, Female, Maltese (Malta), General
    "mt-MT-JosephNeural",  # mt-MT, Male, Maltese (Malta), General
    "my-MM-NilarNeural",  # my-MM, Female, Burmese (Myanmar), General
    "my-MM-ThihaNeural",  # my-MM, Male, Burmese (Myanmar), General
    "nb-NO-FinnNeural",  # nb-NO, Male, Norwegian (Bokmål, Norway), General
    "nb-NO-IselinNeural",  # nb-NO, Female, Norwegian (Bokmål, Norway), General
    "nb-NO-PernilleNeural",  # nb-NO, Female, Norwegian (Bokmål, Norway), General
    "nl-BE-ArnaudNeural",  # nl-BE, Male, Dutch (Belgium), General
    "nl-BE-DenaNeural",  # nl-BE, Female, Dutch (Belgium), General
    "nl-NL-ColetteNeural",  # nl-NL, Female, Dutch (Netherlands), General
    "nl-NL-FennaNeural",  # nl-NL, Female, Dutch (Netherlands), General
    "nl-NL-MaartenNeural",  # nl-NL, Male, Dutch (Netherlands), General
    "pl-PL-AgnieszkaNeural",  # pl-PL, Female, Polish (Poland), General
    "pl-PL-MarekNeural",  # pl-PL, Male, Polish (Poland), General
    "pl-PL-ZofiaNeural",  # pl-PL, Female, Polish (Poland), General
    "ps-AF-GulNawazNeural New",  # ps-AF, Male, Pashto (Afghanistan), General
    "ps-AF-LatifaNeural New",  # ps-AF, Female, Pashto (Afghanistan), General
    "pt-BR-AntonioNeural",  # pt-BR, Male, Portuguese (Brazil), General
    "pt-BR-FranciscaNeural",  # pt-BR, Female, Portuguese (Brazil), General, multiple voice styles available using SSML
    "pt-PT-DuarteNeural",  # pt-PT, Male, Portuguese (Portugal), General
    "pt-PT-FernandaNeural",  # pt-PT, Female, Portuguese (Portugal), General
    "pt-PT-RaquelNeural",  # pt-PT, Female, Portuguese (Portugal), General
    "ro-RO-AlinaNeural",  # ro-RO, Female, Romanian (Romania), General
    "ro-RO-EmilNeural",  # ro-RO, Male, Romanian (Romania), General
    "ru-RU-DariyaNeural",  # ru-RU, Female, Russian (Russia), General
    "ru-RU-DmitryNeural",  # ru-RU, Male, Russian (Russia), General
    "ru-RU-SvetlanaNeural",  # ru-RU, Female, Russian (Russia), General
    "si-LK-SameeraNeural New",  # si-LK, Male, Sinhala (Sri Lanka), General
    "si-LK-ThiliniNeural New",  # si-LK, Female, Sinhala (Sri Lanka), General
    "sk-SK-LukasNeural",  # sk-SK, Male, Slovak (Slovakia), General
    "sk-SK-ViktoriaNeural",  # sk-SK, Female, Slovak (Slovakia), General
    "sl-SI-PetraNeural",  # sl-SI, Female, Slovenian (Slovenia), General
    "sl-SI-RokNeural",  # sl-SI, Male, Slovenian (Slovenia), General
    "so-SO-MuuseNeural",  # so-SO, Male, Somali (Somalia), General
    "so-SO-UbaxNeural",  # so-SO, Female, Somali (Somalia), General
    "sr-RS-NicholasNeural New",  # sr-RS, Male, Serbian (Serbia, Cyrillic), General
    "sr-RS-SophieNeural New",  # sr-RS, Female, Serbian (Serbia, Cyrillic), General
    "su-ID-JajangNeural",  # su-ID, Male, Sundanese (Indonesia), General
    "su-ID-TutiNeural",  # su-ID, Female, Sundanese (Indonesia), General
    "sv-SE-HilleviNeural",  # sv-SE, Female, Swedish (Sweden), General
    "sv-SE-MattiasNeural",  # sv-SE, Male, Swedish (Sweden), General
    "sv-SE-SofieNeural",  # sv-SE, Female, Swedish (Sweden), General
    "sw-KE-RafikiNeural",  # sw-KE, Male, Swahili (Kenya), General
    "sw-KE-ZuriNeural",  # sw-KE, Female, Swahili (Kenya), General
    "sw-TZ-DaudiNeural",  # sw-TZ, Male, Swahili (Tanzania), General
    "sw-TZ-RehemaNeural",  # sw-TZ, Female, Swahili (Tanzania), General
    "ta-IN-PallaviNeural",  # ta-IN, Female, Tamil (India), General
    "ta-IN-ValluvarNeural",  # ta-IN, Male, Tamil (India), General
    "ta-LK-KumarNeural",  # ta-LK, Male, Tamil (Sri Lanka), General
    "ta-LK-SaranyaNeural",  # ta-LK, Female, Tamil (Sri Lanka), General
    "ta-SG-AnbuNeural",  # ta-SG, Male, Tamil (Singapore), General
    "ta-SG-VenbaNeural",  # ta-SG, Female, Tamil (Singapore), General
    "te-IN-MohanNeural",  # te-IN, Male, Telugu (India), General
    "te-IN-ShrutiNeural",  # te-IN, Female, Telugu (India), General
    "th-TH-AcharaNeural",  # th-TH, Female, Thai (Thailand), General
    "th-TH-NiwatNeural",  # th-TH, Male, Thai (Thailand), General
    "th-TH-PremwadeeNeural",  # th-TH, Female, Thai (Thailand), General
    "tr-TR-AhmetNeural",  # tr-TR, Male, Turkish (Turkey), General
    "tr-TR-EmelNeural",  # tr-TR, Female, Turkish (Turkey), General
    "uk-UA-OstapNeural",  # uk-UA, Male, Ukrainian (Ukraine), General
    "uk-UA-PolinaNeural",  # uk-UA, Female, Ukrainian (Ukraine), General
    "ur-IN-GulNeural",  # ur-IN, Female, Urdu (India), General
    "ur-IN-SalmanNeural",  # ur-IN, Male, Urdu (India), General
    "ur-PK-AsadNeural",  # ur-PK, Male, Urdu (Pakistan), General
    "ur-PK-UzmaNeural",  # ur-PK, Female, Urdu (Pakistan), General
    "uz-UZ-MadinaNeural",  # uz-UZ, Female, Uzbek (Uzbekistan), General
    "uz-UZ-SardorNeural",  # uz-UZ, Male, Uzbek (Uzbekistan), General
    "vi-VN-HoaiMyNeural",  # vi-VN, Female, Vietnamese (Vietnam), General
    "vi-VN-NamMinhNeural",  # vi-VN, Male, Vietnamese (Vietnam), General
    "zh-CN-XiaochenNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), Optimized for spontaneous conversation
    "zh-CN-XiaohanNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), General, multiple styles available using SSML
    "zh-CN-XiaomoNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), General, multiple role-play and styles available using SSML
    "zh-CN-XiaoqiuNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), Optimized for narrating
    "zh-CN-XiaoruiNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), Senior voice, multiple styles available using SSML
    "zh-CN-XiaoshuangNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), Child voice，optimized for child story and chat; multiple voice styles available using SSML
    "zh-CN-XiaoxiaoNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), General, multiple voice styles available using SSML
    "zh-CN-XiaoxuanNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), General, multiple role-play and styles available using SSML
    "zh-CN-XiaoyanNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), Optimized for customer service
    "zh-CN-XiaoyouNeural",  # zh-CN, Female, Chinese (Mandarin, Simplified), Child voice, optimized for story narrating
    "zh-CN-YunxiNeural",  # zh-CN, Male, Chinese (Mandarin, Simplified), General, multiple styles available using SSML
    "zh-CN-YunyangNeural",  # zh-CN, Male, Chinese (Mandarin, Simplified), Optimized for news reading, multiple voice styles available using SSML
    "zh-CN-YunyeNeural",  # zh-CN, Male, Chinese (Mandarin, Simplified), Optimized for story narrating, multiple role-play and styles available using SSML
    "zh-HK-HiuGaaiNeural",  # zh-HK, Female, Chinese (Cantonese, Traditional), General
    "zh-HK-HiuMaanNeural",  # zh-HK, Female, Chinese (Cantonese, Traditional), General
    "zh-HK-WanLungNeural",  # zh-HK, Male, Chinese (Cantonese, Traditional), General
    "zh-TW-HsiaoChenNeural",  # zh-TW, Female, Chinese (Taiwanese Mandarin), General
    "zh-TW-HsiaoYuNeural",  # zh-TW, Female, Chinese (Taiwanese Mandarin), General
    "zh-TW-YunJheNeural",  # zh-TW, Male, Chinese (Taiwanese Mandarin), General
    "zu-ZA-ThandoNeural",  # zu-ZA, Female, Zulu (South Africa), General
    "zu-ZA-ThembaNeural",  # zu-ZA, Male, Zulu (South Africa), General
]

SUPPORTED_OUTPUT_FORMATS: Final[list[str]] = ["mp3", "ogg_vorbis", "pcm"]

SUPPORTED_FREQUENCIES: Final[list[str]] = [
    '16KHz',
    '24KHz',
    '48KHz'
]

# https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-speech/azure.cognitiveservices.speech.speechsynthesisoutputformat?view=azure-python
SUPPORTED_FORMAT_FREQUENCY_MAP: Final[dict[Tuple[str, str], str]] = {
    ('mp3', '16KHz'): 'Audio16Khz128KBitRateMonoMp3',
    ('mp3', '24KHz'): 'Audio24Khz160KBitRateMonoMp3',
    ('mp3', '48KHz'): 'Audio48Khz192KBitRateMonoMp3',

    ('ogg_vorbis', '16KHz'): 'Ogg16Khz16BitMonoOpus',
    ('ogg_vorbis', '24KHz'): 'Ogg24Khz16BitMonoOpus',
    ('ogg_vorbis', '48KHz'): 'Ogg48Khz16BitMonoOpus',

    ('pcm', '16KHz'): 'Raw16Khz16BitMonoPcm',
    ('pcm', '24KHz'): 'Raw24Khz16BitMonoPcm',
    ('pcm', '48KHz'): 'Raw48Khz16BitMonoPcm',
}

SUPPORTED_TEXT_TYPES: Final[list[str]] = ["text", "ssml"]


DEFAULT_LANGUAGE: Final = "en-US"
DEFAULT_OUTPUT_FORMAT: Final = "pcm"
DEFAULT_FREQUENCY: Final = "48KHz"
DEFAULT_TEXT_TYPE: Final = "text"

