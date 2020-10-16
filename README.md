# arduino-server

## 激活虚拟环境
* `pip3 install Flask`
* `pip3 install Flask-PyMongo`
* `pip3 install dnspython` 如果mongodb使用了`mongodb+srv://`，则需要安装此插件

## 开发时可以使用虚拟环境
* 创建虚拟环境 `python3 -m venv venv`
* 使用虚拟环境 `. venv/bin/activate`


## 运行
复制`application.config.json.EXAMPLE`文件为`application.config.json`，修改其中内容。

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

## 部署
这里使用Gunicorn
### Gunicorn
* `pip3 install gunicorn` 安装
* `gunicorn "flaskr:create_app()" -b 127.0.0.1:5000 -D` （`-D`, 后台运行)

## 访问地址
http://localhost:5000/hello    测试页
http://localhost:5000/list   列表页
http://localhost:5000/xiaomi    增加数据页
