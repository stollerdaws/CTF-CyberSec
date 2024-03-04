import base64

class Dill:
    prefix = 'sun{'
    suffix = '}'
    o = [5, 1, 3, 4, 7, 2, 6, 0]

    def __init__(self):
        self.encrypted = 'bGVnbGxpaGVwaWNrdD8Ka2V0ZXRpZGls'

    def reverse_order(self, encrypted_blocks):
        # Create an empty list of the same size as encrypted_blocks
        original_order = [''] * len(encrypted_blocks)

        # Populate original_order based on the ordering in `o`
        for i, position in enumerate(Dill.o):
            original_order[position] = encrypted_blocks[i]
        
        return original_order

    def get_flag(self):
        # Split the encrypted string into blocks of 4 characters each
        encrypted_blocks = [self.encrypted[i:i + 4] for i in range(0, len(self.encrypted), 4)]
        
        # Get the blocks in their original order
        original_blocks = self.reverse_order(encrypted_blocks)
        
        # Combine the blocks
        encrypted_combined = ''.join(original_blocks)
        
        # Decode the base64 value
        decoded_value = base64.b64decode(encrypted_combined).decode('utf-8')
        
        # Return the full flag
        return Dill.prefix + decoded_value + Dill.suffix

dill = Dill()
print(dill.get_flag())

