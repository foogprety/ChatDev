'''
This file contains functions to translate the content to French.
'''
from googletrans import Translator
def translate_to_french(content):
    '''
    Translate the content to French.
    Args:
        content (str): The content to be translated.
    Returns:
        str: The translated content in French.
    '''
    translator = Translator()
    translated_content = translator.translate(content, dest='fr').text
    return translated_content