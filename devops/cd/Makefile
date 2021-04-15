


render-prod:
	jinja2 --format=yaml --strict -o prod/rendered/cloudbuild.yaml templates/cloudbuild.yaml prod/data.json

deploy-prod: 
	gcloud builds submit --config prod/rendered/cloudbuild.yaml

