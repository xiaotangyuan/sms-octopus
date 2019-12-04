# sms-octopus
基于nameko的短信任务分发

## 如果没有rabbitmq服务器需要安装

### 启动rabbitmq
*  进入项目根目录 (sms-octopus)
*  cd rabbitmq
*  启动rabbitmq: docker-compose up -d
服务启动成功，此时可以通过端口5672访问rabbitmq
也可以使用 [http://localhost:15672](http://localhost:15672/) 访问管理后台


## 安装流程（docker）
*  cp docker-compose.yml.template docker-compose.yml
*  将docker-compose.yml文件中environment下的环境变量填上正确的值
*  docker-compose up -d
*  在安装有nameko的python环境下使用sms/sendsms.py的参考代码调用发送短信