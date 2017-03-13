from vigenere_cipher import VigenereCipher
from vigenere_cipher import combine_character
from vigenere_cipher import separate_character
import unittest


class TestSquareProcessing(unittest.TestCase):
    @staticmethod
    def test_encode():
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    @staticmethod
    def test_encode_character():
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        assert encoded == "X"

    @staticmethod
    def test_encode_spaces():
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    @staticmethod
    def test_encode_lowercase():
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        assert encoded == "XECWQXUIVCRKHWA"

    @staticmethod
    def test_combine_character():
        assert combine_character("E", "T") == "X"
        assert combine_character("N", "R") == "E"

    @staticmethod
    def test_extend_keyword():
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

    @staticmethod
    def test_separate_character():
        assert separate_character("X", "T") == "E"
        assert separate_character("E", "R") == "N"

    @staticmethod
    def test_decode():
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"


if __name__ == '__main__':
    unittest.main()
