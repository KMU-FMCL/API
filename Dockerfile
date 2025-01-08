FROM taehun3446/systemd-cupy:v13.3.0-12.4.1-cudnn-devel-ubuntu22.04

RUN echo "fastapi\nuvicorn" > requirements.txt \
         && pip3 install --no-cache-dir -r \
                 requirements.txt

WORKDIR /app

COPY app/ /app/

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
