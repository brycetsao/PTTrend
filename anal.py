import sys
import jieba

seg_list = jieba.cut(sys.argv[1], cut_all=False)
print(" ".join(seg_list))
