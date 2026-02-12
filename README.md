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

