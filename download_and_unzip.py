

from fileinput import filename
from io import BytesIO
from urllib.request import urlopen
import urllib
from zipfile import ZipFile
from datetime import datetime
import pytz,os,glob
import requests

class DownloadMethods:

#   this function will return the address of all the files if downloading and unzipping is succesful
#   else it will return 0
# pass the url of the zip file you want to download  
    def download_and_unzip(self,address):
        # if the file is already downloaded then skip
        dt = datetime.now().date()
        newDate=dt.strftime('%d''%b''%Y').upper()
        
        # Try making the request
        try:
            url = urllib.request.urlopen(address,timeout=2)
    
    #   if exceptions is handled function won't terminate
    #   you can use (return, raise, exit(0))
    #   but for some unknown reason return not working here
        except Exception as e:
            print(f'########{str(e)}########')
            return 0
            
    #   it executes only when there is no error
        else:
            files=[]        
            with ZipFile(BytesIO(url.read())) as my_zip_file:
                for contained_file in my_zip_file.namelist():     
                    #  you can pass the directory address where file to be downloaded as
                    #   ( "path/to/file/directory"+contained_file )
                    with open(( contained_file ), "wb") as output:                        
                        for line in my_zip_file.open(contained_file).readlines():
                            # print(line)
                            output.write(line)
                            
                    #  you can pass the directory address where file to be downloaded as
                    #( "path/to/file/directory"+contained_file )
                        files.append(contained_file)
            return files


dm=DownloadMethods()
dm.download_and_unzip('https://www1.nseindia.com/content/historical/EQUITIES/2022/OCT/cm18OCT2022bhav.csv.zip')