import hashlib

class PrivacyService:
    @staticmethod
    def anonymize_reporter(name: str) -> str:
        if not name or name.strip() == "":
            return "Anonymous Responder"
        # Create a consistent but private ID
        return f"User_{hashlib.md5(name.encode()).hexdigest()[:8]}"

    @staticmethod
    def get_public_coords(lat: float, lng: float):
        """Fuzz coordinates for public map safety."""
        return round(lat, 3), round(lng, 3)
