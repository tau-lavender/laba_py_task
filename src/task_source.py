from src.task import Task
from typing import Iterable, Protocol, runtime_checkable


@runtime_checkable
class TaskSource(Protocol):
    def get_tasks(self) -> Iterable[Task]:
        ...
