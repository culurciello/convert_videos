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
for root, d_names, f_names in os.walk(path):
    for f in f_names:
        if f.endswith(".MOV") or f.endswith(".AVI"):
        # if f.endswith(".MOV") or f.endswith(".MP4") or f.endswith(".AVI"):
            fpre, fext = os.path.splitext(f)
            orig_file = os.path.join(root, f)
            conv_file = os.path.join(root, fpre) + ".mp4"
            # conv_file = os.path.join(root, fpre) + "_ec.mp4"
            # cmd = "ls -aGlSr '" + os.path.join(root, f) + "'"
            cmd = "ffmpeg -i '" + orig_file + "' '" + conv_file + "'"
            # print(cmd)
            # input()
            # convert file:
            returned_value = os.system(cmd)  # returns the exit code
            # print('returned value:', returned_value)
            if not returned_value:
                os.remove(orig_file) # delete original movie file
                print('Conversion successful; Removed file:', orig_file)
            original_files.append(orig_file)
            converted_files.append(conv_file)

print('\nFound and processed {} files'.format(len(original_files)))
print('\nList of original video files (processed and deleted):')
print(original_files)
print('\nLog of converted video files:')
print(converted_files)



print('Size of directory AFTER conversion:')
cmd = "du -sh '" + sys.argv[1] + "'"
os.system(cmd)
print('')
