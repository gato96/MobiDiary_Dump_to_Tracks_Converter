import os
import json

# paths to dump files

import glob
import re
import uuid

datafolder = "data/eingang"  # 338 objects with a0_wayUUID attribute

userID = str(uuid.uuid4())


datafiles = glob.glob(datafolder + "/*.json")
for filename in datafiles:
    wayID = re.search("(?<=\[)(.*?)(?=\])", filename)[0]
    print(wayID)

    with open(filename) as json_file:
        data = json.load(json_file)

    data[0]["a0_wayUUID"] = wayID


    data[0]["a6_userID"] = data[0]["a7_userID"]
    print(data)


    with open("data/tracks/" + "MDTrack[" + wayID + "].json", 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
