chalice-serverless-alerts
---------------------

Requirements
------------
* Docker
* Cmake

Help
----
* make
* make help

Commands
--------
```console
Target           Help                                                        Usage
------           ----                                                        -----
build.image       Build image for development                                make build.image
delete            Eliminating project deployment                             make delete
deploy            Deploying project                                          make deploy
run.local         Locally executing the project                              make run.local
ssh               Connect to the container by ssh                            make ssh
```

How to use
----------
```console
Endpoint: /
Method: GET
Output:
        {
        "Status": "Ok",
        "RMTAVG": 0.4588,
        "Total Notifications Analized": 8,
        "Rate minute schedule": "5",
        "Degradation threshold": 0.1
        }
```