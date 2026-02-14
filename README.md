# markstore
Markdown as plain-text data storage

## But Why?
Why use this when there are numerous alternatives for data storage and serialization?  
Check if your use-case meets the following criteria:

1) Primarily human readable (not necessarily, writable) plain-text, especially for non-programmers
2) Easy consumption by version control
3) Easy export, or a desire to prevent vendor lock-in to your application

### What this is
A simple, json-like interface to serialize basic objects to and from a markdown file.

### What this isn't
- A generic markdown processing/generator tool
- A configuration language

It is a non-goal of this library to be tolerant of human error.
The intended use case is **machine-to-machine serialization** and the occasional export
to a human.

## Example

### To File
```py
import markstore

# Serialize
myObject = {
    "myKey": "myData"
}

with open("out.md", mode='wb') as f:
    markstore.dump(myObject, f)

# Deserialize
with open("out.md", mode='rb') as f:
    myObject = markstore.load(f)

```

### To String
```py
import markstore

# Serialize
myObject = {
    "myKey": "myData"
}

myStr = markstore.dumps(myObject)

# Deserialize
myObject = markstore.loads(myStr)

```



## Markdown Object Specification

### Lists
```py
["one", "two", "three", ["four", "five"], "six"]
```
Translates to 

```md
- one
- two
- three
- - four
  - five
- six
```

### Dicts
```py
{
    "key1": "data1",
    "key2": "data2",
    "key3": { 
        "subkey1": "subdata1",
        "subkey2": "subdata2"
        }
}
```

Translates to 

```md
# key1
data1
# key2
data2
# key3
## subkey1
subdata1
## subkey2
subdata2
```

### Combinations
```py
{
    "Key1":
    "My Data",
    "Data": [{
        "Subkey1": "Subdata1"
    }, {
        "Subkey2": {
            "Subkey2.1": "Subdata2.1",
            "Subkey2.2": "Subdata2.2"
        }
    }],
    "Key2":
    "Other data"
}
```

```md
# Key1
My Data
# Data
- ## Subkey1
  Subdata1
- ## Subkey2
  ### Subkey2.1
  Subdata2.1
  ### Subkey2.2
  Subdata2.2
# Key2
Other data
```

**Inner dictionary keys are always prefixed by an increasing number of `#`, even if the key is within a list**