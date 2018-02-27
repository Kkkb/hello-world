# -*- coding: utf-8 -*-
# batch_file_rename.py
# Created: 6th August 2012

'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
批量重命名给定目录下的文件，
将你指定的扩展名重命名为新扩展名
'''
#just checking
__author__ = 'Craig Richards'
__version__ = '1.0'

import os
import argparse

def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    '''
    # files = os.listdir(work_dir)
    # os.listdir()方法用于返回指定路径下的文件和文件夹名字的列表
    for filename in os.listdir(work_dir):
        # Get the file extension
        # os.path.split(filename)用于将文件或文件夹名字分割成前缀名和后缀名二元组返回
        split_file = os.path.splitext(filename)
        # 将文件后缀名赋值给变量file_ext
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        # 如果给定的扩展名与文件扩展名匹配
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            newfile = split_file[0] + new_ext 

            # Write the files
            os.rename(
                os.path.join(work_dir, filename), # join函数用于拼接路径
                os.path.join(work_dir, newfile)
            )

# 命令行解析
def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser

def main():
    '''
    This will be called if the script is directly invoked.
    '''
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args()) # vars()函数返回对象object的属性及属性值的字典

    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()