# Library Manager Flask

基于Flask+MySQL+HTML的图书借阅管理系统，包含用户端和管理端功能。

## 功能特点

- 用户端：图书浏览、借阅、归还、个人借阅记录查询等
- 管理端：图书管理、用户管理、借阅记录管理等
- 响应式界面设计，操作简单直观

## 环境要求

- Python 3.7或Python 3.8
- MySQL 5.7/8.0
- 相关Python依赖包

## 安装步骤

### 1. 安装依赖包

```bash
pip install -r requirements.txt
```

### 2. 配置数据库

修改`config.py`文件中的数据库配置信息：

```python
# 根据你的MySQL配置修改以下信息
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/library?"
```

### 3. 导入数据库

在MySQL中执行以下命令导入数据库结构（建议使用Navicat）：

```bash
mysql -u root -p < library_manager.sql
```

### 4. 启动应用

```bash
python manage.py
```

### 5. 访问系统

启动成功后，在浏览器中打开控制台显示的链接（通常是 http://127.0.0.1:5000）即可访问系统。

## 系统账号

### 管理员账号
- 用户名：admin
- 密码：1

### 普通用户账号
- 用户名：1
- 密码：1

也可通过系统注册功能创建新的普通用户账号。

## 目录结构

```
library_manager_flask/
├── app.py              # 应用入口
├── config.py           # 配置文件
├── app/
│   ├── main/           # 主要功能模块
│   ├── reader/         # 用户/读者功能模块
│   ├── static/         # 静态资源
│   │   ├── bootstrap/  # Bootstrap框架
│   │   │   ├── css/
│   │   │   ├── fonts/
│   │   │   └── js/
│   │   ├── echart/     # 图表组件
│   │   ├── img/        # 图片资源
│   │   │   ├── avata/  # 用户头像
│   │   │   └── cover/  # 图书封面
│   │   ├── jquery/     # jQuery库
│   │   ├── layui/      # Layui框架
│   │   │   ├── css/
│   │   │   ├── font/
│   │   │   ├── images/
│   │   │   └── lay/
│   │   └── static/     # 其他静态资源
│   │       └── css/
│   └── templates/      # HTML模板
│       └── reader/     # 读者相关页面
├── library_manager.sql # 数据库文件
└── requirements.txt    # 依赖包列表
```


