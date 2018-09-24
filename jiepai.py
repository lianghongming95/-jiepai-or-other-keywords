import  requests,json,os
from hashlib import md5
from urllib.parse import urlencode

for offset in range(0,101,20):

    print (offset)
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    response = requests.get('https://www.toutiao.com/search_content/?'+urlencode(params))


    def get_image(json):

        if json.get("data"):
            # print("6666666666")
            data = json.get('data')
            # print(data)
            # print("data1111111111111111")
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = str(item.get("title"))
            # print(title)
            #
            # print("title2222222222")
            images = item.get("image_list")
            # print(images)
            # print("image33333333333")
            for image in images:#生成器
                    yield {
                        'image': 'https:' + image.get('url'),#h获得图片链接
                        'title': title#获得图片标题
                    }

    get_image(response.json())
    r = get_image(response.json())
    # print(r)
    for i in r:

        title_path = "街拍20180919"+os.path.sep + i.get("title")
        if not os.path.exists(title_path):
            os.makedirs(title_path)



        image_response=requests.get(i.get("image"))
        file_image = title_path + os.path.sep+ '{file_name}.{file_suffix}'.format(file_name=md5(image_response.content).hexdigest(),
            file_suffix='jpg')
        with open(file_image,"wb") as f:
            f.write(image_response.content)

        print("111111111")
        print(md5(image_response.content).hexdigest())
        print("2222222")


