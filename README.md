# moscow-time

This is a `Django/uwsgi` application that uses nginx as its reverse proxy.
Replication is provided by uwsgi running the server in two processes under its own manager, see `uwsgi.ini`

```
curl -L int1.tst.iroha.tech/moscow/time/
```

```json
{
  "utc_datetime": "2020-12-05T11:45:04.257630+00:00"
}
```

[playbook link](https://github.com/fenchelfen/moscow-time-ansible)