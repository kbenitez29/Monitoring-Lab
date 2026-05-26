deploy:
	ansible-playbook -i ansible/inventory.ini ansible/deploy.yml

status:
	kubectl get pods -A

app:
	kubectl get pods -n flask-app

logs:
	kubectl logs -n flask-app deployment/flask-app-deployment

grafana:
	kubectl port-forward --address 0.0.0.0 svc/monitoring-grafana  3000:80 -n monitoring

destroy:
	kubectl delete namespace flask-app
	kubectl delete namespace monitoring


