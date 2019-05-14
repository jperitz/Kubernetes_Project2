# Kubernetes_Project2
Teaching myself Docker and Kubernetes

To use:
1. Clone this repository
2. Install Docker-CE, kubectl and minikube
3. Enter the following console commands:
minikube start
kubectl apply -f app-service.yaml,db-service.yaml,app-deployment.yaml,db-deployment.yaml
kubectl describe services (to get the ip address of the app endpoint)
4. Open a web browser and connect to the ip address above, port 5000
5. To view a json dump of the database, the address is $IP:5000/api/data
