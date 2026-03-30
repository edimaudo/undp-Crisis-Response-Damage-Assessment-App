class TranslationService:
    # The 6 core languages for the Crisis and Damage Response Assessment
    SUPPORTED_LANGUAGES = {
        "en": "English",
        "ar": "العربية",
        "fr": "Français",
        "es": "Español",
        "sw": "Kiswahili",
        "pt": "Português"
    }

    # RTL logic specifically for Arabic
    @staticmethod
    def is_rtl(lang: str) -> bool:
        return lang == "ar"

    @classmethod
    def get_ui_labels(cls, lang: str = "en"):
        """
        Returns a dictionary of labels for the report_form.html 
        based on the 6 supported languages.
        """
        labels = {
            "en": {"submit": "Submit Report", "location": "Location", "photo": "Take Photo"},
            "ar": {"submit": "إرسال التقرير", "location": "الموقع", "photo": "التقاط صورة"},
            "fr": {"submit": "Soumettre", "location": "Emplacement", "photo": "Prendre une photo"},
            "es": {"submit": "Enviar", "location": "Ubicación", "photo": "Tomar foto"},
            "sw": {"submit": "Wasilisha", "location": "Mahali", "photo": "Piga Picha"},
            "pt": {"submit": "Enviar", "location": "Localização", "photo": "Tirar Foto"}
        }
        return labels.get(lang, labels["en"])
