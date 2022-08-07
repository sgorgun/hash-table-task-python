# Hash table (Python)

Set of programming assignments that are designed to test knowledge of hash table data structure.

## Problem 1: Implement HashTable with chaining

Implement a HashTable interface **without using any hash table libraries**.

The following building blocks are provided for you:

* Let us assume for this programming assignments that only integer numbers will be used as keys. `KeyValueData` wraps a (key, value) pair.
```python
# tasks/hash_table.py

class KeyValueData:
    """Data that will be stored in hash table.
    
    NOTE: no need to change this class.
    """
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value
```

* Each chain or bucket of `HashTable` will be be handled by `Bucket` class that has the following API:
```python
# tasks/hash_table.py

class Bucket:
    """Represents a set of (K,V) pairs that were assigned to the same bin/chain/bucket."""

    def __init__(self):
        self.elements: List[KeyValueData] = []

    def get(self, key: int) -> Optional[Any]:
        """Returns the value for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass

    def put(self, key: int, value: Any):
        """Puts a given (K,V) pair into the bucket."""
        pass

    def remove(self, key: int):
        """Removes the (K,V) pair for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass
```

* Main `HashTable` API:
```python
# tasks/hash_table.py

class HashTable:
    """Basic Hash Table interface."""

    def __init__(self, n_buckets: int = 100):
        self.n_buckets = n_buckets
        self.buckets = ... # Create #n_buckets Bucket objects.
    
    def h(self, key: int) -> int:
        # Here we use the simplest form of hash function.
        return key % self.n_buckets
    
    def set(self, key: int, value: Any):
        """Inserts a given (K,V) pair.
        
        NOTE: in case the key is already in the hash table - the value should be replaced.
        """
        pass
    
    def get(self, key: int) -> Optional[Any]:
        """Returns the value for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass
    
    def remove(self, key: int):
        """Removes the (K,V) pair for a given key.
        
        Raises:
            ValueError: If no corresponding (K,V) is found.
        """
        pass
```

**Example:**

```python
hash_table = HashTable(n_buckets=3)
hash_table.set(0, 'hello') # 0 bucket
hash_table.set(1, 'world') # 1 bucket
assert hash_table.get(0) == 'hello'

hash_table.set(3, 'hello2') # 0 bucket again
assert len(hash_table.buckets[0].elements) == 2

hash_table.set(0, 'hello_new') # 0 bucket, replace
assert len(hash_table.buckets[0].elements) == 2
assert hash_table.get(0) == 'hello_new'
```


Please use a template for the implementation (`tasks/hash_table.py`).


## Problem 2: Find two numbers that add up to a given target

Given an array of integers `values` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Constraints**
* 2 <= values.length <= 3*10^5
* -10^9 <= values[i] <= 10^9
* -10^9 <= target <= 10^9
* Only one valid answer exists.

**Example 1:**

Input: values = [1, 2, 3, 4, 5], target = 4

Output: [0, 2]

Explanation: values[0] + values[2] == 4


**Example 2:**

Input: values = [1, 2, 3, 4, 5], target = 8

Output: [2, 4]

Explanation: values[2] + values[4] == 8


Please use a template for the implementation (`tasks/two_sum.py`).


## Problem 3: Repeated DNA Sequences

The **DNA sequence** is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'` and `'T'`.

For example, `"ACGAATTCCG"` is a DNA sequence.
When studying **DNA**, it is useful to identify repeated sequences within the DNA.

Given a string `dna_sequence` that represents a **DNA sequence**, return all the `8`**-letter-long** sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in **any order**.

**Constraints**
* 1 <= dna_sequence.length <= 10^5
* dna_sequence contains only 'A', 'C', 'G' and 'T' characters.

**Example 1**

Input: dna_sequence='AAAATTTTAAAATTTT'

Output: ['AAAATTTT']


**Example 2**

Input: dna_sequence='ATATATATATA'

Output: ['ATATATAT', 'TATATATA']

Please use a template for the implementation (`tasks/dna.py`).
