项目配置有 **配置文件** 和 **环境变量** 两种模式。

环境变量中有部分是和配置文件中的配置重复，
这时候环境变量的优先级高于配置文件，
这主要是考虑的在使用 Docker 时候环境变量的灵活性要远远大于配置文件。

默认配置下，项目是处于 DEBUG 模式，可以正常启动。
如果你是在直接使用，请使用下一章节的部署方法，把 DEBUG 使用在正式环境是不合理，不安全的。


## 配置选项

在 Kont BS 中目前有以下配置选择可以配置：

| 配置项 | 功能 | 默认值 | 说明 |
| ------------ | ------------- | ------------ | ------------ |
| SUPER_USER | 默认管理员账号  | admin | 只适用于 Docker 部署方式 |
| SUPER_PASSPORT | 默认管理员密码  | admin | 只适用于 Docker 部署方式 |
| MYSQL_HOST | MySQL 地址 | localhost | 只适用于正式环境 |
| MYSQL_PORT | MySQL 端口 | 3306 | 只适用于正式环境 |
| MYSQL_USER | MySQL 用户 | root | 只适用于正式环境 |
| MYSQL_PASSWORD | MySQL 密码 | mysql | 只适用于正式环境 |
| GITHUB | GitHub 主页地址 | `https://github.com/zhengxiaowai`| 马上迁移到数据库中|
| LINKED | Linked 主页地址 | `https://cn.linkedin.com/in/seanho116` | 马上迁移到数据库中 |
| EMAIL | 邮件| `h1x2y3awalm@gmail.com` | 马上迁移到数据库中 |
| COPYRIGHT | 版权信息 | `Copyright SeanHo 2016` | 马上迁移到数据库中 |
| SITE_NAME | 主页 title| `Aathena` | 马上迁移到数据库中 |