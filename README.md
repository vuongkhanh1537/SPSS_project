# SPSS_project

*/backend - Backend development workflow
```sh
cd backend
```
```sh
pipenv lock --pre
```
```sh
pipenv run pip install -r requirements.txt
```
Test server:
```sh
python manage.py runserver
```

*/frontend - Frontend development workflow

run if strike this error npm ERR! network read ECONNRESET

    npm config set registry http://registry.npmjs.org/ 

then

    npm config set fetch-retry-mintimeout 20000

    npm config set fetch-retry-maxtimeout 120000

    npm install -g @angular/cli

npm i

npm start


For deploying
npm run build

