
import hashlib
import secrets
import random
import pickle
from pyope.ope import OPE, ValueRange

class RangeGrader:
    """
    A class for grading numerical answers within a given range using Order-Preserving Encryption (OPE).

    Attributes:
        lower_bound (int): Encrypted lower bound for grading.
        upper_bound (int): Encrypted upper bound for grading.
        key (bytes): OPE key.
        cipher (OPE): OPE cipher object.
        salt (int): Random salt for encryption.
    """

    def __init__(self, lower_bound : int, upper_bound : int, scale : float = 1.0):
        """
        Initialize a new RangeGrader object.

        Parameters:
            lower_bound (int): The lower bound for grading.
            upper_bound (int): The upper bound for grading.
            scale (float, optional): The scaling factor for the bounds. Default is 1.0.
        """

        lower_bound = int(lower_bound / scale)
        upper_bound = int(upper_bound / scale)
        offset = upper_bound - lower_bound
        self.scale = scale

        self.salt = random.randint(0, 2**128 - 1 - offset)

        self.key = OPE.generate_key(block_size=256//8)
        self.cipher = OPE(
            self.key,
            in_range=ValueRange(0, 2**128 - 1),
            out_range=ValueRange(0, 2**256-1)
        )

        lb_m1 = self.cipher.encrypt(lower_bound+self.salt-1)
        lb_p1 = self.cipher.encrypt(lower_bound+self.salt+1)

        self.lower_bound = random.randint(lb_m1, lb_p1)

        ub_m1 = self.cipher.encrypt(upper_bound+self.salt-1)
        ub_p1 = self.cipher.encrypt(upper_bound+self.salt+1)

        self.upper_bound = random.randint(ub_m1, ub_p1)

    def grade(self, value : int):
        """
        Grade a numerical answer.

        Parameters:
            value (int): The value to be graded.
        """
        scaled_value = int(value / self.scale)
        grade = self.cipher.encrypt(scaled_value+self.salt) < self.upper_bound and self.cipher.encrypt(scaled_value+self.salt) > self.lower_bound

        if grade:

            print(f"{value} is correct")
        
        else:

            print(f"{value} is incorrect")

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

class ChoiceGrader:
    """
    A class for grading choice answers using hashed values.

    Attributes:
        choices (dict): Mapping of choices to their indices.
        correct_hash (str): Hash of the correct answer.
        salt (str): Salt used for hashing.
    """
    
    def __init__(self, correct):
        """
        Initialize a new Grader object.

        Parameters:
            choices (list): The list of available choices.
            correct (str): The correct choice.
        """
        self.salt = secrets.token_hex(16)  # Generating a secure random salt
        self.correct_hash = self._hash_value(correct)

    def _hash_value(self, value: str) -> str:
        """
        Hash a given value with salt.

        Parameters:
            value (str): The value to be hashed.

        Returns:
            str: The hashed value as a hexadecimal string.
        """
        m = hashlib.sha256()
        m.update((value + self.salt).encode('utf-8'))
        return m.hexdigest()

    def grade(self, value: str):
        """
        Grade a choice answer.

        Parameters:
            value (str): The value to be graded.
        """
        if self._hash_value(value) == self.correct_hash:
            print(f"{value} is correct")
        else:
            print(f"{value} is incorrect")

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)