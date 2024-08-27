# Start Minikube and Kind 

Minikube: minikube start
Kind: kind create cluster

# Deploy Services

kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml

# Access Front End

Get the NodePort for the frontend service and enter following site in browser
http://<Minikube IP>:<NodePort>

# Run Test Script:
python3 integration_test.py