import jieba
import pickle
import numpy as np
class Counter(dict):
    def __missing__(self, key):
        return 0

class Feature:
    def __init__(self):
        try:
            with open('c_dict.pkl', 'rb') as file:
                self.chinese_dict = pickle.load(file)
                print("Load Chinese Dict from File")
        except:
            self.chinese_dict = Counter()
        self.index = len(self.chinese_dict) + 1

    def features(self, str):
        x = np.zeros(1000000, dtype=np.int)
        seg_list = jieba.cut(str)
        for i in seg_list:
            if self.chinese_dict[i] == 0:
                self.chinese_dict[i] = self.index
                self.index += 1
            x[self.chinese_dict[i]] += 1
        return x

    def store(self):
        with open('c_dict.pkl', 'wb') as file:
            pickle.dump(self.chinese_dict, file, pickle.HIGHEST_PROTOCOL)
