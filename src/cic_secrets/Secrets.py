import requests
from time import sleep

from .ciphers import decrypt_caesar, decrypt_substitution


class Secrets:

    def __init__(self) -> None:

        import os
        from dotenv import load_dotenv
        load_dotenv()

        self.api = os.getenv("API")
        self.api_key = os.getenv("API_KEY")

    def cipher_type(self):

        url = f"{self.api}/cipher_type"
        headers = {'x-api-key': self.api_key}

        print(url)
        print(headers)
        print(self.api, self.api_key)

        print(f"\nGetting cipher from /cipher_type...")

        while True:
            try:
                r = requests.get(url=url, headers=headers)
                if r.status_code != 200:
                    raise ValueError(f"{r.status_code}")
                break
            except ValueError as e:
                if r.status_code == 429:
                    print("Too many requests! Stopping program...")
                    exit()

                print(f"Error: retrying...")
                sleep(0.1)

        cipher = r.json()['cipher']

        print(f"Cipher: {cipher}")

        return cipher

    def get_encrypted_text(self, cipher: str) -> tuple[str, str, list[str]]:

        if cipher not in ("CAESAR", "SUBSTITUTION"):
            raise ValueError(f"{cipher} is not a valid cipher!")

        url = f"{self.api}/get_encrypted_text"
        headers = {'x-api-key': self.api_key}
        params = {'cipher': cipher}

        print(f"\nGetting encrypted matrix from /get_encrypted_text...")

        r = requests.get(url=url, headers=headers, params=params).json()

        cipher, key, texts = r['cipher'], r['key'], r['encrypted_matrix']

        print("Encrypted matrix:")

        for text in texts:
            print(f"{text}")

        print("Cipher:", cipher, '-', "Key:", key)

        return (cipher, key, texts)

    def decrypt_text(self, encrypted_matrix: tuple[str, str, list[str]]) -> str:

        cipher, key, texts = encrypted_matrix

        decryption = decrypt_caesar if cipher == "CAESAR" else decrypt_substitution

        diagonal = ''.join(
            decryption(
                decryption(
                    texts[i][i], key
                ), key
            ) for i in range(10)
        )

        print(f"\nDiagonal: {diagonal}")

        return diagonal

    def verify_diagonal(self, diagonal: str) -> str:

        url = f"{self.api}/verify_diagonal"
        headers = {'x-api-key': self.api_key}
        body = {'diagonal': diagonal}

        print(f"\nVerifying diagonal from /verify_diagonal...")

        image = requests\
            .post(url=url, headers=headers, json=body)\
            .json()['response_image']

        print(f"\nBASE64 Image: {image[:10]} {'.'*8} {image[-10:]}")

        return image

    def diplay_image(self, image: str) -> None:
        from PIL import Image
        from io import BytesIO
        from base64 import b64decode

        print("Displaying image...\n")

        Image.open(BytesIO(b64decode(image))).show()
