'''
公用工具方法
'''
import struct
def covertFileSizeUnit(fileSize):
    '''
    转换文件单位
    :param fileSize: 文件大小
    :return: 转换后的文件大小字符串
    '''
    result = fileSize
    strUnit = 'B'
    perUnit = 1024.0
    if(type(1) != type(fileSize)):
        return str(result)
    if(result > 1000):
        strUnit = 'KB'
        result = result / perUnit
    if(result > 1000):
        strUnit = 'MB'
        result = result / perUnit
    if(result > 1000):
        strUnit = 'GB'
        result = result / perUnit
    result = round(result, 2)
    return str(result) + strUnit

def getEmoji():
    '''
    获取微软输入法的emoji
    :return: emoji列表
    '''
    emoji = []
    # 把str类型的表情符号转换成bytes类型
    start = int.from_bytes('😀'.encode(), byteorder='big', signed=False)
    end = int.from_bytes('😼'.encode(),byteorder='big', signed=False)

    # 对bytes编码进行递增
    for str in range(start, end, 1):
        # 把bytes类型表情符号转换成str类型，并存储
        emoji.append(struct.pack('>L', str).decode())
    return emoji

if __name__ == '__main__':
    fileSizeTotal = 2819017219
    print(covertFileSizeUnit(fileSizeTotal))
    print(len(getEmoji()), getEmoji())