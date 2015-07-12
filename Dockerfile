FROM python:2-onbuild
MAINTAINER Zoran Olujić <olujicz@gmail.com>

RUN "/bin/echo -e '#!/bin/sh\n/usr/local/bin/celery -A manage.celery worker --workdir=/usr/src/app &\nexit 0' >/etc/rc.local"
CMD ["uwsgi", "-s", "0.0.0.0:9000", "-w", "manage:app"]
EXPOSE 5000 9000
