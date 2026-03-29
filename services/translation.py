class TranslationService:
    @staticmethod
    def get_ui_direction(lang: str) -> str:
        return "rtl" if lang == "ar" else "ltr"

    @staticmethod
    def format_severity(level: str, lang: str = "en") -> str:
        # Simple mapping for localized labels
        labels = {
            "en": {"minor": "Minor Damage", "destroyed": "Total Destruction"},
            "ar": {"minor": "ضرر طفيف", "destroyed": "دمار كامل"}
        }
        return labels.get(lang, labels["en"]).get(level, level)
