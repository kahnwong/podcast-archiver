# podcast-archiver

```
Usage: podcast-archiver.py [OPTIONS] FEED

  Specify FEED url to download the first 10 episodes by default.

  You can use --start_index and --end_index to specify start and end episode
  manually (default to the first 10 episodes chronologically).

Arguments:
  FEED  [required]

Options:
  --start-index INTEGER           First episode to download.  [default: 1]
  --end-index INTEGER             Last episode to download.  [default: 10]
  --last-n-eps INTEGER            Download last n episodes.
  --help                          Show this message and exit.
```

## Output structure
```
podcasts
└── AUTHOR - PODCAST_NAME
    ├── PUBLISHED_DATE-TITLE.EXT


podcasts
└── SuperDataScience Podcast - Skyrocket Your Career - SuperDataScience
    ├── 20210514-SDS 470- My Favorite Books.mp3
    ├── 20210518-SDS 471- 99 Days to Your First Data Science Job.mp3
    ├── 20210521-SDS 472- The Learning Never Stops (so Relax).mp3
    └── 20210525-SDS 473- Machine Learning at NVIDIA.mp3
```

## Example commands
```bash
python3 podcast-archiver.py https://feeds.soundcloud.com/users/soundcloud:users:253585900/sounds.rss

python3 podcast-archiver.py https://feeds.soundcloud.com/users/soundcloud:users:253585900/sounds.rss --last-n-eps 10
```