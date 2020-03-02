# E. Culurciello
# March 2020

# find all moview files and convert them to mp4 with ffmpeg
# this will compress all files with the latest algorithms

import os, sys

path = sys.argv[1]

print('Directory to be processed:', path)

print('Size of directory BEFORE conversion:')
cmd = "du -sh '" + sys.argv[1] + "'"
os.system(cmd)
print('')

# find all movie files:
original_files = []
converted_files = []
orig_size_video_files = 0
conv_size_video_files = 0
count_files = 0
count_processed = 0

# first count files to get an idea of progress:
for root, d_names, f_names in os.walk(path):
    for f in f_names:
        # modify this list of extenstions to process the files you are interested in:
        if f.endswith(".mov") or f.endswith(".MOV") or f.endswith(".avi") or f.endswith(".AVI"):
            count_files += 1

print('Number of files to be processed:', count_files)

# now process:
for root, d_names, f_names in os.walk(path):
    for f in f_names:
        # modify this list of extenstions to process the files you are interested in:
        if f.endswith(".mov") or f.endswith(".MOV") or f.endswith(".avi") or f.endswith(".AVI"):
            count_processed += 1
            fpre, fext = os.path.splitext(f)
            orig_file = os.path.join(root, f)
            orig_size_video_files += os.path.getsize(orig_file)
            conv_file = os.path.join(root, fpre) + ".mp4"
            # conv_file = os.path.join(root, fpre) + "_ec.mp4"
            # cmd = "ls -aGlSr '" + os.path.join(root, f) + "'"
            cmd = "ffmpeg -hide_banner -loglevel panic -i '" + orig_file + "' '" + conv_file + "'"
            # print(cmd)
            # input()
            # convert file:
            returned_value = os.system(cmd)  # returns the exit code
            # print('returned value:', returned_value)
            if not returned_value:
                os.remove(orig_file) # delete original movie file
                print('Conversion successful; Removed file:', orig_file)
            orig_size_video_files += os.path.getsize(conv_file)
            original_files.append(orig_file)
            converted_files.append(conv_file)
            print('Processed file number', count_processed, 'out of:', count_files)
            

print('Found and processed {} files'.format(len(original_files)))
print('List of original video files (processed and deleted):')
print(original_files)
print('Log of converted video files:')
print(converted_files)

print('Size of directory AFTER conversion:')
cmd = "du -sh '" + sys.argv[1] + "'"
os.system(cmd)
print('')

print('size of the video files before conversion:', orig_size_video_files)
print('size of video files after conversion:', conv_size_video_files)
