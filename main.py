from prefect import flow, task
import pandas as pd

import random

from base_functions import tasks

@task
def get_customer_ids() -> list[str]:
    # Fetch customer IDs from a database or API
    return [f"customer{n}" for n in random.choices(range(100), k=10)]

@task
def process_customer(customer_id: str) -> str:
    # Process a single customer
    return f"Processed {customer_id}"

@flow
def main() -> list[str]:
    test = tasks.process_dataframe()
    customer_ids = get_customer_ids()
    results = process_customer.map(customer_ids)
    return results


if __name__ == "__main__":
    main()
