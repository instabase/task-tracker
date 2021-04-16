

install-deps:
	pip install jinja2-cli --user

test-deployment: render-staging
	cloud-build-local -config cloudbuild.yaml -substitutions=_ENVIRON=staging --dryrun=false .

render-prod:
	python -m jinja2cli.cli --strict -o prod/deploy.sh templates/deploy.sh prod/data.json 

render-staging:
	python -m jinja2cli.cli --strict -o staging/deploy.sh templates/deploy.sh staging/data.json 

deploy-prod: 
	gcloud builds submit --config cloudbuild.yaml --substitutions=_ENVIRON=prod

deploy-staging:
	gcloud builds submit --config cloudbuild.yaml --substitutions=_ENVIRON=staging
