import os
import api
import constants
import tarfile
import extract_zst

# Install Directories
LUTRIS_RUNTIME = os.path.expanduser("~/.local/share/lutris/runtime/")
STEAM_RUNTIME = os.path.expanduser("~/.local/share/Steam/compatibilitytools.d/")


def Install(repo):
    file = api.DownloadLatestRelease(repo)
    print()
    LUTRIS = constants.COMPITABILITY[repo]["LUTRIS"]
    STEAM = constants.COMPITABILITY[repo]["STEAM"]

    suffix=file.split('.tar')[1]

    if suffix == ".gz":
        if STEAM:
            ExtractTARGZ(file,STEAM_RUNTIME)
        
        if LUTRIS:
            ExtractTARGZ(file, LUTRIS_RUNTIME)
    else:
        if STEAM:
            extract_zst.extract_zst(file,STEAM_RUNTIME)
        
        if LUTRIS:
            extract_zst.extract_zst(file, LUTRIS_RUNTIME)


def ExtractTARGZ(file, out_path):
    f = tarfile.open(file).extractall(out_path)
    f.close()