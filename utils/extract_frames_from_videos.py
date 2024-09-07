import os
from ffmpy import FFmpeg


def extract_frames_from_videos(
    video_dir, output_dir, 
    frame_rate=30, 
    additional_video_formats: list=None, 
    output_image_format='jpg',
    jpg_quality=2,
    png_compression=9):
    """
    从指定视频文件夹中提取帧，并将其保存为图像文件到指定输出文件夹中。

    Args:
        video_dir (str): 包含视频文件的目录路径。需要提取帧的视频应存储在此目录下。
        output_dir (str): 保存提取帧图片的输出目录路径。如果目录不存在，则会自动创建。
        frame_rate (int, optional): 每秒提取的帧数（帧率）。默认为30，即每秒提取30帧。
        additional_video_formats (list, optional): 额外支持的视频格式列表，格式以扩展名表示（如['.flv', '.webm']）。
            默认支持 .mp4, .avi, .mov, .mkv 格式。
        output_image_format (str, optional): 指定输出帧图片的格式。默认为 'jpg'，可设置为 'png'。
        jpg_quality (int, optional): JPEG 图片的质量，值越小质量越高，范围是 2 到 31，默认为 2。
        png_compression (int, optional): PNG 图片的压缩级别，范围是 0 到 9，0 表示无压缩，9 表示最大压缩。

    Raises:
        ValueError: 当提供不支持的图片格式时，抛出此错误。
    """
    
    # 默认支持的视频格式
    video_formats = [".mp4", ".avi", ".mov", ".mkv"]
    if additional_video_formats is not None:
        video_formats.extend(additional_video_formats)
        video_formats = list(set(video_formats))
        
    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"帧图像保存路径: '{output_dir}' 不存在，已成功创建！")
    else:
        print(f"帧图像保存路径: '{output_dir}' 已存在！")

    # 遍历指定的视频文件夹内的所有文件
    for filename in os.listdir(video_dir):
        # 检查文件是否是视频文件（根据文件扩展名筛选）
        if any(filename.endswith(ext) for ext in video_formats):
            video_path = os.path.join(video_dir, filename)
            filename_dir = os.path.join(output_dir, os.path.splitext(filename)[0])
            if not os.path.exists(filename_dir):
                os.makedirs(filename_dir)
                print(f"帧图像保存子路径: '{output_dir}' 不存在，已成功创建！")
            else:
                print(f"帧图像保存子路径: '{output_dir}' 已存在！")
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0], os.path.splitext(filename)[0]+f'_frame_%05d.{output_image_format}')

            # 构建输出参数，基于不同图片格式指定不同的质量选项
            if output_image_format.lower() == 'jpg' or output_image_format.lower() == 'jpeg':
                output_params = f'-vf fps={frame_rate} -q:v {jpg_quality}'
            elif output_image_format.lower() == 'png':
            # 如果是 PNG 格式，使用 -compression_level 参数控制压缩级别
                output_params = f'-vf fps={frame_rate} -compression_level {png_compression}'
            else:
                raise ValueError(f"Unsupported output image format: {output_image_format}")
            # 使用ffmpy进行切帧操作
            ff = FFmpeg(
                inputs={video_path: None},
                outputs={output_path: output_params}
            )
            print(f"Extracting frames from {filename}...")
            ff.run()
            print(f"Frames saved to {output_path}")


if __name__ == '__main__':
    # 设置要处理的视频文件夹和帧输出文件夹
    video_folder = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\videos'
    output_folder = r'D:\DesktopShortcut\Project\MyUtils\FrameProcess\datasets\frames_all'

    extract_frames_from_videos(
        video_folder, output_folder,
        frame_rate=30,
        output_image_format='jpg',
        jpg_quality=2)
