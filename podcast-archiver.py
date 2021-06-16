import typer
from utils.utils import *
import os


def main(
    feed: str,
    start_index: int = typer.Option(1, help="First episode to download."),
    end_index: int = typer.Option(10, help="Last episode to download."),
    last_n_eps: int = typer.Option(None, help="Download last n episodes.")
):
    """
    Specify FEED url to download the first 10 episodes by default.

    You can use --start_index and --end_index to specify start and end episode manually (default to the first 10 episodes chronologically).
    """

    FOLDER_NAME, episodes = get_episodes(feed)

    ######################## filter download episodes ########################
    if last_n_eps:
        episodes = episodes[-last_n_eps:]
    elif start_index:
        start_index -= 1
        episodes = episodes[start_index: end_index]

    ######################## download ########################
    FOLDER_NAME = os.path.join('podcasts',  FOLDER_NAME)
    os.makedirs(FOLDER_NAME, exist_ok=True)

    for episode in episodes:
        output_file = os.path.join(FOLDER_NAME, episode['filename'])

        print(f'Downloading {output_file}')
        download(episode['url'], output_file)

if __name__ == "__main__":
    typer.run(main)
