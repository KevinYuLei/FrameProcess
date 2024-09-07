from utils.extract_frames_from_videos import extract_frames_from_videos
from utils.random_frame_selection import random_frame_selection


if __name__ == '__main__':
    # 设置要处理的视频文件夹和帧输出文件夹
    video_folder = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\videos'
    output_folder = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\frames_all'

    extract_frames_from_videos(
        video_folder, output_folder,
        frame_rate=30,
        output_image_format='jpg',
        jpg_quality=2)
    
    # 设置帧图片的源文件夹（之前生成帧的文件夹）
    source_frames_folder = output_folder
    # 设置保存随机抽取帧的输出文件夹
    output_selected_frames_folder = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\frames_selected'

    # 调用函数，每隔30帧随机抽取一帧
    random_frame_selection(
        source_frames_folder,
        output_selected_frames_folder,
        step=30)