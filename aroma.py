#!/usr/bin/python3


import utils
import constants
import parser
import installer
import api

def main():
    args = parser.initializeParser()

    if args.list:
        api.ListProjects()
    elif args.download:
        api.DownloadLatestRelease(args.download)
    elif args.install:
        installer.Install(args.install)
    else:
        utils.pm(constants.AROMA)
