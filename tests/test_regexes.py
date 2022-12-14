# Adapted from commonregex-improved/test_cregex_improved.py

import re
import crim as cregex

SAMPLE_DATA = {
    "phone": [
        "12345678900",
        "1234567890",
        "+1 234 567 8900",
        "234-567-8900",
        "1-234-567-8900",
        "1.234.567.8900",
        "5678900",
        "567-8900",
        "(003) 555-1212",
        "+41 22 730 5989",
        "+442345678900",
    ],
    "phone_ext": [
        "(523)222-8888 ext 527",
        "(523)222-8888x623",
        "(523)222-8888 x623",
        "(523)222-8888 x 623",
        "(523)222-8888EXT623",
        "523-222-8888EXT623",
        "(523) 222-8888 x 623",
    ],
    "email": [
        "john.smith@gmail.com",
        "john_smith@gmail.com",
        "john@example.net",
        "John@example.net",
        "jane@example.gov.us",
    ],
    "ip": ["127.0.0.1", "192.168.1.1", "8.8.8.8", "192.30.253.113", "216.58.194.46"],
    "ipv6": [
        "fe80:0000:0000:0000:0204:61ff:fe9d:f156",
        "fe80:0:0:0:204:61ff:fe9d:f156",
        "fe80::204:61ff:fe9d:f156",
        "fe80:0000:0000:0000:0204:61ff:254.157.241.86",
        "fe80:0:0:0:0204:61ff:254.157.241.86",
        "::1",
    ],
    "credit-card": [
        "0000-0000-0000-0000",
        "0123456789012345",
        "0000 0000 0000 0000",
        "012345678901234",
        # visa
        "4111 1111 1111 1111",
        "4222 2222 2222 2222",
        # Mastercard
        "5500 0000 0000 0004",
        "5500 3334 0000 1234",
    ],
    "btc address": [
        "1LgqButDNV2rVHe9DATt6WqD8tKZEKvaK2",
        "19P6EYhu6kZzRy9Au4wRRZVE8RemrxPbZP",
        "1bones8KbQge9euDn523z5wVhwkTP3uc1",
        "1Bow5EMqtDGV5n5xZVgdpRPJiiDK6XSjiC",
    ],
    "address": ["101 main st.", "504 parkwood drive", "3 elm boulevard", "500 elm street "],
    "po box": ["PO Box 123456", "p.o. box 234234"],
    "ssn": ["000-00-0000", "111-11-1111", "222-22-2222", "123-45-6789"],
    "mac": ["f8:2f:a4:fe:76:d2", "F8:2F:A4:FE:76:D2", "3D-F2-C9-A6-B3-4F"],
}


def test_cregex_dates():
    # Test local scan

    # Test db query scan, per database
    ...
