<p align="center">
  <br>
  <a href="https://sherlock-project.github.io/" target="_blank"><img src="images/sherlock-logo.png" alt="sherlock"/></a>
  <br>
  <span>Hunt down social media accounts by username across <a href="https://sherlockproject.xyz/sites">400+ social networks</a></span>
  <br>
</p>

<p align="center">
  <a href="https://sherlockproject.xyz/installation">Installation</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="https://sherlockproject.xyz/usage">Usage</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="https://sherlockproject.xyz/contribute">Contributing</a>
</p>

<p align="center">
<img width="70%" height="70%" src="images/demo.png" alt="demo"/>
</p>


## Installation

> [!WARNING]  
> Packages for ParrotOS and Ubuntu 24.04, maintained by a third party, appear to be __broken__.  
> Users of these systems should defer to pipx/pip or Docker.

| Method | Notes |
| - | - |
| `pipx install sherlock-project` | `pip` may be used in place of `pipx` |
| `docker run -it --rm sherlock/sherlock` |
| `dnf install sherlock-project` | |

Community-maintained packages are available for Debian (>= 13), Ubuntu (>= 22.10), Homebrew, Kali, and BlackArch. These packages are not directly supported or maintained by the Sherlock Project.

See all alternative installation methods [here](https://sherlockproject.xyz/installation)

## General usage

To search for only one user:
```bash
sherlock user123
```

To search for more than one user:
```bash
sherlock user1 user2 user3
```

Accounts found will be stored in an individual text file with the corresponding username (e.g ```user123.txt```).

```console
$ sherlock --help
usage: sherlock [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT]
                [--output OUTPUT] [--tor] [--unique-tor] [--csv] [--xlsx]
                [--site SITE_NAME] [--proxy PROXY_URL] [--json JSON_FILE]
                [--timeout TIMEOUT] [--print-all] [--print-found] [--no-color]
                [--browse] [--local] [--nsfw]


... (truncated)