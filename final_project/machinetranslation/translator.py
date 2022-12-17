import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = "17-12-2022"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    if english_text is None:
        return ""
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        phrase = translation["translations"][0]["translation"]
    except ApiException as ex:
        phrase = ""
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)

    return phrase

def french_to_english(french_text):
    if french_text is None:
        return ""
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        phrase = translation["translations"][0]["translation"]
    except ApiException as ex:
        phrase = ""
        print("Method failed with status code " +
              str(ex.code) + ": " + ex.message)

    return phrase