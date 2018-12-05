import get_html
import re

def parse_one_page(html,list_data):
    #解析后得到的是标签中的内容
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                         + '.*?data-src="(.*?)"'
                         + '.*?name"><a.*?>(.*?)</a>'
                         + '.*?star">(.*?)</p>'
                         + '.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>'
                         + '.*?fraction">(.*?)</i>'
                         + '.*?</dd>', re.S)
    items = pattern.findall(html)
    #items = re.findall(pattern, html)
    #print(items)
    #将结果放入到字典中
    '''
        for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
    '''

    for item in items:
        ranking = item[0]
        image = item[1]
        title = item[2]
        actor = item[3].strip()[3:]
        release_time = item[4].strip()[5:]
        score = item[5] + item[6]
        list_data.append([ranking, image, title, actor,release_time,score])
