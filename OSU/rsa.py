from ossapi import Ossapi
client_id = 30620
client_secret = 'EnUYcJgsL3aoJcDcF8JWsIqmBcIKm1I8yAT4OAY5'
api = Ossapi(client_id, client_secret)
def calculate_d(p, q, e):
    # Calculate n (not used in this function, but part of RSA)
    n = p * q

    # Calculate Euler's totient function φ(n)
    phi = (p - 1) * (q - 1)

    # Calculate d, the modular multiplicative inverse of e mod φ(n)
    # d * e % φ(n) = 1
    d = pow(e, -1, phi)

    return d

# Example usage:
p = 59644326261100157131
q = 99132954671935298039
e = 876603837240112836821145245971528442417

d = calculate_d(p, q, e)
print(f"The private key d is: {d}")

print(api.user(d, mode='osu').username)
print(api.user('Strellic'))
print(api.forum_topic(1883356))