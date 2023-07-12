import hashlib
# Converting a string to hash value by passing to sha_256 function

def sha_256(text):
    if len(text)<1:
        return ''
    string = text.encode('utf-8')
    hash_val = hashlib.sha256(string).hexdigest()
    return hash_val


def sha_1(text):
    string = text.encode('utf-8')
    sha1_hash = hashlib.sha1(string).hexdigest()
    return sha1_hash

def md_5(text):
    string = text.encode('utf-8')
    md5_hash = hashlib.md5(string).hexdigest()
    return md5_hash