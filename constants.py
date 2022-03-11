

# Colors used for terminal output

COLOR_RED       = "\033[31m"
COLOR_BLUE      = "\033[34m"
COLOR_GREEN     = "\033[32m"
COLOR_PURPLE    = "\033[35m"
COLOR_CYAN      = "\033[36m"
END_COLOR       = "\033[0m"

# Software's version

VERSION         = "0.1"


# GitHub urls

PROJECTS = {}

GITHUB_ENDPOINT                 = "https://api.github.com/repos"

PROJECTS["VKD3D-PROTON"]        = "https://github.com/HansKristian-Work/vkd3d-proton"

PROJECTS["DXVK"]                = "https://github.com/doitsujin/dxvk"
PROJECTS["DXVK-NVAPI"]          = "https://github.com/jp7677/dxvk-nvapi"

PROJECTS["WINE-GE-CUSTOM"]      = "https://github.com/GloriousEggroll/wine-ge-custom"

PROJECTS["PROTON-GE-CUSTOM"]    = "https://github.com/GloriousEggroll/proton-ge-custom"
#PROJECTS["PROTON"]             = "https://github.com/ValveSoftware/Proton"
PROJECTS["PROTON-TKG"]          = "https://github.com/gardotd426/proton-tkg"

#PROJECTS["MANGOHUD"]           = "https://github.com/flightlessmango/MangoHud"

ACCEPTED_CONTENT_TYPES          = {'application/x-xz':"r:xz",'application/gzip':"r:gz",'application/zstd':"r"}

# Intro Message

END_LINE        = "\n"

AROMA = [
    COLOR_PURPLE,   "###############################################################################", END_LINE,
                    "                                                                    ^          ", END_LINE,
                   f"         Welcome to Aroma                                          / \         ", END_LINE,
                    "                                                                  / - \        ", END_LINE,
    COLOR_CYAN,     "         A small software that manages different Wine-based      / - - \       ", END_LINE,
                    "         or gaming-related projects on any Linux distro         /_/   \_\      ", END_LINE,
                    "                                                                               ", END_LINE,
    COLOR_RED,      "         Licenese: MIT                                                         ", END_LINE,
                    "         Repo: https://github.com/h0x32/Aroma                                  ", END_LINE,
                   f"         Version: {VERSION}                                                    ", END_LINE,
                    "                                                                               ", END_LINE,
    COLOR_BLUE,     "   Synopsis:                                                                   ", END_LINE,
    COLOR_GREEN,    "    Usage: Aroma -i or --install {PROJECT} to install and configure a project  ", END_LINE,
                    "    Usage: Aroma -d or --download {PROJECT} to only download a project         ", END_LINE,
                    "    Usage: Aroma -l or --list to list avaible projects                         ", END_LINE,
                    # "    Usage: Aroma -v or ---verbose to enable verbose mode                       ", END_LINE,
    COLOR_PURPLE,   "###############################################################################", END_COLOR
]


# Compilation commands

COMPITABILITY = {}

COMPITABILITY["VKD3D-PROTON"]        = {"LUTRIS":True, "STEAM":False}

COMPITABILITY["DXVK"]                = {"LUTRIS":True, "STEAM":False}
COMPITABILITY["DXVK-NVAPI"]          = {"LUTRIS":True, "STEAM":False}

COMPITABILITY["WINE-GE-CUSTOM"]      = {"LUTRIS":True, "STEAM":False}

COMPITABILITY["PROTON-GE-CUSTOM"]    = {"LUTRIS":False, "STEAM":True}
#COMPITABILITY["PROTON"]             = {"LUTRIS":False, "STEAM":True}
COMPITABILITY["PROTON-TKG"]          = {"LUTRIS":False, "STEAM":True}

#COMPITABILITY["MANGOHUD"]           = {"LUTRIS":False, "STEAM":False}

