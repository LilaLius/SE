---
tags:
  - github
link:
---
  > GitHub Guides

[[se00.实践作业说明.pdf#page=22&selection=6,0,6,13|se00.实践作业说明, 页面 22]]

先看[视频](https://www.bilibili.com/video/BV1i44y1e7hv/?spm_id_from=333.337.search-card.all.click&vd_source=f3868917b3f419d2bdace3cc40935b45)，可以结合[文档](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git)看
# 创建repository
略
## 使用git clone+git仓库地址将某个仓库下载到本地

![[Pasted image 20250522012259.png]]
![[Pasted image 20250522012438.png]]
![[Pasted image 20250522012441.png]]
![[Pasted image 20250522012556.png]]



# 将更改 commit到本地git
- 初始git
![[Pasted image 20250522014944.png]]

## git查看修改状态
```
git status
```
![[Pasted image 20250522015014.png]]
## 新建文件

![[Pasted image 20250522015240.png]]

## git查看修改的状态

![[Pasted image 20250522015335.png]]

## git指定本次commit包含的文件

```cmd
git add
```

```
git add .
```
![[Pasted image 20250522015627.png|362]]

## git完成一次到本地git的commit

```
git commit -a -m ""
```

![[Pasted image 20250522020834.png]]

![[Pasted image 20250522021131.png]]

![[Pasted image 20250522021323.png]]
![[Pasted image 20250522021347.png]]
## git加所有未保存的文件

```
git add .
```

![[Pasted image 20250522021540.png]]

![[Pasted image 20250522021710.png]]

> 只要有更改就会检测到

![[Pasted image 20250522021905.png]]

![[Pasted image 20250522022252.png]]

# 恢复到某个commit

## git看一下之前的commit

```
git log
```

![[Pasted image 20250522022640.png]]

## git恢复到某个commit

```
git reset --hard commit_id
```

![[Pasted image 20250522023636.png]] 

![[Pasted image 20250522023606.png]]
![[Pasted image 20250522023711.png]]

# push和pull操作

## 将本地内容同步到云端

![[Pasted image 20250522030315.png]]

同
![[Pasted image 20250522030342.png]]

![[Pasted image 20250522030456.png]]

刷新

![[Pasted image 20250522030533.png]]

## 从云端拉取内容

```
git pull
```

#？？？  

![[Pasted image 20250522031803.png]]

```
J:\documents\Github\SE>git pull
error: RPC failed; curl 56 Recv failure: Connection was reset
fatal: expected flush after ref listing
```

```
J:\documents\Github\SE>git pull
fatal: unable to access 'https://github.com/LilaLius/SE.git/': Failed to connect to github.com port 443 after 21127 ms: Couldn't connect to server
```

关闭VPN

![[Pasted image 20250522032256.png]]

```
J:\documents\Github\SE>git pull
fatal: unable to access 'https://github.com/LilaLius/SE.git/': Recv failure: Connection was reset
```

![[Pasted image 20250522032321.png]]

# 使用分支

## 创建新branch

```
git branch 新branch名称
```
![[Pasted image 20250522032940.png]]
要push一下
## 切换branch

```
git checkout 
```

![[Pasted image 20250522033046.png]]

![[Pasted image 20250522033125.png]]

![[Pasted image 20250522033259.png]]

![[Pasted image 20250522033520.png]]
push



## 合并branch

回到主分支
![[Pasted image 20250522034614.png]]

![[Pasted image 20250522034637.png]]
```
git merge
```


![[Pasted image 20250522035211.png]]![[Pasted image 20250522035235.png]]
![[Pasted image 20250522035522.png]]
push
## 删除branch

```
git branch -D branch名称
```

![[Pasted image 20250522035436.png]]
同步到云端
![[Pasted image 20250522035622.png]]

![[Pasted image 20250522035801.png]]
# [[在Git repository中创建一个 e1 目录]]
