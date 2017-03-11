# 部署静态文件

当 Django 使用在正式环境的时候，静态文件需要被托管于 Web 服务器。

在 Kont BS 中使用 Makefile 可以快速导出静态文件到项目目录下的 staticfiles 的文件夹中
```shell
make collection
``` 
# 环境变量

在 [项目配置](configuration.md) 中的配置选都设置在启动之前，
推荐的做法的创建一个 `env.sh` 文件，填入你需要配置，使用 `source` 命令生效，当然你也可以在命令行中一个一个的 `export`。

```bash
# env.sh
export DEBUG=False
export MYSQL_PASSWORD=*****
```

```shell
source env.sh
```


# uWsgi 部署

Django 默认支持 uwsgi 可以方便的启动，在 Makefile 添加一些能增强性能的配置，使用 Makefile 也可以迅速启动项目。

```shell
make start-uwsgi
```

如果想停止可以使用：

```shell
make stop-uwsgi
```

如果想重启 uwsgi 可以使用：

```shell
make reload-uwsgi
```

# gunicorn 部署

暂无

# Docker 部署

暂无