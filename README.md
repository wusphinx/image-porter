# image-porter
镜像搬运工

由于`gcr.io`的镜像拉取不下来，有时候下载这些被 X 的镜像稍微有点费劲，不过可以借助github的action，将镜像拉下来
然后推送到[Dockerhub](https://hub.docker.com/)即可，由于Dockerhub对于免费用户目前只能开放三个Repo，
需要在项目中配置好`DOCKERHUB_USERNAME`和`DOCKERHUB_TOKEN`，嗯，就是酱紫。
