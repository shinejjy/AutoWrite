import json


def rewrite_json():
    dct = '''{
    "main": {
        "write_speed": 1,
        "by_word": {
            "is": true,
            "long": 1
        },
        "by_line": {
            "is": false,
            "long": 1
        },
        "by_whole_text": {
            "is": false
        }
    },
    "#":
    {
        "说明": "这一板块是注释",
        "write_speed": "表示每次复制粘贴操作所间隔时间，单位是ms",
        "by_word": "其中的is若为true则使用以字复制方式，long表示每次复制的长度",
        "by_line": "其中的is若为true则使用以行复制方式，long表示每次复制的长度",
        "by_whole_text": "其中的is若为true则使用整篇文章复制方式",
        "ps1": "by_word,by_line,by_whole_text中的is只能存在一个true，否则重置",
        "ps2": "若更改数据导致无法恢复，不必担心，重新启动程序即可重置"
    }
}'''
    with open('main/config.json', 'w+') as f:
        f.write(dct)


def load_json():
    try:
        with open('main/config.json', 'r') as f:
            cfg = json.load(f)['main']
    except:
        rewrite_json()
        with open('main/config.json', 'r') as f:
            cfg = json.load(f)['main']
    return cfg


def process_json():
    cfg = load_json()
    write_speed = max(1, cfg['write_speed']) / 1000
    if cfg['by_word']['is'] and not cfg['by_line']['is'] and not cfg['by_whole_text']['is']:
        by = 0
        long = cfg['by_word']['long']
    elif not cfg['by_word']['is'] and cfg['by_line']['is'] and not cfg['by_whole_text']['is']:
        by = 1
        long = cfg['by_line']['long']
    elif not cfg['by_word']['is'] and not cfg['by_line']['is'] and cfg['by_whole_text']['is']:
        by = 2
        long = 1
    else:
        rewrite_json()
        by = 1
        long = 1
    return [write_speed, by, long]

