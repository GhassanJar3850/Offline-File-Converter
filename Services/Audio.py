from moviepy.editor import AudioFileClip
import os

def get_audio_codec(output_format):
    format_codecs = {
        'mp3': 'libmp3lame',
        'wav': None,
        'ogg': 'libvorbis',
        'aac': 'aac',
        'flac': 'flac',
        'm4a': 'aac'
    }
    return format_codecs.get(output_format, None)

def convert_audio(input_file, output_format, output_dir=None):
    input_format = os.path.splitext(input_file)[-1][1:].lower()
    
    supported_formats = ['mp3', 'wav', 'ogg', 'aac', 'flac', 'm4a']
    
    if input_format not in supported_formats:
        formatted_supported_formats = ', '.join(supported_formats)
        raise ValueError(f"Unsupported input format: {input_format}. Supported formats are {formatted_supported_formats}")
    
    output_filename = os.path.splitext(os.path.basename(input_file))[0] + '.' + output_format
    
    if output_dir:
        output_file = os.path.join(output_dir, output_filename)
    else:
        output_file = os.path.join(os.path.dirname(input_file), output_filename)
    
    audio_clip = AudioFileClip(input_file)
    
    codec = get_audio_codec(output_format)
    
    audio_clip.write_audiofile(output_file, codec=codec)
    
    print(f"Conversion complete: {input_file} to {output_file} with codec: {codec}")
