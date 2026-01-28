---
title: "Normalised vs denormalised data"
tags: data, modelling, development
author: Colm Britton
created: 2026/01/28
updated: 2026/01/28
---

# Normalised vs denormalised data plain English explainer

This is a clear, plain English explanation of normalised and denormalised data, with examples that work both in everyday terms and in a planning data context.

---

## Normalised data

Normalised data means you store each fact once and then reference it from other places. Instead of repeating information, you split it into separate tables or entities and link them together.

The aim is to keep data tidy, consistent, and easy to maintain.

Normalised data is good when you care about:
- accuracy
- consistency
- long term maintenance
- modelling real world relationships

### Everyday example

Imagine a library system.

You keep authors in one place:

| author_id | name        | nationality |
|---------|------------|-------------|
| 17      | Zadie Smith | British     |

And books in another place:

| book_id | title       | author_id |
|-------|-------------|-----------|
| 202   | White Teeth | 17        |
| 406   | On Beauty   | 17        |

The author is stored once. Each book simply points to the author using an ID.

If the author details change, you update them in one place and everything stays consistent.

### Planning data example

This is similar to:
- storing authorities in one dataset
- storing application types in another
- storing conditions in another
- linking them together using identifiers

This approach is especially useful for decision stage data where relationships matter and the structure needs to reflect the real world.

---

## Denormalised data

Denormalised data means you put everything together in one place, even if that means repeating information. It is flattened and self contained so it can be read easily without looking anything up elsewhere.

The aim is convenience and speed.

Denormalised data is good when you care about:
- simplicity
- fast reads
- easy API payloads
- systems that cannot do joins

### Everyday example

Using the same library, you could store everything in one table:

| book_id | title       | author_name | nationality |
|-------|-------------|-------------|-------------|
| 202   | White Teeth | Zadie Smith | British     |
| 406   | On Beauty   | Zadie Smith | British     |

Here the author name appears multiple times. This is easier to read, but harder to maintain. If you need to correct something, you must change it in more than one place.

### Planning data example

This is similar to an application or decision payload where a single JSON object contains:
- the authority name
- the application reference
- site information
- proposal details
- conditions
- documents

It is convenient for data exchange, even if some of that information exists elsewhere in more structured datasets.

---

## Simple analogy

Normalised data is like a well organised kitchen:
- spices in one cupboard
- pans in another
- everything has its place

Denormalised data is like a takeaway delivery bag:
- fork, napkin, sauce, menu all together
- some items repeated across meals
- convenience over tidiness

---

## When to use normalised data

Use normalised data when you need:
- high data quality
- strong relationships between entities
- minimal duplication
- confidence that changes apply everywhere

In planning terms, this suits:
- decision modelling
- conditions and their life cycle
- appeals
- enforcement

---

## When to use denormalised data

Use denormalised data when you need:
- simple payloads
- fast reads
- easy integration
- flat structures for APIs and exports

In planning terms, this suits:
- API responses
- decision notice representations
- analytical tables
- data downloads

---

## Using both together

In most real systems, you use both.

Internally, data is usually normalised so it is accurate and well structured.

Externally, data is often denormalised so it is easy to consume.

### Example

Internally:
- Decision table
- Condition table
- Authority table
- Application table

All linked by identifiers.

Externally:

```
{
  "decision_id": "123",
  "authority_name": "Camden",
  "application_reference": "2024/1234",
  "conditions": [
    {
      "number": 1,
      "text": "Development must begin within three years",
      "trigger": "pre-commencement"
    }
  ]
}
```

The API response is denormalised for convenience, even though the underlying data model is normalised.

---

## One line summary

Normalised data is about correctness and structure.

Denormalised data is about convenience and speed.

Most good systems use both, each where it makes the most sense.
