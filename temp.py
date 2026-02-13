import markstore

EXPECTED = {
    "Key1":
    "My Data",
    "Data": [{
        "Subkey1": "Subdata"
    }, {
        "Subkey2": {
            "Subkey2.1": "Subdata2.1",
            "Subkey2.2": "Subdata2.2"
        }
    }],
    "Key2":
    "Other data"
}

x = markstore.dumps(EXPECTED)
x = x.replace(" ", ".")
print(x)
