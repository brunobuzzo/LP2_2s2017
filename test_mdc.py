def mdc(m,n):
    if m > n:
        mdc = m
    else:
        mdc = n
    while n % mdc != 0 or m % mdc != 0:
        mdc = mdc - 1
    return mdc

def test_mdc():
    print('mdc')
    assert mdc(16,24) == 8
    assert mdc(196,40) ==  4
    assert mdc(1120,525) ==  35
    assert mdc(352,416) ==  32
    assert mdc(288,360) ==  72
       