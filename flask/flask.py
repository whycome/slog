# coding:utf-8

flask 使用session之前，必须设置秘钥
生成秘钥：
>>> import os
>>> os.urandom(24)
b'....\xb6F\xad\x91\x00\xdf'

# manage.py
# 设置秘钥
app.secret_key = "....\xb6F\xad\x91\x00\xdf"


flask_upload:

# IMAGES: 定义图片类型
# 创建一个set, 通过实例化uploadSet()类实现, 
photos = UploadSet("photos", IMAGES)
# configure_uploads: 注册并完成相应的配置
configure_uploads(app, photos)
# 传入应用实例和大小
patch_request_class(app, 32 * 1024 * 1024)

filename = photos.save(request.files['file'])
rec = photos.url(filename)
# url: 获取文件url
# save: 保存文件， 返回处理后的文件名
# path: 获取文件绝对路径


jinja2: 
	自定义过滤器： 
	def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
		return value[:2]
	app.add_template_filter(datetimeformat, 'dtf')
	# 函数的第一个参数是过滤器函数，第二个参数是过滤器名称