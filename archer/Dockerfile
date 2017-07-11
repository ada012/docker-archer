FROM centos:latest
MAINTAINER caihanyong@foxmail.com
ENV PATH=/apps/srv/python3/bin:$PATH
WORKDIR /apps/srv/archer
COPY ./apps /apps
EXPOSE 80/tcp
CMD ["/apps/srv/run.sh"]