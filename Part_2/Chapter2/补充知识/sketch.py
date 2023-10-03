import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

# 每一个开头的第一个数代表的意思就是格式化对应第几个数
# {0:2d} 就是.format() 里面对应的第一个数字，是一个 int 按照宽度为 2 格式化
ROW_FMT = '{0:4d} @ {1:3d} {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):    # 这里倒序，所以是从大到小的
        position = bisect_fn(HAYSTACK, needle)  # 找到要插入的位置
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    # 输入参数控制
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    # haystack 的数拿出来，宽度为 2 的排布
    # 不然个数位 1 的就站一个空，排起来不好看
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
