# Telegram-Data-Collection
# Description
The method helps to deploy a Telegram data collection setup for extracting Telegram messages broadcast across channels. As a broadcasting social media platform, the channel administrator can broadcast content as text messages and other media to disseminate information to the users of that channel. The method takes public channel IDs (as seeds) and a telephone number with Telegram App installed as input and extracts messages across all seed channels as well as other public channels where the message was published. 

# Relevant research questions that could be adressed with the help of this method

1. Study of extremism in a specific geographic area(Walther, Samantha, and Andrew McCoy. "US extremism on Telegram." Perspectives on Terrorism 15.2 (2021): 100-124.)

2. Study of Terrorism and Mass Media (Yayla, Ahmet S., and Anne Speckhard. "Telegram: The mighty application that ISIS loves." International Center for the Study of Violent Extremism 9 (2017).)

3. Right wing networks and their analysis (Urman, Aleksandra, and Stefan Katz. "What they do in the shadows: examining the far-right networks on Telegram." Information, communication & society 25.7 (2022): 904-923.)

4. Investigate social media and fake channels (La Morgia, Massimo, et al. "It’sa Trap! Detection and Analysis of Fake Channels on Telegram." 2023 IEEE International Conference on Web Services (ICWS). IEEE, 2023.)


# Social Science Usecase
John is a researcher studying about misinformation and rumors in social media. He seeks to harness Telegram data for his research endeavors. He visits the MH portal to find this method that helps him to fetch data from Telegram channels. He uses the search box on the top of the interface and types in Data Collection or Telegram. The search functionality of the MH shows him a list or related methods and tutorials that provides John with methods that can help him generate this huge collection of messages which he can reuse for his study.


# Keywords
Telegram, Social-Media, Data Collection

# Repo Structure
The repository is organized as follows:
* Folders
  
    `public_group_messages folder` -output folder where messages from channels will be stored as txt files

    `seed folder` - input folder where the channel names from where messages should be collected is stored

    `src folder` - Main code for data collection using Telethon API

    `tracking folder` - output folder for tracking the channel names and the time of the last message collected

* Files

    `config.py` - configurable parameters of the framework

# Environment SetUp
This method requires Python 3.x to run.

# Dependencies
To install the dependencies you may use: 

  `pip3 install -r requirements.txt `

You should also have Telegram installed and a Telegram account in your phone


# Limitation
The method collects only the raw messages. For enrichments to the messages, further modifications to the code would be required

# How to Use

1. Run in command line:  

   `python 1_extract_from_seed_list.py`

2. The framework will ask for a phone number : Enter the phone number through which Telegram account has been created

3. The framework will ask for an one time password : Enter the OTP sent to you through the Telegram app




# Input data
The output of this method is channel names which needs to be specified in the public_group_seed_list.txt file in seed folder

# Sample Input to the method

    britishnewspatriot
     bloomberg
     SpotifyGroup`

# Sample Output of the method

```{
  "_": "Message",
  "id": 2004376,
  "peer_id": {
    "_": "PeerChannel",
    "channel_id": 1050982793
  },
  "date": "2024-01-25 16:13:00.000000",
  "message": "In math homework, Reem was given a value of x and was asked to find y using the following formula.\ny = x + exp(x/100)\nThe function exp(z) is exponentiation in the natural log base, that is, e to the power of z (also written as e^z).\nReem wrote down the value of y, which is equal to 418.23783639564084, but forgot to note the value of x. Can you help her recover the value of x?\nYour answer should be a real number x. The answer is considered correct if when substituted into the formula above, the result is very close to y. More precisely, the answer is considered correct if and only if the following holds.\n|y - (x + exp(x/100))| < 0.001",
  "out": false,
  "mentioned": false,
  "media_unread": false,
  "silent": false,
  "post": false,
  "from_scheduled": false,
  "legacy": false,
  "edit_hide": false,
  "pinned": false,
  "noforwards": false,
  "from_id": {
    "_": "PeerUser",
    "user_id": 5885885469
  },
  "fwd_from": null,
  "via_bot_id": null,
  "reply_to": null,
  "media": null,
  "reply_markup": null,
  "entities": [],
  "views": null,
  "forwards": null,
  "replies": {
    "_": "MessageReplies",
    "replies": 1,
    "replies_pts": 3145930,
    "comments": false,
    "recent_repliers": [],
    "channel_id": null,
    "max_id": 2004379,
    "read_max_id": null
  },
  "edit_date": null,
  "post_author": null,
  "grouped_id": null,
  "reactions": null,
  "restriction_reason": [],
  "ttl_period": null
}```

# Contact
Susmita.Gangopadhyay@gesis.org


