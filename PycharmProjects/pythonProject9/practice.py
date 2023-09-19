a= b'h\x65llo'
print(list(a)) # byte
print(a) # str

a = 'a\u0300 propos'
print(list(a)) # unicode
print(a)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


