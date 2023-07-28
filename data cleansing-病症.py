import os

def concat(file_list,folder_path,file_new_name):

    str1 = ''
    for file_name in file_list:
        file_name1 = folder_path + file_name
        with open(file_name1,'r',encoding='utf8') as file:
            text = file.read().strip().split('\n')
            for line in text:
                str1 += '1'+'\t'+line+'\n'+'0'+'\t'+line[::-1]+'\n'
        with open(file_new_name, 'w', encoding='utf8') as f:
            f.write(str1)
if __name__ == '__main__':
    folder_path = "structured/noreview/"
    file_list = os.listdir(folder_path)
    file_new_name = 'result_1.csv'
    concat(file_list,folder_path,file_new_name)