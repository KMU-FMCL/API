FROM taehun3446/systemd-cupy:v13.3.0-12.4.1-cudnn-devel-ubuntu22.04

RUN echo "fastapi\nuvicorn" > requirements.txt \
         && pip3 install --no-cache-dir -r \
                 requirements.txt

WORKDIR /app

COPY src/main.py src/gpu_module.py src/

EXPOSE 8080

CMD [ "python3", "src/main.py" ]
