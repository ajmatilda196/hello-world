from _typeshed import Incomplete
from typing import Any

from . import util

def build_treeprocessors(md, **kwargs): ...
def isString(s): ...

class Treeprocessor(util.Processor):
    def run(self, root) -> Any | None: ...

class InlineProcessor(Treeprocessor):
    inlinePatterns: Any
    ancestors: Any
    def __init__(self, md) -> None: ...
    stashed_nodes: Any
    parent_map: Any
    def run(self, tree, ancestors: Incomplete | None = ...): ...

class PrettifyTreeprocessor(Treeprocessor): ...
