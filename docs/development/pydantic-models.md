---
title: "Pydantic models"
tags: python, development, data, models
author: Colm Britton
created: 2025/05/01
updated: 2025/05/01
---

Often used with Flask by Adam. So I thought I'd best understand it a bit more.

## What is a Pydantic model?

- It’s a Python class that knows how to **validate**, **parse**, and **serialise** data for you
- Under the hood, it checks that the data you give it matches the types you’ve declared

## Why use Pydantic?

1. **Automatic validation**
   You declare `age: int` and Pydantic will error if someone passes `"old"` instead of `42`

2. **Easy parsing**
   It converts simple things for you (e.g. strings to `datetime`, ints to `Decimal`)

3. **Easier to read code - clear schemas**
   Your code documents itself: other devs see exactly what shape your data should have.

4. **Fast serialisation**
   Dump your model to JSON or dict with a single call (`.model_dump()`)

## Basic example

Install
```
pip install pydantic
```

Define a model by inheriting from `BaseModel` and adding typed attributes:
```
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: int
    name: str
    signup_ts: date | None = None
```

Create an instance (it'll be validated)
```
# valid
u = User(id=123, name="Alice", signup_ts="2024-05-01")
assert isinstance(u.signup_ts, date)

# invalid: raises a clear error
User(id="nope", name="Bob")
# → ValidationError: id\n  value is not a valid integer
```

Inspect or serialise
```
u.dict()          # → {'id': 123, 'name': 'Alice', 'signup_ts': datetime.date(2024, 5, 1)}
u.json()          # → '{"id":123,"name":"Alice","signup_ts":"2024-05-01"}'
```
