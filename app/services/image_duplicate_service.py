from PIL import Image
import imagehash

def compute_hash(file):
    img = Image.open(file)
    return str(imagehash.phash(img))

def is_duplicate(hash_val, existing):
    for h in existing:
        if imagehash.hex_to_hash(h) - imagehash.hex_to_hash(hash_val) < 5:
            return True
    return False
