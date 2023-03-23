FROM node:8-alpine as node
ENV DockerHOME=/home/app/frontend 
RUN mkdir -p $DockerHOME
##RUN npm install -g http-server
WORKDIR $DockerHOME

COPY package.json package-lock.json ./
RUN npm install
RUN npm install @vue/cli@4.5.0 -g
COPY . ./
#RUN npm run serve
CMD ["npm", "run", "build"]

# expose the port
#EXPOSE 8080

 FROM nginx:alpine

COPY --from=node /home/app/frontend/dist /usr/share/nginx/html
EXPOSE 80 443
CMD [ "nginx", "-g", "daemon off;" ]