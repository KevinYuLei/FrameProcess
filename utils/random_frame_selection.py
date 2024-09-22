import os
import random
import shutil


def random_frame_selection(source_dir, output_dir, step=30):
    """
    从帧图片文件夹中每隔 step 帧随机抽取一帧并保存到相应的输出文件夹中。

    Args:
        source_dir (str): 包含帧图片的主目录，每个子文件夹代表一个视频的帧图像。
        output_dir (str): 保存随机抽取帧的输出目录。
        step (int, optional): 隔多少帧抽取一帧。 Defaults to 30.
    """
    # 如果输出文件夹不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历主文件夹中的每个子文件夹（每个子文件夹对应一个视频的帧图片）
    for video_frames_folder in os.listdir(source_dir):
        video_frames_folder_path = os.path.join(source_dir, video_frames_folder)
        # 检查是否为文件夹
        if os.path.isdir(video_frames_folder_path):
            # 获取该文件夹内的所有帧文件
            frame_files = sorted([f for f in os.listdir(video_frames_folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
            
            # 如果帧文件数量大于 step
            if len(frame_files) > step:
                # 创建输出文件夹
                output_video_folder = os.path.join(output_dir, video_frames_folder)
                if not os.path.exists(output_video_folder):
                    os.makedirs(output_video_folder)
                    print(f"帧图像保存路径: '{output_video_folder}' 不存在，已成功创建！")
                else:
                    print(f"帧图像保存路径: '{output_video_folder}' 已存在，停止抽取该视频:{video_frames_folder} 帧图像！")
                    continue
                
                # 按照步长遍历并随机选取每组中的一帧
                for i in range(0, len(frame_files), step):
                    selected_frame = random.choice(frame_files[i:i+step])
                    source_frame_path = os.path.join(video_frames_folder_path, selected_frame)
                    output_frame_path = os.path.join(output_video_folder, selected_frame)
                    
                    # 复制选中的帧到输出文件夹
                    shutil.copy(source_frame_path, output_frame_path)
                    print(f"Selected frame: {selected_frame} from {video_frames_folder}")
            else:
                print(f"Not enough frames in {video_frames_folder} to sample with step {step}.")


if __name__ == '__main__':
    # 设置帧图片的源文件夹（之前生成帧的文件夹）
    source_frames_folder = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\frames_all'
    # 设置保存随机抽取帧的输出文件夹
    output_selected_frames_folder = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\frames_selected'

    # 调用函数，每隔30帧随机抽取一帧
    random_frame_selection(
        source_frames_folder,
        output_selected_frames_folder,
        step=30)
