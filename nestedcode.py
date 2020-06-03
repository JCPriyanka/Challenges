def parse(obj, key):
    kl = key.split('/')
    for k in kl:
        try:
            obj = obj[k]
        except Exception:
            raise Exception("Key not found")
    return obj

if __name__ == "__main__":
    o = {"a":{"b":{"c":"d"}}}
    k = "a/b/c"
    print(parse(o, k))