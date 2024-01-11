import random
from datetime import datetime

def generate_random_numbers(timestamp_str, count=48):
    # Convert the timestamp string to a datetime object
    timestamp_format = "%Y-%m-%d-%H-%M-%S"
    datetime_obj = datetime.strptime(timestamp_str, timestamp_format)

    # Convert the datetime object to a Unix timestamp
    unix_timestamp = int(datetime_obj.timestamp())

    # Seed the random number generator
    rrr = random.Random(unix_timestamp)
    #print(random.getstate())

    # Generate 'count' random numbers
    return [rrr.randint(2**32) for _ in range(count)]

# Example usage
timestamp_str = "2023-11-18-05-17-36"  # Replace with the specific timestamp you have
random_numbers = generate_random_numbers(timestamp_str)
lis = [2646640425,    2746813182,    1743432795,    1021251219,    1084464634,    3005406808,    120085451,    4098370039,    4239654846,    2374266066,    3157706339,    464293212,    1671881348,    3089202849,    1640219769,    500263082,    1277795133,    1292667967,    891939749,    3378687589,    3419509284,    810232454,    3509227928,    644185118,    895672276,    885548957,    2175259006,    775160507,    65162173,    1356090588,    1083583849,    751699253,    2895595219,    3539243876,    2115642774,    4102247480,    1904660127,    447074290,    3761567579,    355307341,    1106644708,    910875738,    865615682,    2351071191,    841845359,    3206051877,    1684463401,    3648377826]
r = random.setstate(lis)
print(random.getstate())
if any(x in lis for x in random_numbers):
    print("yes")
#print(random_numbers)
