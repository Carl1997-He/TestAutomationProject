import os
import shutil
import filecmp

class FileHandler:
    def __init__(self, system_name, upload_dir):
        self.system_name = system_name
        self.upload_dir = upload_dir

    def upload_file(self, source_file):
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)
        dest_file = os.path.join(self.upload_dir, os.path.basename(source_file))
        shutil.copy(source_file, dest_file)
        return dest_file

    def compare_files(self, file1, file2):
        if not (os.path.exists(file1) and os.path.exists(file2)):
            return False, "文件缺失"
        if filecmp.cmp(file1, file2, shallow=False):
            return True, "文件一致"
        else:
            return False, "文件内容不一致"