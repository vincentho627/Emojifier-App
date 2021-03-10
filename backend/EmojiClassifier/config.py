import json
import pathlib

# ====== GLOBAL VARIABLES ====== #
EMOJI_DICT = {}

PATH_NAME = str(pathlib.Path().absolute())
PATH_EMOJILIST = PATH_NAME + "/../EmojiList.json"
PATH_TO_DATASET = PATH_NAME + "/Dataset"
PATH_TO_TRAIN = PATH_TO_DATASET + "/images/train"
PATH_TO_VAL = PATH_TO_DATASET + "/images/validation"

NUM_TRAIN_SAMPLES = 28821
NUM_VAL_SAMPLES = 7066
EPOCHS = 25
IMG_ROW, IMG_COL = 48, 48
INPUT_SHAPE = (IMG_ROW, IMG_COL, 1)
BATCH_SIZE = 32

f = open(PATH_EMOJILIST)
emojiList = json.load(f)["Emoji"]
for i, emoji in enumerate(emojiList):
    EMOJI_DICT[emoji] = i


if __name__ == "__main__":
    print(EMOJI_DICT)

