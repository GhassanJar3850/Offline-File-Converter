from moviepy.editor import VideoFileClip
import os

def get_codec(output_format):
    format_codecs = {
        'mp4': 'libx264',
        'avi': 'png',
        'mkv': 'libx264',
        'mov': 'libx264',
        'webm': 'libvpx',
        'ogv': 'libtheora',
        'mpeg': 'mpeg2video'
    }
    return format_codecs.get(output_format, 'libx264')

def convert_video(input_file, output_format, output_dir=None):

    input_format = os.path.splitext(input_file)[-1][1:].lower()
    
    supported_formats = ['mp4', 'avi', 'mkv', 'mov', 'webm', 'ogv','mpeg']
    
    if input_format not in supported_formats:
        raise ValueError(f"Unsupported input format: {input_format}. Supported formats are {supported_formats}")
    
    output_filename = os.path.splitext(os.path.basename(input_file))[0] + '.' + output_format
    
    if output_dir:
        
        output_file = os.path.join(output_dir, output_filename)
    else:
        output_file = os.path.join(os.path.dirname(input_file), output_filename)
        
    clip = VideoFileClip(input_file)
    
    original_width, original_height = clip.size
    
    codec = get_codec(output_format)
    
    clip.write_videofile(output_file, codec=codec)
    
    print(f"Conversion complete: {input_file} to {output_file} with codec: {codec}")

input_video = "Resources/Video/ccc.mp4"
desired_output_format = "mov"
output_directory = "Outputs/Video"
convert_video(input_video, desired_output_format, output_directory)