import pandas as pd
import os
import re
from datetime import datetime
import time
import pytz
import requests


def get_all_tag(website_info_data):
    all_tag = []
    all_tag_info_data = []
    # 遍历数据,获取所有的tag
    for website_info_index, website_info_row in website_info_data.iterrows():
        tag_list = website_info_row["Tag"].split(";")
        pure_tag_list = []
        for tag in tag_list:
            pure_tag = tag.strip()
            if pure_tag != "":
                pure_tag_list.append(pure_tag)
                if pure_tag not in all_tag:
                    all_tag.append(pure_tag)
                    all_tag_info_data.append([])
        print("pure_tag_list", pure_tag_list)
        print(
            "tag==>>",
            website_info_index,
            website_info_row["Tag"],
            "pure_tag_list==>>",
            pure_tag_list,
        )

    # 遍历所有数据,将数据放到all_tag_info_data 中
    for website_info_index, website_info_row in website_info_data.iterrows():
        tag_list = website_info_row["Tag"].split(";")
        for tag in tag_list:
            pure_tag = tag.strip()
            if pure_tag != "":
                all_tag_info_data[all_tag.index(pure_tag)].append(website_info_row)

    print("all_tag", all_tag, "all_tag_info_data", all_tag_info_data)
    return {"all_tag": all_tag, "all_tag_info_data": all_tag_info_data}


def short_url(url):
    result = ""
    url = url.lstrip("http://")
    url = url.lstrip("https://")
    url = url.lstrip("www.")
    url = url.rstrip("/")

    if len(url) > 30:
        result = url[0:30] + "..."
    else:
        result = url
    return result


def replaceTemplate(template, reInfo, data):

    reResult = re.findall(reInfo, template)
    new_read_me = template.replace(reResult[0], data)
    return new_read_me


def create_tag_table_html(tag_name, tag_info_data):
    print("==create_tag_table_html", tag_name)
    website_info_html = "<table>"
    website_info_html = (
        website_info_html
        + "<tr>"
        + "<td width='400'>"
        + "<span>(づ｡◕‿‿◕｡)づ</span><br/><span>Name</span>"
        + "</td>"
        + "<td>"
        + "<span> (●ﾟωﾟ●)</span><br/><span>Description</span>"
        + "</td>"
        + "</tr>"
    )
    for info_data in tag_info_data:
        print(
            "==>>",
            {
                "Name": info_data["Name"],
                "Url": info_data["Url"],
                "Description": info_data["Description"],
            },
        )
        website_info_html = (
            website_info_html
            + "<tr>"
            + "<td>"
            + info_data["Name"]
            + "</td>"
            + "<td>"
            + info_data["Description"]
            + "</td>"
            + "</tr>"
        )

    website_info_html = website_info_html + "</table>"

    return website_info_html


