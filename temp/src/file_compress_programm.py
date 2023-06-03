import os
import subprocess
import time
import csv
from tqdm import tqdm

zip_app = r'C:\Program Files\7-Zip\7z.exe'


def get_data(location):
    file_data = []  # Initialize an empty list to hold the file data
    for root, directories, files in os.walk(
            location):  # Iterate over the directory and its subdirectories using os.walk()
        for filename in files:  # Iterate over each file in the current directory
            filepath = os.path.join(root, filename)  # Construct the full path of the file
            size_bytes = os.path.getsize(filepath)  # Get the size of the file in bytes
            size_mb = size_bytes / (1024 * 1024)  # Convert the size from bytes to megabytes
            file_data.append({'filename': filename, 'path': filepath, 'size': size_mb})  # Add the file data to the list
    process_data(file_data)


def process_data(file_data):
    # file_info = []
    for file_info in tqdm(file_data):
        file_to_compress = file_info['path']
        filename = file_info['filename']
        archive_extension = '.7z'
        if not filename.endswith(archive_extension):
            archive_name = os.path.join(os.path.dirname(file_to_compress), f'{filename}{archive_extension}')
        else:
            archive_name = os.path.join(os.path.dirname(file_to_compress), filename)

        start_time = time.time()
        subprocess.call([zip_app, 'a', '-t7z', archive_name, file_to_compress], stdout=subprocess.DEVNULL)
        end_time = time.time()
        total_time = end_time - start_time
        compressed_file_size_bytes = os.path.getsize(archive_name)
        compressed_file_size_mb = compressed_file_size_bytes / (1024 * 1024)
        file_info.update(
            {'c_filename': filename,
             'c_path': archive_name,
             'c_size': compressed_file_size_mb,
             'c_total_time': total_time})

        # print(f"Time taken to compress {filename}: {total_time:.2f} seconds")

    write_log(file_data)


def write_log(file_data):
    # location = 'C:/MPS_Script/output/'
    # csv_file_path = 'path'

    with open(location + 'new.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(
            ['Filename', 'Size (MB)', 'Path', 'Compressed Filename', 'Compressed Size (MB)', 'Compressed Path',
             'Compression Time', 'Space Saved (MB)'])

        # writer = csv.writer(csv_file)

        for data in file_data:
            original_filename = data['filename']
            original_size_mb = data['size']
            original_filepath = data['path']

            compressed_filename = data['c_filename']
            compressed_size_mb = data['c_size']
            compressed_filepath = data['c_path']
            compression_time = data['c_total_time']
            space_saved = original_size_mb - compressed_size_mb

            writer.writerow(
                [original_filename, '{:.2f}'.format(original_size_mb), original_filepath, compressed_filename,
                 '{:.2f}'.format(compressed_size_mb), compressed_filepath, '{:.2f}'.format(compression_time),
                 '{:.2f}'.format(space_saved)])


# location = 'C:\\Django Project\\django_project\\HQVFX'
get_data('C:\\Django Project\\djangoproject1\\HQVFX1\\')
