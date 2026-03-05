from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class Payload(Protocol):
    def do_smth(self) -> None:
        ...


@dataclass
class Task:
    """Task data"""
    id: int
    payload: Payload


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> list[Task]:
        ...
