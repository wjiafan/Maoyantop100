import get_html
import parse_html
import write_file
import time
from multiprocessing import Pool
import Data_DB


def main():

    start_url = 'http://maoyan.com/board/4'

    # def main(offset):
    # url = 'http://maoyan.com/board/4?offset='+ str(offset)
    # print(url)
    length = 10

    #模拟浏览器的行为
    header ={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep - alive",
        "Host": "maoyan.com",
        "Referer": "http://maoyan.com/board",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }


    for i in range(length):

        url = start_url + '?offset=' + str(10 * i)
        html = get_html.get_html(url,header)
        '''
            for item in parse_html.parse_one_page(html):
            write_file.write_to_file(item)
        '''
        list_data = []
        parse_html.parse_one_page(html,list_data)
        write_file.write_to_file(list_data)
        Data_DB.write_to_sql(list_data)


if __name__ == '__main__':

    main()

    #for i in range(10):
         #main(offset=i * 10)
         #time.sleep(1)

    #进程池的抓取效率--多进程的用法
    #pool = Pool()
    #pool.map(main,[i*10 for i in range(10)])