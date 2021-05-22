## ToDo

Setup a K8s cluster, you are free to choose any installation tool you want. - OK

Install any application you want on this cluster make sure it uses Nginx as its frontend. - OK

Implement scale up to Nginx using the “request per second” metric.

Perform some load on it and test it that it scales up.





## HowTo
1. install minikube and kubectl

    Make sure to enable the ingress addon

        minikube addons enable ingress

2. build docker image locally:

    use the following commands to build the container(from the flask-app directory):

        eval $(minikube docker-env)
        docker build -t k8s/flask-nginx .


3. run deployment:

        kubectl apply -f flask.yml

4. get the url:
    
        minikube service flaskapi --url

