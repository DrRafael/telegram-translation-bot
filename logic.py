from collections import defaultdict
from translate import Translator


class TextAnalysis:
    """Analyzes user text messages, maintains session memory, and provides translation services."""
    
    memory = defaultdict(list)
    preset_answers = {
        "what is your name": "I am an AI Translation Bot designed to assist you with language translation!",
        "how old are you": "Age is relative in the digital world!"
    }

    def __init__(self, text: str, owner: str):
        self.owner = owner
        self.text = text
        self.translation = self._translate(self.text, from_lang="ru", to_lang="en")
        
        # Check for preset FAQ responses or trigger default help text
        lowered_text = self.text.lower().strip()
        if lowered_text in self.preset_answers:
            self.response = self.preset_answers[lowered_text]
        else:
            self.response = self._get_default_answer()

        # Append instance to user memory history
        TextAnalysis.memory[self.owner].append(self)

    def _get_default_answer(self) -> str:
        """Returns translated default assistant response."""
        return self._translate("I am ready to help you translate or analyze your text.", from_lang="en", to_lang="ru")

    def _translate(self, text: str, from_lang: str, to_lang: str) -> str:
        """Translates input text between specified languages."""
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            return translator.translate(text)
        except Exception:
            return "Translation failed. Please try again."
