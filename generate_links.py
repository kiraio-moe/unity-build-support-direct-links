import json
import os
# import requests

UNITY_VERSIONS_DATA = "unity_versions.json"

servers = [
    "download.unity3d.com/download_unity/",
    "beta.unity3d.com/download/"
]
linkPrefix = "/TargetSupportInstaller/UnitySetup-"
linkSuffix = "-Support-for-Editor-"
platforms = {
    "Android": "Android",
    "iOS": "iOS",
    "tvOS": "AppleTV",
    "Linux (IL2CPP)": "Linux-IL2CPP",
    "Linux (Mono)": "Linux-Mono",
    "Mac (Mono)": "Mac-Mono",
    "Universal Windows Platform": "Universal-Windows-Platform",
    "WebGL": "WebGL",
    "Windows (IL2CPP)": "Windows-IL2CPP",
    "Lumin OS (Magic Leap)": "Lumin"
}

##
# TODO: Fetch data in realtime then update unity_versions.json automatically
# get request from https://unity.com/releases/editor/archive
# collect every Unity Hub links
# parse into json file with Unity version as key and hash/id as value
##
# fetchData = requests.get("https://unity.com/releases/editor/archive")
# if fetchData.status_code == 200:
#     print("Fetching Unity version from Unity Download Archive...")
# else:
#     print("Unable to connect into Unity Download Archive! Error: status code", fetchData.status_code)

with open(UNITY_VERSIONS_DATA, "r") as file:
    unityVersionsData = json.load(file)

# Generate main README
with open("README.md", "w") as file:
    print("Generating README...")
    file.writelines([
        "# Unity Build Support Direct Download Links\n",
        "\n",
        "Taking too long to download Build Support/Playback Engine using Unity Download Assistant?  \n",
        "No worry... You can use the direct download link below and download it using your favorite Download Manager!\n",
        "\n",
        "All links are obtained from the official Unity server, so it's safe.  \n",
        "I limit the version of Unity that I think is still often used.\n",
        "\n",
        "Because of Markdown limitation, I separate each major version.\n",
        "\n"
    ])

    filteredVersions = [] # 2022, 2021, etc.

    for version in unityVersionsData:
        shortVersion = version[:4]
        if shortVersion not in filteredVersions:
            filteredVersions.append(shortVersion)

    for version in filteredVersions:
        file.write(f"- [Unity {version}](./unity_{version}/README.md \"Unity {version}\")\n")

for version in filteredVersions:
    if not os.path.exists(f"unity_{version}"):
        os.mkdir(f"unity_{version}")

    with open(f"unity_{version}/README.md", "w") as file:
        print(f"Generating Unity {version}...")

        for unityVersion in unityVersionsData:
            if unityVersion[:4] == version:
                uid = unityVersionsData[unityVersion]

                file.writelines([
                    f"## Unity {unityVersion}\n",
                    "\n"
                ])

                for platform in platforms:
                    platformUrl = platforms[platform]

                    file.writelines([
                        "- <details>\n",
                        f"  <summary>{platform}</summary>\n",
                        "\n"
                    ])

                    for server in servers:
                        compiledUrl = f"https://{server}{uid}{linkPrefix}{platformUrl}{linkSuffix}{unityVersion}.exe"

                        file.writelines([
                            f"  - <{compiledUrl}>\n"
                        ])

                    file.writelines([
                        "\n",
                        "  </details>\n",
                        "\n"
                    ])
