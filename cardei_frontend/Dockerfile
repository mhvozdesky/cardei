#FROM node:16

#WORKDIR /app

#COPY package*.json ./

#RUN npm install

#RUN npm install axios

#COPY . .

#CMD npm run serve


FROM node:16

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json ./

RUN npm install && \
	npm install axios && \
	npm install vuex-persistedstate

COPY . .

CMD npm run serve
# CMD npm run build
# CMD sleep 10000