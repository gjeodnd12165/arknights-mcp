"""Clones https://github.com/Kengxxiao/ArknightsGameData_YoStar into /ArknightsGameData_YoStar"""

from git import Repo

import logging

def clone_raw_data_repo():
    """Clone the Arknights raw data repository."""
    repo = Repo("ArknightsGameData_YoStar")
    if repo:
        logging.info("Repository already exists, skipping clone.")
    else:
        logging.info("Cloning Arknights raw data repository. This may take a while...")
        repo = Repo.clone_from(
            url="https://github.com/Kengxxiao/ArknightsGameData_YoStar.git",
            to_path="ArknightsGameData_YoStar",
        )
    logging.info("Updating the repository to the latest version...")
    repo.remote().fetch()
    repo.git.reset("--hard", "origin/main")
    logging.info("Repository cloned and updated successfully.")