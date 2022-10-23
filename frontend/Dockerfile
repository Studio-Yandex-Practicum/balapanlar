FROM node:16-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install && npm run prepare
COPY . ./
RUN npm run build
CMD cp -r dist result_build