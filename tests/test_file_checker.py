from scripts.pages.file_handler import FileHandler

class SystemChecker:
    def __init__(self, system_name, upload_dir):
        self.file_handler = FileHandler(system_name, upload_dir)

    def pre_market_upload(self, txt_file, flg_file):
        self.file_handler.upload_file(txt_file)
        self.file_handler.upload_file(flg_file)

    def post_market_compare(self, txt_file, flg_file):
        result, msg = self.file_handler.compare_files(txt_file, flg_file)
        print(f"{self.file_handler.system_name}: {msg}")
        return result

if __name__ == "__main__":
    systems = {
        "bnt": SystemChecker("bnt", "../files/bnt_files"),
        "fex": SystemChecker("fex", "../files/fex_files"),
        "ipo": SystemChecker("ipo", "../files/ipo_files")
    }
    for system in systems.values():
        system.pre_market_upload("sample.txt", "sample.flg")
        system.post_market_compare("../files/bnt_files/sample.txt", "../files/bnt_files/sample.flg")