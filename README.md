# Telegram-Data-Collection

## Description

The method extracts messages broadcast across Telegram channels. As a broadcasting social media platform, on Telegram channel administrator can broadcast their content as text or other media messages to disseminate information to the users of that channel. This method takes public channel IDs (as seeds), requires a telephone number with Telegram App, and extracts messages in JSON format across all seed channels as well as other public channels where the messages from the seed channels were forwarded. 

## Use Cases

Telegram data, such as collected via this method, can be used in various analyses. For example:

- Analysing extremism in a specific geographic area (e.g., Walther, Samantha, and Andrew McCoy. "US extremism on Telegram." Perspectives on Terrorism 15.2 (2021): 100-124.)
- Analysing terrorism and mass media (e.g., Yayla, Ahmet S., and Anne Speckhard. "Telegram: The mighty application that ISIS loves." International Center for the Study of Violent Extremism 9 (2017).)
- Analysing right wing networks (e.g., Urman, Aleksandra, and Stefan Katz. "What they do in the shadows: examining the far-right networks on Telegram." Information, communication & society 25.7 (2022): 904-923.)
- Analysing social media and fake channels (e.g., La Morgia, Massimo, et al. "It’s a Trap! Detection and Analysis of Fake Channels on Telegram." 2023 IEEE International Conference on Web Services (ICWS). IEEE, 2023.)

## Input data

The output of this method is channel names which needs to be specified in the [`public_group_seed_list.txt`](seed/public_group_seed_list.txt) file in the `seed` folder. Following are few input examples:

```
britishnewspatriot
bloomberg
SpotifyGroup
```

*To get the complete seed list used and the dataset created with it, please go to [https://search.gesis.org/research_data/SDN-10.7802-2825](https://search.gesis.org/research_data/SDN-10.7802-2825) and click on the Dataset from the right menu. The list link on the list is the seeds*

## Output Data

The method outputs the collected raw data as JSON objects containing the message and its metadata like in the example shown below into the [`public_group_messages`](public_group_messages/) directory (see there for some examples). The file [`tracking/public_group.csv`](tracking/public_group.csv) is automatically updated to track the last collected message per channel.

```json
{
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
}
```

## Hardware Requirements

The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD). However, more resources are needed to set it up for large-scale Telegram data collection.

## Environment Setup

This method requires Python 3.10 or higher to run.

```bash
conda create -n env python=3.11
```

To install the dependencies you may use: 

```bash
pip3 install -r requirements.txt
```

You should also have Telegram installed and a Telegram account in your phone

## How to Use

1. Run in command line:  
  ```bash
  python extract_from_seed_list.py
  ```
2. The framework will ask for a phone number: Enter the phone number through which Telegram account has been created
3. The framework will ask for an one time password: Enter the one-time-password (OTP) sent to you through the Telegram app

# Contact

For further queries, please contact <Susmita.Gangopadhyay@gesis.org>
