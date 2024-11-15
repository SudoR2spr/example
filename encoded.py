import base64

# Base64 encoded code
encoded_code = b"ZGVmIGRvdWJsZV9udW1iZXIobik6CiAgICByZXR1cm4gbiAqIDIKCm51bWJlciA9IDUKcmVzdWx0ID0gZG91YmxlX251bWJlcihudW1iZXIpCnByaW50KGYiVGhlIGRvdWJsZSBvZiB7bnVtYmVyfSBpcyB7cmVzdWx0fSIp"

# Base64 decode
decoded_code = base64.b64decode(encoded_code).decode('utf-8')

# Execute the decoded code
exec(decoded_code)
