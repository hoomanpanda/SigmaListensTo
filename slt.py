import argparse
import os
import subprocess

SigmaListens = 'SigmaListens.mp4'

# Set up command-line argument parser
parser = argparse.ArgumentParser(description='Sigma will listen to the music of your choice.')
parser.add_argument('SigmaMusic', help='path to Sigma music')
parser.add_argument('-o', '--output', default='', help='path for output')
args = parser.parse_args()

# Extract the base filename and extension from the input file
input_basename, input_ext = os.path.splitext(os.path.basename(args.SigmaMusic))

# Construct the output filename by combining the base filename of the input file with 'SigmaListensTo' and '.mp4'
if args.output:
    output_filename = args.output
else:
    output_filename = 'SigmaListensTo' + input_basename + '.mp4'

# Use FFmpeg to extract the audio from the audio file.
subprocess.run(['ffmpeg', '-i', args.SigmaMusic, '-vn', '-acodec', 'copy', 'temp_audio.aac'], check=True)

# Use FFmpeg to replace the audio in the video file with the extracted audio.
subprocess.run(['ffmpeg', '-i', SigmaListens, '-i', 'temp_audio.aac', '-c:v', 'copy', '-map', '0:v:0', '-map', '1:a:0', '-shortest', output_filename], check=True)

# Remove the temporary audio file.
print('Removing temporary file')
try:
    os.remove('temp_audio.aac')
except OSError as e:
    print('Error:', e)

print('Audio replaced successfully! Output file:', output_filename)
