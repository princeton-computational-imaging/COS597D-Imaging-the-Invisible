import os

def test_netid():
    with open('netid', 'r') as f:
        data = str(f.readline())
    assert (data != "NETID_GOES_HERE")