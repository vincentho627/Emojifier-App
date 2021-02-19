import json
import pathlib

# ====== GLOBAL VARIABLES ====== #
EMOJI_DICT = {}

PATH_NAME = str(pathlib.Path().absolute())
PATH_EMOJILIST = PATH_NAME + "/EmojiList.json"
PATH_TO_DATASET = PATH_NAME + "/Dataset"
PATH_TO_DATA_CSV = PATH_TO_DATASET + "/Data/500_picts_satz.csv"

f = open(PATH_EMOJILIST)
emojiList = json.load(f)["Emoji"]
for i, emoji in enumerate(emojiList):
    EMOJI_DICT[emoji] = i


if __name__ == "__main__":
    print(PATH_TO_DATA_CSV)

