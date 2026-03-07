from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Task:
    """Task data"""
    task_id: str
    payload: object
