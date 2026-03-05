from src.task import TaskSource
from src.task_json import TaskSourceJSON


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    source_list: list[TaskSource] = [TaskSourceJSON("example.json")]
    for source in source_list:
        assert isinstance(source, TaskSource)
        for task in source.get_tasks():
            print(f"start task: {task.id}")
            task.payload.do_smth()


if __name__ == "__main__":
    main()
