# ali raee interview task

### how to use this code.

1. clone code from this repo
```
git clone https://github.com/aliraee/tps.git
```

2. build docker image
```
docker build -t tapsi-interview .
```

3. run django project
```
 docker run --rm -p 8000:8000 --name app tapsi-interview 
```

4. after run container you can open this url 
    [http://127.0.0.1:8000/ip/](http://127.0.0.1:8000/ip/)

5. you can enter your desiered IP in HTML Form tab and ping to entered IP.

6. for option you can run project test by this command after setting up a running container of this project
```
docker exec -it app python manage.py test
```



### Contact me: [aliraee1@yahoo.com](mailto:aliraee1@yahoo.com)