def main():
    # 读取csv文件
    website_info_data = pd.read_csv("./website_info.csv")
    # 反转数据,保证最新的数据在最前面
    website_info_data = website_info_data.reindex(index=website_info_data.index[::-1])
    print(website_info_data)
    # 遍历数据
    for website_info_index, website_info_row in website_info_data.iterrows():
        print("=start=>>", website_info_index, website_info_row["Url"])
        # 检测网站可用性,记录请求时间,完成数据拼接
        try:
            # 检测网站是否正常
            website_info_row_url_result = requests.get(
                website_info_row["Url"], timeout=5
            )
            total_ms = str(
                int(website_info_row_url_result.elapsed.total_seconds() * 1000)
            )
            # 响应码为2开头,标注绿色,否则标注红色
            if website_info_row_url_result.status_code:
                website_info_row["Name"] = (
                    "<span style='font-weight: 600'>"
                    + website_info_row["Name"]
                    + "</span>"
                    + "<span>"
                    + (
                        " 🟢 " + total_ms + "ms"
                        if str(website_info_row_url_result.status_code).startswith("2")
                        else " 🔴"
                    )
                    + "</span><br/>"
                )
        # 无法响应，标注红色
        except Exception as e:
            print("error==", e)
            website_info_row["Name"] = (
                "<span style='font-weight: 600'>"
                + website_info_row["Name"]
                + " 🔴"
                + "</span><br/>"
            )
        finally:
            website_info_row["Name"] = (
                "<span>"
                + website_info_row["Name"]
                + "</span>"
                + "<a href='"
                + website_info_row["Url"]
                + "'>"
                + (short_url(website_info_row["Url"]))
                + "</a>"
            )
            print("finish", website_info_row["Url"], website_info_row["Name"])
    # 完成table数据拼接
    website_info_html = "<table>"
    website_info_html = (
        website_info_html
        + "<tr>"
        + "<td width='400'>"
        + "<span>(づ｡◕‿‿◕｡)づ</span><br/><span>Name</span>"
        + "</td>"
        + "<td>"
        + "<span> (●ﾟωﾟ●)</span><br/><span>Description</span>"
        + "</td>"
        + "<td width='300'>"
        + "<span> ︿(￣︶￣)︿</span><br/><span>Tag</span>"
        + "</td>"
        + "</tr>"
    )
    for website_info_index, website_info_row in website_info_data.iterrows():
        website_info_html = (
            website_info_html
            + "<tr>"
            + "<td>"
            + website_info_row["Name"]
            + "</td>"
            + "<td>"
            + website_info_row["Description"]
            + "</td>"
            + "<td>"
            + website_info_row["Tag"]
            + "</td>"
            + "</tr>"
        )
    website_info_html = website_info_html + "</table>"
    # 根据EditREADME.md模板,替换占位符, 生成最终数据
    readme_md = ""
    with open(os.path.join(os.getcwd(), "EditREADME.md"), "r") as load_f:
        readme_md = load_f.read()
    mail_re = r"--insStart----insEnd--"
    in_datetime = datetime.fromtimestamp(
        int(time.time()), pytz.timezone("Asia/Shanghai")
    ).strftime("%Y-%m-%d %H:%M:%S")
    all_info_content = (
        "\n\n"
        + "## 开源灵感库已收录"
        + str(len(website_info_data))
        + "束灵感INS!"
        + "(～￣▽￣)～更新时间("
        + in_datetime
        + ")\n\n"
        + website_info_html
        + "\n\n"
    )
    new_read_me = replaceTemplate(readme_md, mail_re, all_info_content)
    print("new_read_me", new_read_me)

    # 生成类别数据
    tag_re = r"--tagStart----tagEnd--"
    all_tag_result = get_all_tag(website_info_data)
    all_tag = all_tag_result["all_tag"]
    all_tag_info_data = all_tag_result["all_tag_info_data"]
    print("==all_tag_info_data==", all_tag_info_data)
    print("==all_tag==", all_tag)
    all_tag_content = ""

    for tag_content in all_tag:
        tag_html = create_tag_table_html(
            tag_content, all_tag_info_data[all_tag.index(tag_content)]
        )
        tag_whole_content = "## " + tag_content + "\n\n" + tag_html + "\n\n"
        all_tag_content = all_tag_content + tag_whole_content

    new_read_me = replaceTemplate(new_read_me, tag_re, all_tag_content)

    # 添加索引锚点
    tag_index_info = ""
    for tag_index, tag_content in enumerate(all_tag):
        if tag_index != (len(all_tag) - 1):
            tag_index_info = (
                tag_index_info
                + "<a href='#"
                + tag_content
                + "'>"
                + tag_content
                + "</a>"
                + ", "
            )
        else:
            tag_index_info = (
                tag_index_info
                + "<a href='#"
                + tag_content
                + "'>"
                + tag_content
                + "</a>"
            )

    tag_index_re = r"--tagIndexInfoStart----tagIndexInfoEnd--"

    new_read_me = replaceTemplate(new_read_me, tag_index_re, tag_index_info)

    # 将生成的数据写入README.md
    with open(os.path.join(os.getcwd(), "README.md"), "w") as load_f:
        load_f.write(new_read_me)


main()
