---
title: Linux系统中的cgroups的了解与应用
icon: pen-to-square
date: 2024-09-12
category:
  - Linux
tag:
  - Linux
  - docker
  - cgroups
---
Linux 的 cgroup（控制组）特性是一种强大的工具，它允许你限制、记录和隔离进程组所使用的物理资源（包括 CPU、内存、磁盘 I/O 等）。如果你想限制一个进程或一组进程的最大内存使用量，你可以使用 cgroup 的内存限制功能。

以下是如何使用 cgroup 来限制最大内存使用的基本步骤：

1. **创建 cgroup**:
   使用 `cgcreate` 命令创建一个新的 cgroup。例如，创建一个名为 `mygroup` 的 cgroup，可以使用以下命令：

   ```bash
   sudo cgcreate -g memory:/mygroup
   ```

2. **设置内存限制**:
   使用 `cgset` 命令为 cgroup 设置内存限制。例如，将 `mygroup` 的内存限制设置为 200MB，可以使用以下命令：

   ```bash
   sudo cgset -r memory.limit_in_bytes=209715200 mygroup
   ```

3. **将进程添加到 cgroup**:
   使用 `cgclassify` 命令将进程添加到 cgroup。例如，将进程 ID 为 1234 的进程添加到 `mygroup`，可以使用以下命令：

   ```bash
   sudo cgclassify -g memory:mygroup 1234
   ```

这样，进程 ID 为 1234 的进程及其子进程将被限制在最多使用 200MB 的内存。

注意：这些命令可能需要 root 权限来执行。此外，确保你的系统安装了 cgroup 工具，这些工具可能在某些 Linux 发行版中不是默认安装的。

通过这些步骤，你可以有效地控制 Linux 系统上进程组的内存使用，有助于防止单个进程消耗过多的内存资源，从而影响系统的整体稳定性和性能。

要通过 Linux 的 cgroup 特性限制 Docker 所有容器的最大内存使用，你可以利用 Docker 自身的内存限制功能，这实际上是基于 cgroup 实现的。Docker 允许你在容器级别设置内存和 CPU 的限制。

以下是如何为 Docker 容器设置内存限制的基本步骤：

1. **创建或更新 Docker 容器时设置内存限制**：
   使用 `docker run` 命令创建容器时，可以使用 `--memory` 或 `-m` 选项来设置内存限制。例如，要创建一个内存限制为 500MB 的容器，可以运行：

   ```bash
   docker run -m 500m --name my_container my_image
   ```

   如果你想要更新一个已经存在的容器的内存限制，可以使用 `docker update` 命令：

   ```bash
   docker update --memory 500m --memory-swap -1 my_container
   ```

   这里 `--memory-swap` 设置为 `-1` 表示不限制 swap 空间的使用，如果你想要限制 swap 空间，可以将其设置为一个具体的值，比如 `--memory-swap 1g`。

2. **为 Docker 守护进程设置默认内存限制**：
   你也可以在 Docker 守护进程的配置文件 `/etc/docker/daemon.json` 中设置默认的内存和 swap 限制，这样所有新创建的容器都会继承这些限制，除非在创建时明确指定了其他值。例如：

   ```json
   {
     "default-ulimits": {
       "nofile": {
         "name": "nofile",
         "hard": 64000,
         "soft": 64000
       }
     },
     "default-memory-limit": "500m",
     "default-memory-swap": "-1"
   }
   ```

   修改配置文件后，需要重启 Docker 守护进程来使更改生效。

3. **验证内存限制**：
   你可以使用 `docker stats` 命令来查看容器的内存使用情况，以验证内存限制是否生效。

通过这些步骤，你可以有效地控制 Docker 容器在 Linux 系统上的内存使用，防止单个容器消耗过多的内存资源。