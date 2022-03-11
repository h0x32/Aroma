import argparse
import constants


def initializeParser():
    ARGS = argparse.ArgumentParser(usage="%(prog)s", description="A small software that manages different Wine-based or gaming-related projects on any Linux distro ",
                                   epilog="MIT - Repo : https://github.com/h0x32/Aroma")

    ARGS.add_argument("-i", "--install",
                      help="Usage: Aroma -i or --install {PROJECT} to install and configure a project", type=str, metavar="{PROJECT}")

    ARGS.add_argument("-d", "--download",
                      help="Usage: Aroma -d or --download {PROJECT} to only download a project", type=str, metavar="{PROJECT}")

    ARGS.add_argument('-l', '--list', action='store_true',
                      help="Usage: Aroma -l or --list to list avaible projects")

    ARGS.add_argument("-v", "--verbose", action='store_true',
                      help="Usage: Aroma -v to enable verbose mode")

    return ARGS.parse_args()
