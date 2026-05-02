from fastapi import Request

def get_locale(request: Request):
    return request.cookies.get("lang", "en")
