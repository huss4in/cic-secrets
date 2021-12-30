import pytest

from cic_secrets.ciphers import decrypt_caesar, decrypt_substitution


def test_decrypt_caesar():

    assert decrypt_caesar("B", 1) == "A"

    assert decrypt_caesar("A", 1) == "Z"

    assert decrypt_caesar("Z", 1) == "Y"

    assert decrypt_caesar("BCD", 1) == "ABC"

    assert decrypt_caesar("VUGXKDUHRI", 10) == "LKWNATKXHY"


def test_decrypt_substitution():

    assert decrypt_substitution("Q", "NQXPOMAFTRHLZGECYJIUWSKDVB") == "B"

    assert decrypt_substitution("B", "NQXPOMAFTRHLZGECYJIUWSKDVB") == "Z"

    assert decrypt_substitution("N", "NQXPOMAFTRHLZGECYJIUWSKDVB") == "A"

    assert decrypt_substitution("NQX", "NQXPOMAFTRHLZGECYJIUWSKDVB") == "ABC"
