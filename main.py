import pandas as pd
import os
import re
from datetime import datetime
import time
import pytz

website_info_data = pd.read_csv('./website_info.csv')
website_info_md = website_info_data.to_markdown(index=False)
print(website_info_md)
readme_md = ""
with open(os.path.join(os.getcwd(),"README.md"),'r') as load_f:
    readme_md = load_f.read();

mail_re = r'--insStart--([.\S\s]*)--insEnd--'
reResult = re.findall(mail_re, readme_md)


in_datetime = datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

new_read_me = readme_md.replace(reResult[0], "\n\n" + "## 开源灵感库更新时间("+ in_datetime + ")\n\n" + website_info_md + "\n\n")
print('new_read_me',new_read_me)

with open(os.path.join(os.getcwd(),"README.md"),'w') as load_f:
    load_f.write(new_read_me)