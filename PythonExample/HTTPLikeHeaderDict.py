#Normal Header keys to lowercase for lookup.

headers = {"content-Type":"text/plain", "Accept":"*/*"}
normalized = {k.lower(): v for k, v in headers.items()}
if __name__ == '__main__':
    print (normalized.get("content-type"))