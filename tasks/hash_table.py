"""Templates for programming assignments: operations with hash table."""
from typing import Any, List, Optional


class KeyValueData:
    """Data that will be stored in hash table.
    
    NOTE: no need to change this class.
    """
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value


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