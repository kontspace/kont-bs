Kont BS 代码托管于 GitHub 平台中，你可以使用以下方式获得源码并且启动。

# 从 GitHub 获取代码

在快速开始之前，需要在先在电脑中安装 Python2.7 和 virtualenv 或及其类似工具（推荐）,
假如你没有在 GitHub 中添加过 SSH Key，把 clone 地址换成 `https://github.com/kontspace/kont_bs.git`。

```shell
git clone git@github.com:kontspace/kont_bs.git
```

# 使用 Django 内置开发服务器

```
cd kont_bs

# 创建虚拟环境，如果不使用和可以跳过此步骤
virtualenv venv
source ./venv/bin/activate

pip install -r requirments.txt

./manage.py migrate
```        

添加超级管理员，根据提示一步一步完成即可

```
./manage.py createsuper
```

启动 Kont BS

```
./manager.py runserver
```

Kont BS 会启动在你的本地的 8000 端口，使用浏览器访问 `http://localhost:8000`。

# Docker

需要先构建镜像（最后替换成国内的 Docker Register Mirrors，否则可能基础镜像 pull 不下来），
容器内部的包管理工具，已经替换成阿里源。

```shell
cd kont_bs
docker build -t kont-bs:0.1
```

启动容器

```
docker run -d \
    --name kont-bs \
    -p 8000:8000 \
    kont-bs:0.1
``` 

Kont BS 会启动在你的本地的 8000 端口，使用浏览器访问 `http://localhost:8000`，默认后台账号和密码都是 `admin`。

