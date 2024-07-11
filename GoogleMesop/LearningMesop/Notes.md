# Notes while Learning Mesop v 0.9.3

## States
`@me.stateclass` is like python's `dataclass`
This module provides a decorator and functions for automatically adding generated special methods such as `__init__()` and `__repr__()` to user-defined classes.
``` python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
will add, among other things, a `__init__()` that looks like:
```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
```
:bulb: Note that this method is automatically added to the class: it is not directly specified in the InventoryItem definition shown above.