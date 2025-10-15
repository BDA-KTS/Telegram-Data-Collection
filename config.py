# insert your own api_id and api_hash, see https://core.telegram.org/api/obtaining_api_id
API_ID = 00000000
API_HASH = '00000000000000000000000000000000'

# collection process configuration
MAX_MESSAGES = 100                             # maximum number of messages to collect per channel
LIMIT_SEED_LIST = 100                          # maximum number of seed channels to use

# input/output configuration
SEED_LIST = 'input/public_group_seed_list.txt' # input file
OUT_DIR = 'output/messages/'                   # output directory for channel files
OUT_TRACKING = 'output/tracking.csv'           # file to store the last collected message per channel

