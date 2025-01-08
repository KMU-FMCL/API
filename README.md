## KMU-FMCL API 

### 1.

```bash
git clone -b v1 https://github.com/KMU-FMCL/API.git

cd API
```

<details>
<summary>Server</summary>

```bash
cd Server

sudo chmod +x ./build.sh # Docker Image Build

docker compose up -d # Server Start

docker attach KMU-FMCL_API # Log Check
```

</details>

<details>
<summary>Client</summary>

```bash
cd Cliet

python3 -m venv $HOME/.env/client # Recommend : Python Virtual Envrionment

source $HOME/.env/client/bin/activate # Virtual Envrionment Activate

pip3 install -r requirements.txt # Requirement

python3 client.py # Request
```

</details>
