import hashlib
import re

class AnonymizationService:
    @staticmethod
    def mask_reporter_id(raw_id: str, salt: str = "undp_secure_2026") -> str:
        """
        Creates a deterministic but anonymous hash of a user's ID.
        Reasoning: Allows us to see if the same person sent 5 reports 
        without knowing WHO that person is.
        """
        if not raw_id:
            return "anon_user"
        hash_obj = hashlib.sha256(f"{raw_id}{salt}".encode())
        return f"uid_{hash_obj.hexdigest()[:12]}"

    @staticmethod
    def blur_location(lat: float, lon: float, precision: int = 3) -> tuple:
        """
        Reduces coordinate precision for public viewing.
        Reasoning: 3 decimal places (~110m) protects the exact house 
        location while showing the general affected neighborhood.
        """
        return round(lat, precision), round(lon, precision)

    @staticmethod
    def strip_pii_from_text(text: str) -> str:
        """
        Uses Regex to remove potential phone numbers or emails from notes.
        Reasoning: Users often accidentally type contact info in 'Notes'.
        """
        if not text:
            return ""
        # Basic pattern for emails and phone-like digits
        text = re.sub(r'\S+@\S+', '[EMAIL_REMOVED]', text)
        text = re.sub(r'\+?\d{10,13}', '[PHONE_REMOVED]', text)
        return text
