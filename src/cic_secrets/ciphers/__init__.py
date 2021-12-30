from string import ascii_uppercase

ALPHABET: str = ascii_uppercase


def decrypt_caesar(text: str, key: str) -> str:
    """
    # Decrypts a Caesar cipher.

    Args:
    ```py
        text: str  # Encrypted text.
        key: int   # Encryption key.
    ```
    Returns:
    ```py
        str  # Decrypted text.
    ```
    ---
    Examples:

    ###
    ```py
        decrypt_caesar('B', 1)
    ```
    ###
    ```py
    >>  A
    ```
    """

    return ''.join(ALPHABET[(ALPHABET.find(char) - int(key)) % 26] for char in text)


def decrypt_substitution(text: str, key: str) -> str:
    """
    # Decrypts a Substitution cipher.

    Args:
    ```py
        text: str  # Encrypted text.
        key: int   # Encryption key.
    ```
    Returns:
    ```py
        str  # Decrypted text.
    ```
    ---
    Examples:

    ###
    ```py
        decrypt_substitution('Q', "NQXPOMAFTRHLZGECYJIUWSKDVB")
    ```
    ###
    ```py
    >>  B
    ```
    """

    return ''.join(ALPHABET[key.find(char)] for char in text)
