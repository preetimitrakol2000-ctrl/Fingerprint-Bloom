from bit_vector import BitfieldTracker

class ProbabilisticFilter:
    def __init__(self, size=64):
        self.bitfield = BitfieldTracker(size)
        self.size = size

    def _hash_indices(self, item_string):
        """Calculates dual location positions using non-overlapping polynomial steps."""
        hash_1 = 0
        hash_2 = 5381
        for symbol in item_string:
            hash_1 = (hash_1 * 33 + ord(symbol)) % self.size
            hash_2 = (((hash_2 << 5) + hash_2) + ord(symbol)) % self.size
        return [hash_1, hash_2]

    def insert_signature(self, signature):
        for index in self._hash_indices(signature):
            self.bitfield.assert_bit(index)

    def check_existence(self, signature):
        for index in self._hash_indices(signature):
            if not self.bitfield.query_bit(index):
                return False # Confirmed out-of-bounds entity (No False Negatives)
        return True # Probable system match indicator
