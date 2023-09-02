FROM python:3.11 AS builder

COPY requirements.txt .

# install dependencies
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /usr/project

# copy install package from builder to local
COPY --from=builder /root/.local /root/.local
COPY . .