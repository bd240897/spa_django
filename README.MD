// SPA сайт на Django Rest Framework и NuxtJS

https://stepik.org/course/82067/syllabus
https://github.com/bd240897/spa_django

### 1 
// вертка сатй на bootstrap
blog_bootstrap


### 2
// блог чисто на django
blog/myblog
// точка входа
http://127.0.0.1:8000/myblog

// мой старый сайт вставленный сюда
blog/mistite
// точка входа
http://127.0.0.1:8000/mysite/home

### 3
// блог чисто drf
api
// точка входа
http://127.0.0.1:8000/api

# nuxt

## Установка

// поставить глобально
npm install -g create-nuxt-app
// куда c:\Users\<user>\AppData\Roaming\npm\node_modules\
// старт проекта
npm init nuxt-app <project-name>

// проблемы - оч долго ставиться
https://stackoverflow.com/questions/66893199/hanging-stuck-reifyprettier-timing-reifynodenode-modules-nrwl-workspace-comp

    node --version
    npm --version
    npm install -g npm@6


####
// nuxt-doc
https://nuxtjs.org/docs/get-started/installation/
//

// nuxt bould to vps
https://www.youtube.com/watch?v=QOgaifhmhHI
https://habr.com/ru/post/558178/
https://ru.stackoverflow.com/questions/877263/Загрузка-nuxt-js-на-vps

// + docker
https://habr.com/ru/post/438862/
https://jonathanmh.com/deploying-a-nuxt-js-app-with-docker/
https://stackoverflow.com/questions/61295997/how-to-setup-nuxt-js-as-a-spa-with-net-core-web-api-in-a-single-docker-containe
https://linuxtut.com/en/6166f8118370c774adea/

// create site in github
https://www.youtube.com/watch?v=lG9y6WKcyeE

// nuxt auth
https://auth.nuxtjs.org/api/auth/

// vue auth
https://pavelgonzales.medium.com/best-practices-авторизации-для-vue-8b769589001a
https://emackovenko.ru/vue-js-vuex-jwt-autentifikaciya-instrukciya-prime/
https://www.internet-technologies.ru/articles/obrabotka-autentifikacii-v-vue-s-vuex.html#header-45996-8

# запросы curl
    sudo apt install curl
    curl -L yandex.ru

# как у меня заработало
    blog_nuxt_v1/nuxt.config.js
        заменить baseURL: 'http://178.154.241.157:8000',
    blog_nuxt_v1/store/index.js
          заменить
        axios: {
            baseURL: 'http://178.154.241.157:8000',
            browserBaseURL: 'http://178.154.241.157:8000', 
        },

# Мусор
npm install -g create-nuxt-app
npm install -g npm@6
c:\Users\Дмитрий\AppData\Roaming\npm\node_modules\
https://stackoverflow.com/questions/66893199/hanging-stuck-reifyprettier-timing-reifynodenode-modules-nrwl-workspace-comp
% node --version 
# 16.5
% npm --version 
# 7.19.1

<!--  название страницы и есть имя прокидываемого параметра на нее -->

# ДРУГИЕ ЗАМЕТКИ
1. [readme api](./api/README.md)
2. [readme nuxt](./blog_nuxt/README.md)


