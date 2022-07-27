import configparser
from time import strftime


def config_generator():
    # 설정파일 만들기
    config = configparser.ConfigParser()

    # # 캡쳐 상태, 주기
    # global capStat
    # capStat = 1 , 0.5
    # # 핸들값
    # global hwnd
    # hwnd = 0
    # # 핸들 상태 , 주기
    # global handleStat
    # handleStat = 1 , 2
    # # 위치 상태 , 주기
    # global locationStat
    # locationStat = 1 , 2
    # # 룬 상태 , 주기
    # global runeStat
    # runeStat = 1 , 2

    # 설정파일 오브젝트 만들기
    config['system'] = {}
    config['system']['title'] = 'pickit'
    config['system']['version'] = '1.2.42'
    config['system']['update'] = strftime('%Y-%m-%d %H:%M:%S')
    config['system']['language'] = 'ko'
    config['system']['캡쳐 상태'] = 'True'
    config['system']['캡쳐 주기'] = '0.05'
    config['system']['핸들 서치 상태'] = 'True'
    config['system']['핸들 서치 주기'] = '2'
    config['system']['위치 서치 상태'] = 'True'
    config['system']['위치 주기'] = '2'
    config['system']['룬 서치 상태'] = 'True'
    config['system']['룬 주기'] = '2'
    config['system']['미니맵서치X'] = '0'
    config['system']['미니맵서치Y'] = '0'
    config['system']['미니맵서치W'] = '320'
    config['system']['미니맵서치H'] = '200'
    

    config['video'] = {}
    config['video']['width'] = '1366'
    config['video']['height'] = '768'
    config['video']['type'] = 'mp4'


    # 설정파일 저장
    with open('src/config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


def config_read():
    
    # 설정파일 읽기
    config = configparser.ConfigParser()    
    config.read('src/config.ini', encoding='utf-8') 

    # 설정파일의 색션 확인
    # config.sections())
    result = version_read(config)
    return result

def version_read(config):
    ver = config['system']['version']
    title = config['system']['title']
    update = config['system']['update']
    language = config['system']['language']
    capStat = config['system']['캡쳐 상태']
    capTime = config['system']['캡쳐 주기']
    handleStat = config['system']['핸들 서치 상태']
    handleTime = config['system']['핸들 서치 주기']
    locationStat = config['system']['위치 서치 상태']
    locationTime = config['system']['위치 주기']
    runeStat = config['system']['룬 서치 상태']
    runeTime = config['system']['룬 주기']
    miniMapX = config['system']['미니맵서치X']
    miniMapY = config['system']['미니맵서치Y']
    miniMapW = config['system']['미니맵서치W']
    miniMapH = config['system']['미니맵서치H']
    result = [ver, title, update, language, capStat, capTime, handleStat, handleTime, locationStat, locationTime, runeStat, runeTime , miniMapX, miniMapY, miniMapW, miniMapH]
    # print(result)
    return result

# config_generator()
# config_read()