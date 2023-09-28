from math import sin, pi
import tqdm

ct = b"\xca\xae`fg\x94\x88d\xfe'ut|\x1a\x11_\xd4\xc2UmK\xb4\xcf_\x13\x1dy_\x87\x1a\x00_\xd5\xb3MnK\xbe\xd8i\x0c\x14}ns)\x07e\xc0\x8ei"

for key in tqdm.tqdm(range(2**32)):
    pt = bytes((c - k)%256 for c, k in zip(ct, (int(256*sin(key*(i+1)/256*pi)) for i in range(len(ct)))))
    if b"ictf" in pt:
        print(pt)
        break