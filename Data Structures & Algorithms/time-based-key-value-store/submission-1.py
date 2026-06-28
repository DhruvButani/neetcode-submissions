from collections import defaultdict
from collections import OrderedDict

class TimeMap:

    def __init__(self):
        self.keystore = defaultdict(OrderedDict) # key -> {ts: value}
                           # alice -> {1: happy, 3: sad}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        
        if timestamp in self.keystore[key]:
            return self.keystore[key][timestamp]
        else:
            timestamps = list(self.keystore[key].keys())

            if len(timestamps) ==0:
                return ""
            
            if len(timestamps) ==1:
                return self.keystore[key][timestamps[0]] if timestamps[0]<timestamp else ""

            # floor search
            res = -1 
            target  = timestamp
            l, r = 0, len(timestamps)-1
            while l <= r:
                mid = (r+l) // 2
                print(l, r, mid, timestamps)

                if timestamps[mid] > target:
                    r = mid-1
                else:
                    res = max(res, mid)
                    l = mid + 1
            if res > -1:
                return self.keystore[key][timestamps[res]]
            else:
                return ""



        # use a dict of dict
            # key : alice
                # value : {1:happy, 3:sad}
                # but when I get timeMap.get("alice", 2); 
                # I don't have a key ... so I need to find the lower key 
                # ordered dict would be helpful, since the timestamps are increasing
                    # I could loop over the dict until I find the key < 2
                    # I can look at the keys   [1, 3]
                    # do a binary search over the keys to see if target =2 is present