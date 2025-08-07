# JSON in Python: A Simple Tutorial

## 📘 What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write, and easy for machines to parse and generate.

In Python, the built-in `json` module allows us to work with JSON data easily.

---

## 📥 Importing the JSON Module

```python
import json
```

---

## 🔄 Converting Between Python and JSON

### Python Dictionary to JSON String

```python
import json

data = {"name": "Alice", "age": 30, "is_member": True}
json_string = json.dumps(data)

print(json_string)
# Output: {"name": "Alice", "age": 30, "is_member": true}
```

### JSON String to Python Dictionary

```python
json_str = '{"name": "Alice", "age": 30, "is_member": true}'
data = json.loads(json_str)

print(data)
# Output: {'name': 'Alice', 'age': 30, 'is_member': True}
```

---

## 💾 Storing JSON Data in a File

### Write JSON to a File

```python
data = {"project": "JSON Tutorial", "version": 1.0}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

### Read JSON from a File

```python
with open("data.json", "r") as f:
    data = json.load(f)

print(data)
```

---

## ⚙️ Using JSON for Configuration/Parameters

You can store app settings or parameters in a JSON file:

**config.json**
```json
{
    "api_key": "12345-ABCDE",
    "timeout": 30,
    "debug": true
}
```

### Load Configuration in Python

```python
with open("config.json") as f:
    config = json.load(f)

print(config["api_key"])  # Output: 12345-ABCDE
```

---

## 🧹 Summary

- Use `json.dumps()` and `json.loads()` to work with JSON strings.
- Use `json.dump()` and `json.load()` to work with JSON files.
- JSON is a great format for data exchange and parameter storage.

---

## 🛠️ Useful Tips

- JSON keys must be strings (in double quotes).
- JSON supports: strings, numbers, arrays (lists), booleans, and null (`None` in Python).

