import subprocess
import sys
import os

def compress_video(input_path, output_path, target_size_mb=10):
    """
    使用 ffmpeg 压缩视频到目标大小
    :param input_path: 输入视频路径
    :param output_path: 输出视频路径
    :param target_size_mb: 目标文件大小，单位 MB
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"{input_path} 不存在")

    # 获取视频时长（秒）
    cmd_duration = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of",
        "default=noprint_wrappers=1:nokey=1", input_path
    ]
    duration = float(subprocess.check_output(cmd_duration).decode().strip())

    # 计算目标比特率
    # 1 Byte = 8 bits, target_size_mb 转成 bits
    target_bitrate = (target_size_mb * 1024 * 1024 * 8) / duration
    # ffmpeg bitrate 单位 kbps
    target_bitrate_kbps = int(target_bitrate / 1000)

    print(f"视频时长: {duration:.2f}s, 目标比特率: {target_bitrate_kbps} kbps")

    # ffmpeg 压缩命令
    cmd_compress = [
        "ffmpeg", "-i", input_path,
        "-b:v", f"{target_bitrate_kbps}k",
        "-bufsize", f"{target_bitrate_kbps}k",
        "-maxrate", f"{target_bitrate_kbps}k",
        "-preset", "fast",
        "-y", output_path
    ]

    subprocess.run(cmd_compress, check=True)
    print(f"压缩完成，输出文件: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python compress_video.py 输入文件 输出文件 [目标大小MB]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    target_mb = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    compress_video(input_file, output_file, target_mb)

    # python compress_video.py input.mp4 output.mp4 10