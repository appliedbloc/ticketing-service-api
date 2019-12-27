pidfile = 'app.pid'
worker_tmp_dir = '/tmp'
worker_class = 'gthread'
workers = 2
worker_connections = 1000
timeout = 30
keepalive = 2
threads = 4
proc_name = 'app'
bind = '0.0.0.0:8888'
backlog = 2048
accesslog = '-'
errorlog = '-'
user = 'root'
group = 'root'