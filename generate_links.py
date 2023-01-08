import json
# import requests

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

# TODO: Fetch data in realtime then update unity_versions.json automatically
# fetchData = requests.get("https://unity.com/releases/editor/archive")
# if fetchData.status_code == 200:
#     print("Fetching Unity version from Unity Download Archive...")
# else:
#     print("Unable to connect into Unity Download Archive! Error: status code", fetchData.status_code)

with open("unity_versions.json", "r") as file:
    unityVersions = json.load(file)

with open("README.md", "w") as file:
    file.writelines([
        "# Unity Build Support Direct Download Links\n",
        "\n",
        "Taking too long to download Build Support/Playback Engine using Unity Download Assistant?  \n",
        "No worry... You can use the direct download link below and download it using your favorite Download Manager!\n",
        "\n",
        "All links are obtained from the official Unity server, so it's safe.  \n",
        "I limit the version of Unity that is still often used.\n",
        "\n"
    ])

    for version in unityVersions:
        uid = unityVersions[version]

        file.writelines([
            f"## Unity {version}\n",
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
                compiledUrl = f"https://{server}{uid}{linkPrefix}{platformUrl}{linkSuffix}{version}.exe"

                file.writelines([
                    f"  - <{compiledUrl}>\n"
                ])

            file.writelines([
                "\n",
                "  </details>\n",
                "\n"
            ])
