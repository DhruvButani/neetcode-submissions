class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.dictionary):
            self.dictionary[key] = [[value,timestamp]]

        else:
            self.dictionary[key].append([value,int(timestamp)])





    def get(self, key: str, timestamp: int) -> str:
        

        if(key not in self.dictionary):
            return ""

        #bs on seocnd index of array
        arr = self.dictionary[key]
        


        left = 0
        right = len(arr)-1

        ret = arr[0][0]

        if(arr[0][1]>timestamp):
            return ""

        while(left<=right):

            mid = (left+right)//2


            if(int(arr[mid][1])<=timestamp):
                left = mid+1
                ret = arr[mid][0]

            else:
                right = mid-1


        return ret

