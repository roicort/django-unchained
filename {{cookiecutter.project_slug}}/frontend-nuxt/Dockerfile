FROM node:21

ENV NEXT_TELEMETRY_DISABLED 1

WORKDIR /app

RUN npm install -g pnpm

COPY . .

RUN pnpm install