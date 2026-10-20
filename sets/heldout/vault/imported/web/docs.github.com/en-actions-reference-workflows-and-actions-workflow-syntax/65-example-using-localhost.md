---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#65-example-using-localhost.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-65-example-using-localhost
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.services` › Example: Using localhost'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#65-example-using-localhost
source_hash: 5fe449814b0708caf7b69a8d14c945293013fd62a9d2102ea91f9ebad7e9bfd8
---
This example creates two services: nginx and redis. When you specify the container port but not the host port, the container port is randomly assigned to a free port on the host. GitHub sets the assigned host port in the `${{job.services.<service_name>.ports}}` context. In this example, you can access the service host ports using the `${{ job.services.nginx.ports['80'] }}` and `${{ job.services.redis.ports['6379'] }}` contexts.

```
services:
  nginx:
    image: nginx
    # Map port 8080 on the Docker host to port 80 on the nginx container
    ports:
      - 8080:80
  redis:
    image: redis
    # Map random free TCP port on Docker host to port 6379 on redis container
    ports:
      - 6379/tcp
steps:
  - run: |
      echo "Redis available on 127.0.0.1:${{ job.services.redis.ports['6379'] }}"
      echo "Nginx available on 127.0.0.1:${{ job.services.nginx.ports['80'] }}"
```

## `jobs.<job_id>.services.<service_id>.image`

The Docker image to use as the service container to run the action. The value can be the Docker Hub image name or a registry name.

If `jobs.<job_id>.services.<service_id>.image` is assigned an empty string, the service will not start. You can use this to set up conditional services, similar to the following example.

```
services:
  nginx:
    image: ${{ options.nginx == true && 'nginx' || '' }}
```

## `jobs.<job_id>.services.<service_id>.credentials`

If the image's container registry requires authentication to pull the image, you can use `jobs.<job_id>.container.credentials` to set a `map` of the `username` and `password`. The credentials are the same values that you would provide to the [`docker login`](https://docs.docker.com/engine/reference/commandline/login/) command.

### Example of `jobs.<job_id>.services.<service_id>.credentials`

```
services:
  myservice1:
    image: ghcr.io/owner/myservice1
    credentials:
      username: ${{ github.actor }}
      password: ${{ secrets.github_token }}
  myservice2:
    image: dockerhub_org/myservice2
    credentials:
      username: ${{ secrets.DOCKER_USER }}
      password: ${{ secrets.DOCKER_PASSWORD }}
```

## `jobs.<job_id>.services.<service_id>.env`

Sets a `map` of environment variables in the service container.

## `jobs.<job_id>.services.<service_id>.ports`

Sets an `array` of ports to expose on the service container.

## `jobs.<job_id>.services.<service_id>.volumes`

Sets an `array` of volumes for the service container to use. You can use volumes to share data between services or other steps in a job. You can specify named Docker volumes, anonymous Docker volumes, or bind mounts on the host.

To specify a volume, you specify the source and destination path:

`<source>:<destinationPath>`.

The `<source>` is a volume name or an absolute path on the host machine, and `<destinationPath>` is an absolute path in the container.

### Example of `jobs.<job_id>.services.<service_id>.volumes`

```
volumes:
  - my_docker_volume:/volume_mount
  - /data/my_data
  - /source/directory:/destination/directory
```

## `jobs.<job_id>.services.<service_id>.options`

Additional Docker container resource options. For a list of options, see [`docker create` options](https://docs.docker.com/engine/reference/commandline/create/#options).

Warning

The `--network` option is not supported.

## `jobs.<job_id>.services.<service_id>.command`

Overrides the Docker image's default command (`CMD`). The value is passed as arguments after the image name in the `docker create` command. If you also specify `entrypoint`, `command` provides the arguments to that entrypoint.

### Example of `jobs.<job_id>.services.<service_id>.command`

```
services:
  mysql:
    image: mysql:8
    command: --sql_mode=STRICT_TRANS_TABLES --max_allowed_packet=512M
    env:
      MYSQL_ROOT_PASSWORD: test
    ports:
      - 3306:3306
```

## `jobs.<job_id>.services.<service_id>.entrypoint`

Overrides the Docker image's default `ENTRYPOINT`. The value is a single string defining the executable to run. Use this when you need to replace the image's entrypoint entirely. You can combine `entrypoint` with `command` to pass arguments to the custom entrypoint.

### Example of `jobs.<job_id>.services.<service_id>.entrypoint`

```
services:
  etcd:
    image: quay.io/coreos/etcd:v3.5.17
    entrypoint: etcd
    command: >-
      --listen-client-urls http://0.0.0.0:2379
      --advertise-client-urls http://0.0.0.0:2379
    ports:
      - 2379:2379
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
