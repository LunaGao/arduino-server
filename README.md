# arduino-server

## 激活虚拟环境
开发和运行时需要使用虚拟环境
`. venv/bin/activate`

## 运行
复制`application.config.json.EXAMPLE`文件为`application.config.json`，修改其中内容。

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```