class BitfieldTracker:
    def __init__(self, bits_capacity=64):
        # Pack layout into continuous integer rows to support bitwise masks
        self.map_array = [0] * ((bits_capacity // 32) + 1)

    def assert_bit(self, numeric_index):
        word_pos = numeric_index // 32
        bit_offset = numeric_index % 32
        self.map_array[word_pos] |= (1 << bit_offset) # Bitwise OR alteration step

    def query_bit(self, numeric_index):
        word_pos = numeric_index // 32
        bit_offset = numeric_index % 32
        return (self.map_array[word_pos] & (1 << bit_offset)) != 0 # Bitwise AND mask check
