import pandas as pd
# 输出便于阅读的Markdown
log_website_info_data = pd.read_csv("./website_info.csv")
for website_info_index, website_info_row in log_website_info_data.iterrows():
    print("## " + str(website_info_index+1) + ". " + website_info_row['Name'] + "\n\n**网址**: " + website_info_row['Url'] + "\n\n**简介**: " + website_info_row['Description'] + "\n\n" + "**标签**: " +website_info_row['Tag'] +"\n\n")