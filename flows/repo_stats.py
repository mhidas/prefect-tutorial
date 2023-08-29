import sys
import httpx
from datetime import timedelta
from prefect import flow, task, get_run_logger
from prefect.tasks import task_input_hash


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
def get_url(url: str, params: dict = None):
    response = httpx.get(url, params=params)
    response.raise_for_status()
    return response.json()


@flow(log_prints=True, retries=3, retry_delay_seconds=5)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    repo = get_url(f"https://api.github.com/repos/{repo_name}")
    logger = get_run_logger()
    logger.info(f"{repo_name} repository statistics 🤓:")
    logger.info(f"Stars 🌠 : {repo['stargazers_count']}")
    logger.info(f"Forks 🍴 : {repo['forks_count']}")
    print("'That's all for now!' he printed.")


if __name__ == "__main__":
    try:
        get_repo_info(sys.argv[1])
    except IndexError:
        get_repo_info()
