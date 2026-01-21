# 校园吐槽墙 (Say Something)

这是一个基于 Django 的匿名吐槽墙系统。

## 功能
- 匿名发布吐槽
- 匿名评论
- 管理员后台删除评论

## 部署说明 (Deployment)

本项目设计为一键启动，符合 [部署教程](https://static.yunguhs.com/tutorials/deploy/) 的要求。

### 启动命令
在项目根目录下运行：

```bash
sh run.sh
```

该脚本会自动：
1. 安装依赖 (`pip install -r requirements.txt`)
2. 初始化数据库 (`migrate`)
3. 创建默认管理员账户 (如果不存在)
4. 启动服务器 (端口 8000)

## 管理员后台 (Admin)

- 访问地址: `/admin/` (例如: `http://localhost:8000/admin/`)
- 默认账号: `admin`
- 默认密码: `admin123`

请在部署后及时修改密码。
