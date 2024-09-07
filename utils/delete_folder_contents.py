import os
import shutil

def delete_folder_contents(folder_path):
    """
    删除指定文件夹内的所有文件、子文件夹及其文件。
    
    Args:
        folder_path (str): 要清空的文件夹路径。
    
    Raises:
        FileNotFoundError: 如果文件夹路径不存在，将抛出此异常。
        PermissionError: 如果没有权限删除文件或文件夹，将抛出此异常。
    """
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    
    # 遍历文件夹内容，逐个删除
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # 如果是文件夹，递归删除文件夹及其内容
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print(f"Deleted folder: {file_path}")
        # 如果是文件，直接删除
        elif os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        else:
            print(f"Skipped: {file_path}")

if __name__ == '__main__':
    # 设置要清空的文件夹路径
    folder_to_clear_1 = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\frames_all'
    folder_to_clear_2 = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\frames_selected'
    
    # 删除指定文件夹内的所有文件、子文件夹及其文件
    delete_folder_contents(folder_to_clear_1)
    delete_folder_contents(folder_to_clear_2)
