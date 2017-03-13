from vigenere_cipher import VigenereCipher
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
        encoded = cipher.encoded("ENCODED IN PYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    @staticmethod
    def test_encode_lowercase():
        cipher = VigenereCipher("TRain")
        encoded = cipher.encoded("encoded in Python")
        assert encoded == "XECWQXUIVCRKHWA"

    @staticmethod
    def test_combine_character():
        assert VigenereCipher.combine_character("E", "T") == "X"
        assert VigenereCipher.combine_character("N", "R") == "E"

    @staticmethod
    def test_extend_keyword():
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

    @staticmethod
    def test_separate_character():
        assert VigenereCipher.separate_character("X", "T") == "E"
        assert VigenereCipher.separate_character("E", "R") == "N"

    @staticmethod
    def test_decode():
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"


if __name__ == '__main__':
    unittest.main()
