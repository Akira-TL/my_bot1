import os


def path_create(path:str):
    """创建文件夹,带有反斜杠或'/'但不以此为结尾"""
    if '/' in path and '\\' in path:
        if '\\' in path:
            path = path.replace('\\','/')
        tail = path.split('/')[-1]
    else:
        # print(f'<<<文件路径格式错误，请检查路径是否存在“/”和“\”>>>')
        raise Exception('FilePathFormatError:文件路径格式错误，请检查路径是否存在“/”和“\”')
    if os.path.exists(path):
        os.mkdir(path)
    else:
        path_next = path[:-len(tail)-1]
        path_create(path_next)
    print(f'<<<创建{path}成功>>>')
    return None