import os
import random
import string

def generate_random_text_file(filename, size_mb):
    size_bytes = size_mb * 1024 * 1024  # 将MB转换为字节
    chars = string.ascii_letters + string.digits
    chunk_size = 1024 * 1024  # 每次写入1MB

    with open(filename, 'w') as file:
        for _ in range(size_bytes // chunk_size):
            file.write(''.join(random.choices(chars, k=chunk_size)))

    print(f"{filename} 已生成，大小为 {size_mb}MB")

file_dict={
    "16MB": 16,
    "32MB": 32,
    "64MB": 64,
    "128MB": 128,
    "256MB": 256,
    "512MB": 512
}
filename = ["16MB", "32MB", "64MB", "128MB", "256MB", "512MB"]
for name in filename:
    print(name)
    generate_random_text_file('D:\\EDI-QZF\\experiment\\AppVendor\\'+f'{name}.txt', file_dict[name])