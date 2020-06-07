from collections import deque
from typing import Deque, Dict, List

_name = "spypy"
_version = "0.0.1"

_counters: Dict[str, int] = {}
_stamps: Dict[str, float] = {}
_history: Dict[str, list] = {}
_stack: Deque = deque()
_tree: List[dict] = []
_config = None
