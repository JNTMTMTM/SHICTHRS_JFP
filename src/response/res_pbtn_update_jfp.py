
from copy import deepcopy
from nt import write
from functions.jfp.func_jfp_verify_sac_jfp_order import verify_sac_jfp_order
from functions.io.func_io_write_json_file import write_json_file
from functions.io.func_io_read_json_file import read_json_file
from PySide6.QtWidgets import QMessageBox



def res_pbtn_update_jfp(self) -> None:
    if not verify_sac_jfp_order(self.file_data):
        write_json_file(self.file_data , self.file_path)
        QMessageBox.information(self , 'SAC_JFP 提示' , 'SAC_JFP 更新成功。')
        self.file_data = read_json_file(self.file_path)

    else:
        QMessageBox.warning(self , 'SAC_JFP 警告' , '该json文件的SAC_JFP命令不需要更新。')
