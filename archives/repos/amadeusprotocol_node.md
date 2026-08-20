# node

### Tested Distro/Env
Linux Kernel 6.8  
Ubuntu 24.04  

### Building
Using podman or docker
```
podman build --tag erlang_builder -f build.Dockerfile
./build.sh
```

### Testnet
```
#run local testnet with RPC api

#point RPC endpoint to localhost
vim /etc/hosts
127.0.0.1 nodes.amadeus.bot

#run google chrome with cert verification disabled and CORS disabled
mkdir -p /tmp/chrome_debug
google-chrome  --user-data-dir="/tmp/chrome_debug" --no-first-run --no-default-browser-check \
--ignore-certificate-errors --disable-web-security --unsafely-treat-insecure-origin-as-secure=https://nodes.amadeus.bot

#allow listening on port 80 and 443
sudo sysctl -w net.ipv4.ip_unprivileged_port_start=80

#run the local testnet
TESTNET=true WORKFOLDER=/tmp/testnet HTTP_IPV4=127.0.0.1 HTTP_PORT=80  ./amadeusd

# inside REPL submit a transfer to self
pk = Application.fetch_env!(:ama, :trainer_pk)
sk = Application.fetch_env!(:ama, :trainer_sk)
Testnet.call(sk, "Coin", "transfer", [pk,"1","AMA"])

# Deploy contract (default account is :trainer_pk)

pk = Application.fetch_env!(:ama, :trainer_pk)
sk = Application.fetch_env!(:ama, :trainer_sk)
Testnet.deploy "/home/user/project/node/contract_samples/assemblyscript/counter.wasm"
Testnet.call sk, pk, "get", []
Testnet.call sk, pk, "increment", ["2"]
```

### AutoUpdates + Running as a systemd service

```
cat <<EOT > /etc/sysctl.conf
#buff up the UDP stack for 1gbps
net.core.wmem_max = 268435456
net.core.rmem_default = 212992
net.core.rmem_max = 268435456
net.core.netdev_max_backlog = 300000
net.core.optmem_max = 16777216
net.ipv4.udp_mem = 3060432 4080578 6120864

# for normal networks: block spoofed UDP packets
net.ipv4.conf.all.rp_filter=1
net.ipv4.conf.default.rp_filter=1
EOT
```

```
cat <<EOT > /etc/security/limits.conf
root hard nofile 1048576
root soft nofile 1048576
* hard nofile 1048576
* soft nofile 1048576
root hard nproc unlimited
root soft nproc unlimited
* hard nproc unlimited
* soft nproc unlimited
root hard memlock unl

... (truncated)