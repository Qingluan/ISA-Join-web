#ISC  Document

>git 使用说明

###提交
>git add -A  #添加所有内容
>git commit -m "xxx" #提交所有内容
>git push origin master

###从远端dump 到本地 
>git pull origin master

>Include Part
 - one 
 
## Introduction 
## Install 
## Useage 
## arguments

 - client to server
```
{
	'JSON_REGISTER':{
		'email':str,
		'ID':str,
		'nick':str,
		'passwd':str(hash),
		'introduction':str,
	}
}
```

 - server to client

```
{
	'result':'ok'/'no'
	'error':str # if result is 'ok' this item is not appearence
}

```

```
{
	'JSON_LOGIN':{
		'ID':int,
		'passwd':str,
	}
}
```
