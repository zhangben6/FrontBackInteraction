import requests
import re

def song_processing(name):
    # 第一步: 获取歌曲的ids
    search_api = 'http://music.taihe.com/search'
    #搜索的关键字,传递参数,通过字典构造
    keyword={'key':'%s'%name} 
    #以get的方式发送请求
    response = requests.get(search_api,params=keyword)
    #取出html的源码  params是传递的get参数
    response.encoding = 'utf-8'
    html = response.text   
    # 通过正则表达式获取id
    ids = re.findall(r'&quot;id&quot;:&quot;(\d+)&quot;',html)
    # print(ids)

    #第二部:获取歌曲的信息
    mp3_info_api = 'http://play.taihe.com/data/music/songlink'
    data = {
        'songIds':','.join(ids),
        'hq': 0 ,
        'type': 'm4a,mp3',
        'rate': '' ,
        'pt': 0 ,
        'flag': -1 ,
        's2p': -1 ,
        'prerate': -1 ,
        'bwt': -1 ,
        'dur': -1 ,
        'bat': -1 ,
        'bp': -1 ,
        'pos': -1 ,
        'auto': -1 
    }

    #发送requests请求
    #data就是post的参数
    res = requests.post(mp3_info_api,data=data)
    #因为返回的数据json格式  直接调用json方法,转成字段
    info = res.json()
    # print(info)
    #下载歌曲
    #根据数据的结构,获取歌曲的信息
    song_info = info['data']['songList']
    song_combine_list = []
    song_link_sum = []
    song_name_sum = []
    #循环接收每个歌曲的信息
    for song in song_info:
        # print(song)
        #根据数据结构获取信息
        song_name = song['songName']
        if song_name == None:
            break
        song_name_sum.append(song_name)
        song_author = song['artistName']
        song_combine = 'Music:%s--author:%s' % (song_name,song_author)
        song_combine_list.append(song_combine)

        #接着获取歌曲的mp3下载地址
        song_link = song['songLink']
        song_link_sum.append(song_link)
        #获取歌名的后缀格式fomat 
        for_mat = song['format']

        #歌词的下载地址
        lrc_link = song['lrcLink']
    # print(song_combine_list)
    print('以下是您搜索的结果:')
    #根据此列表下载对应的歌曲
    for k,v in enumerate(song_combine_list):
        print(k,v)
    # print(song_link_sum)
    download_music(song_name_sum,song_link_sum,for_mat)

    
def download_music(song_name_sum,song_link_sum,for_mat):
    num = int(input("please enter singName："))
    song_name = song_name_sum[num]
    download_music_link = song_link_sum[num]         
    #下载mp3
    if download_music_link: #有可能没有地址
        song_res = requests.get(download_music_link)
        with open('%s.%s'%(song_name,for_mat),'wb') as f:
            f.write(song_res.content)
            print("恭喜您下载成功")
    # if lrc_link:
    #     lrc_response = requests.get(lrc_link)
    #     with open('%s.lrc' % song_name,'w',encoding='gbk') as f:
    #         f.write(lrc_response.text)
    #         f.close()

def main():
    name = input('please enter name or singName:')
    song_processing(name)
    
if __name__ == "__main__":
    main()