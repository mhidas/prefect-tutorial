import sys
import httpx
from prefect import flow, get_run_logger


@flow(log_prints=True, retries=3, retry_delay_seconds=5)
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
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
