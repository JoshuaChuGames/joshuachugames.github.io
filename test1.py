import requests
from dirsearch import DirsearchFuzzer, FuzzerConfig

url = "http://cs177.seclab.cs.ucsb.edu:33245/download"

# Common directory names to check inside /home/app/ (no slashes needed)
subdirs = [
    "static",
    "templates",
    "src",
    "app",
    "data",
    "secret",
    "secrets",
    "config",
    "uploads",
    "files",
    "admin"
]

config = FuzzerConfig(
    url="https://example.com",
    wordlist=["admin", "login.php", "api/users"],
)

results = DirsearchFuzzer(config).run()

for result in results:
    print(result.status, result.path, result.url, result.length)