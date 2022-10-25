# blog_nuxt


### изменить тип рендеринга
///nuxt.config.js
port default {
  ssr: false,
  ....
}
// или в скриптах package.json проставить флаг --spa

### Установка зависимостей из файла package.json
npm install или npm i

## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

### разница между generate & build
https://www.reddit.com/r/Nuxt/comments/f7rr4k/whats_the_difference_between_nuxt_build_spa_and/
https://nuxtjs.org/docs/get-started/commands/
https://stackoverflow.com/questions/46175023/nuxt-build-spa-vs-nuxt-generate

### диплой в докер
https://www.youtube.com/watch?v=WGUE2R9L_do

### не ставиться pillow
https://stackoverflow.com/questions/44043906/the-headers-or-library-files-could-not-be-found-for-jpeg-installing-pillow-on
  
# add that 

  FROM python:alpine
  RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
  RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
  RUN pip install Pillow
