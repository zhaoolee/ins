import pandas as pd
import os
import re
from datetime import datetime
import time
import pytz
import requests

website_info_data = pd.read_csv('./website_info.csv')
print(website_info_data)
for website_info_index, website_info_row in website_info_data.iterrows():
    print('=start=>>', website_info_index, website_info_row['Url'])
    try:
        website_info_row_url_result = requests.get(website_info_row['Url'], timeout=5)
        total_ms = str(int(website_info_row_url_result.elapsed.total_seconds()*1000))
        # 响应码为2开头,标注绿色,否则标注红色
        if website_info_row_url_result.status_code:
            website_info_row['Name'] = website_info_row['Name'] + (" 🟢"+ total_ms + "ms" if str(website_info_row_url_result.status_code).startswith("2") else "🔴")
    # 无法响应，标注红色
    except Exception as e:
        print('error==', e)
        website_info_row['Name'] = website_info_row['Name'] + "🔴"
    finally:
        print("finish", website_info_row['Url'], website_info_row['Name'])
website_info_md = website_info_data.to_markdown(index=False)
print(website_info_md)
readme_md = ""
with open(os.path.join(os.getcwd(),"EditREADME.md"),'r') as load_f:
    readme_md = load_f.read();
mail_re = r'--insStart----insEnd--'
reResult = re.findall(mail_re, readme_md)

in_datetime = datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
new_read_me = readme_md.replace(reResult[0], "\n\n" + "## 开源灵感库更新时间("+ in_datetime + ")\n\n" + website_info_md + "\n\n")
print('new_read_me',new_read_me)

with open(os.path.join(os.getcwd(),"README.md"),'w') as load_f:
    load_f.write(new_read_me)