import urllib.request

def download_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter img URL to download:')
file_name = input('Enter file name to save as:')

download_jpg(url,'images/', file_name) # create images folder in your directory, it will be saved there.

