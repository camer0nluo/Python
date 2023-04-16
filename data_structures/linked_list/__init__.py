"""
Linked Lists consists of Nodes.
Nodes contain data and also may link to other nodes:
    - Head Node: First node, the address of the
                 head node gives us access of the complete list
    - Last node: points to null
"""
from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, item: Any, next: Any) -> None:
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0

    def add(self, item: Any) -> None:
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self) -> Any:
        if self.head is None:
            return None
        item = self.head.item
        self.head = self.head.next
        self.size -= 1
        return item

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        """
        >>> linked_list = LinkedList()
        >>> linked_list.add(23)
        >>> linked_list.add(14)
        >>> linked_list.add(9)
        >>> print(linked_list)
        9 --> 14 --> 23
        """
        if not self.is_empty:
            return ""
        iterate = self.head
        item_str = ""
        item_list: list[str] = []
        while iterate:
            item_list.append(str(iterate.item))
            iterate = iterate.next

        return " --> ".join(item_list)

    def __len__(self) -> int:
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        1
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        0
        """
        return self.size
