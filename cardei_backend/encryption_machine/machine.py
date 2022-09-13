import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

fields_exempt_from_encryption = [
    'date_creation',
    'date_update',
    'archived',
    'tag',
    'category',
    'user',
    'id'
]


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(pad(raw.encode(), self.bs))).decode()

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[AES.block_size:]), self.bs).decode()

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


class CardeiPycryptodome:
    def __init__(self, key):
        self.cipher_machine = AESCipher(key)

    def encrypt(self, raw):
        return self.cipher_machine.encrypt(raw)

    def decrypt(self, enc):
        return self.cipher_machine.decrypt(enc)

    def process_dict(self, data_raw: dict, action):
        data = {}
        action_dict = {
            'encrypt': self.encrypt,
            'decrypt': self.decrypt
        }
        for k, v in data_raw.items():
            if k in fields_exempt_from_encryption:
                data[k] = v
                continue

            action_func = action_dict[action]
            data[k] = action_func(v)

        return data


