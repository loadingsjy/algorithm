#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os

def vaild():
    picture_str = "1.jpg 2.jpeg 3.GIFsddfghgjk"
    pattern_pic = r'\S*?jpg|\S*?JPG|\S*?jpeg|\S*?JPEG|\S*?gif|\S*?GIF|\S*?bmp|\S*?BMP'
    searchObj_ = re.findall(pattern_pic, picture_str)
    if searchObj_:
        print("searchObj.group() : ", searchObj_)


    date_str = '2/31/2006444sdfghjh'
    pattern_date = r'\d\/\d\/\d{4}'
    searchObj_1 = re.search(pattern_date, date_str)
    if searchObj_1:
        print("searchObj.group() : ", searchObj_1.group())


    tel_str = '(0512)68078800-6852678fghjjkkjk'
    pattern_tel = r'(0\d{3})\d{8}[-]\d{4}'
    searchObj_2 = re.search(pattern_tel, tel_str)
    if searchObj_2:
        print("searchObj.group() : ", searchObj_2.group())

def Get_Html(filename):
    filename = r"data/" + filename
    filename = os.path.join(os.path.dirname(__file__), filename)

    # set variable
    http_result = []

    # set rule
    p = re.compile(r'href="(https:.+?)"|href="(http:.+?)"')

    # read html file
    html_content = open(filename, 'rb').read()
    # print html_content

    # regex match
    matches = p.findall(html_content)
    # print len(matches)

    for m in matches:
        if m[0] != '':
            http_result.append(m[0])
        if m[1] != '':
            http_result.append(m[1])

    return http_result, len(http_result)


def main():
    vaild()
    
    http_result, http_result_size = Get_Html(r'list.html')
    print("提取的超链接个数为：%d" % http_result_size)
    print("提取的超链接的集合为：")
    print(http_result)


    # content_list, content_size, title_list, title_size = Get_Content(r'content.html')
    #
    # print "提取的标题个数为：%d" % title_size
    # print "提取的标题为："
    # for i in title_list:
    #     print i.decode('utf-8')

    # print "提取的内容个数为：%d" % content_size
    # print "提取的内容为："
    # for i in content_list:
    #    print i.decode('utf-8')
    pass

if __name__ == "__main__":
    main()
    pass
