from airflow.sdk import dag, task
from src import iterate_over


@dag()
def my_example_dag():
    @task
    def extract():
        return [1, 2, 3]

    @task
    def transform(data):
        return list(iterate_over(data))

    @task
    def load(data):
        print(f"Loaded data: {data}")

    data = extract()
    transformed_data = transform(data)
    load(transformed_data)


my_example_dag()
