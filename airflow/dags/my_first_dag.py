from airflow.sdk import dag, task


@dag
def my_first_dag():
    @task
    def task1():
        print("Completed Task 1")
        return "Hello from Task 1"

    @task
    def task2(message: str):
        print(f"Completed Task 2 with message: {message}")
        return (f"{message}").lower()

    @task
    def task3(final_message: str):
        print(f"Completed Task 3 with message: {final_message}")

    m = task1()
    t = task2(m)
    task3(t)


my_first_dag()
