from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime
import os

API_KEY = "AIzaSyCXpqOV7EscChBa0nga5OFssXVQvH30NuU"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# 20 popular YouTube channel IDs
channel_ids = [
    "UCX6OQ3DkcsbYNE6H8uQQuVA",  # MrBeast
    "UCq-Fj5jknLsUf-MWSy4_brA",  # T-Series
    "UCbCmjCuTUZos6Inko4u57UQ",  # Cocomelon - Nursery Rhymes
    "UCOhHO2ICt0ti9KAh-QHvttQ",  # SET India
    "UCvlE5gTbOvjiolFlEm-c_Ow",  # Vlad and Niki
    "UCk8GzjMOrta8yxDcKfylJYw",  # Kids Diana Show
    "UCJplp5SjeGSdVdwsfb9Q7lQ",  # Like Nastya
    "UCbp9MyKCTEww4CxEzc_Tp0Q",  # Stokes Twins
    "UCFFbwnve3yF62-tVXkTyHqg",  # Zee Music Company
    "UC-lHJZR3Gqxm24_Vd_AJ5Yw",  # PewDiePie
    "UCOmHUn--16B90oW2L6FRR3A",  # BLACKPINK
    "UCLkAepWjdylmXSltofFvsYQ",  # BANGTANTV
    "UCY1kMZp36IQSyNx_9h4mpCg",  # Mark Rober
    "UCRijo3ddMTht_IHyNSNXpNQ",  # Dude Perfect
    "UCiGm_E4ZwYSHV3bcW1pnSeQ",  # Billie Eilish
    "UC8-Th83bH_thdKZDJCrn88g",  # The Tonight Show
    "UCYzPXprvl5Y-Sf0g4vX-m6g",  # jacksepticeye
    "UCaWd5_7JhbQBe4dknZhsHJg",  # WatchMojo.com
    "UCsXVk37bltHxD1rDPwtNM8Q",  # Kurzgesagt – In a Nutshell
    "UCZU9T1ceaOgwfLRq7OKFU4Q",  # Linkin Park
]

# Output directory
output_dir = "Python/youtube_scraping_project/output"
os.makedirs(output_dir, exist_ok=True)

# Build YouTube client
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

all_stats = []
today = datetime.today().strftime("%Y-%m-%d")

# Pull stats
for i in range(0, len(channel_ids), 50):
    request = youtube.channels().list(
        part="snippet,statistics",
        id=",".join(channel_ids[i:i+50])
    )
    response = request.execute()
    for channel_info in response["items"]:
        stats = {
            "Channel ID": channel_info["id"],
            "Channel Title": channel_info["snippet"]["title"],
            "Subscribers": int(channel_info["statistics"].get("subscriberCount", 0)),
            "Total Views": int(channel_info["statistics"].get("viewCount", 0)),
            "Video Count": int(channel_info["statistics"].get("videoCount", 0)),
            "Date": today
        }
        all_stats.append(stats)

# Save daily snapshot
file_path = os.path.join(output_dir, f"channel_stats_{today}.csv")
df = pd.DataFrame(all_stats)
df.to_csv(file_path, index=False)
print(f"Saved daily stats: {file_path}")
