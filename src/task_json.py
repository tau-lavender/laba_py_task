from src.task import Task
import json


class BrokenJSONError(Exception):
    pass


class PrintPayload:
    def __init__(self, msg: str) -> None:
        self.msg = msg

    def do_smth(self) -> None:
        print(self.msg)


class TaskSourceJSON:
    def __init__(self, filename: str) -> None:
        if not filename.endswith(".json"):
            raise NameError(f"{filename} is not json")
        self.filename = filename

    def get_tasks(self) -> list[Task]:
        with open(self.filename, "r", encoding="utf-8") as f:
            task_list: list[Task] = []
            json_string = f.read()
            raw: dict = json.loads(json_string)
            if not isinstance(raw, dict):
                raise BrokenJSONError(f"in {self.filename} no task dict")
            for task_id in raw:
                try:
                    task_id_int = int(task_id)
                except ValueError:
                    raise BrokenJSONError(f"in {self.filename} id {task_id} not int")
                msg = raw[task_id]
                if not isinstance(msg, str):
                    raise BrokenJSONError(f"in {self.filename} payload not string")
                task_list.append(Task(task_id_int, PrintPayload(msg)))
            return task_list
