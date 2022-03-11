import requests
import constants
import utils
import wget


headers = {
    
}


def GetRepoDataInJson(owner, repo):
    return requests.get(f"{constants.GITHUB_ENDPOINT}/{owner}/{repo}", headers=headers).json()


def GetRepoReleasesInJson(owner, repo):
    return requests.get(f"{constants.GITHUB_ENDPOINT}/{owner}/{repo}/releases", headers=headers).json()


def PrettyPrintRepo(repoData):

    if repoData['license'] == None:
        licenseData = "None"
    else:
        licenseData = repoData['license']['name']

    F = [
        constants.COLOR_GREEN,  f" Owner:       {repoData['owner']['login']:<20}        ", constants.END_LINE,
        constants.COLOR_BLUE,   f" Description: {repoData['description']:<20}           ", constants.END_LINE,
        constants.COLOR_PURPLE, f" Created:     {repoData['created_at']:<20}            ", constants.END_LINE,
        constants.COLOR_RED,    f" License:     {licenseData:<20}                       ", constants.END_LINE,
        constants.COLOR_CYAN,   f" Install:     {str(repoData['name']).upper():<20}     ", constants.END_COLOR, constants.END_LINE
    ]

    utils.pm(F)


def SplitOwnerRepo(url): return url.split("/")[-2:]


def ListProjects():
    for value in constants.PROJECTS.values():
        owner, repo = SplitOwnerRepo(value)
        PrettyPrintRepo(GetRepoDataInJson(owner, repo))


def DownloadFile(url): return wget.download(url)


def DownloadLatestRelease(repo):
    for key in constants.PROJECTS:
        if key == repo:

            owner, repo = SplitOwnerRepo(constants.PROJECTS[key])
            releases = GetRepoReleasesInJson(owner, repo)
            latest = releases[0]

            release_url = latest['html_url']
            release_notes = latest['body']
            created = latest['created_at']
            version = latest['tag_name']
            assets= latest['assets']

            if (len(assets) > 0):
                for asset in latest['assets']:
                    if asset['content_type']:
                        if asset['content_type'] in constants.ACCEPTED_CONTENT_TYPES:
                            link = asset['browser_download_url']

                            size = int(asset['size'])/1048576
                            size = "%.2fMB" % size
            else:
                link = latest['tarball_url']
                size = "N/A"

            F = [
                constants.COLOR_BLUE,   f"                                          ", constants.END_LINE,
                                        f" Release Notes:\n {release_notes:<20}     ", constants.END_LINE,
                constants.COLOR_GREEN,  f" Url:             {release_url:<20}       ", constants.END_LINE,
                constants.COLOR_PURPLE, f" Created:         {created:<20}           ", constants.END_LINE,
                constants.COLOR_RED,    f" Version:         {version:<20}           ", constants.END_LINE,
                constants.COLOR_RED,    f" Link:            {link:<20}              ", constants.END_LINE,
                constants.COLOR_CYAN,   f" Size:            {size:<20}              ", constants.END_COLOR, constants.END_LINE
            ]

            utils.pm(F)

            choice = input(" Enter (Y/n) to download: ")

            if not choice == "n":
                return DownloadFile(link)
