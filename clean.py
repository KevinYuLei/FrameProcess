from utils.delete_folder_contents import delete_folder_contents

if __name__ == '__main__':
    # 设置要清空的文件夹路径
    folder_to_clear_1 = r'D:\DesktopShortcut\Project\MyUtils\frame_process\datasets\frames_all'
    folder_to_clear_2 = r'D:\DesktopShortcut\Project\MyUtils\frame_process\datasets\frames_selected'

    # 删除指定文件夹内的所有文件、子文件夹及其文件
    delete_folder_contents(folder_to_clear_1)
    delete_folder_contents(folder_to_clear_2)
