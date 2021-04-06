WEBAPP_IMAGE_NAME=appx-webapp
GCLOUD_CONTAINER_URL=gcr.io
GCLOUD_PROJ_NAME=instabase-appx
GCLOUD_DOCKER_NAME_PREFIX=$(GCLOUD_CONTAINER_URL)/$(GCLOUD_PROJ_NAME)


build-docker:
	docker build . -t $(WEBAPP_IMAGE_NAME):$(USER)

push-docker:
	docker tag $(WEBAPP_IMAGE_NAME):$(USER) $(GCLOUD_DOCKER_NAME_PREFIX)/$(WEBAPP_IMAGE_NAME)
	docker push $(GCLOUD_DOCKER_NAME_PREFIX)/$(WEBAPP_IMAGE_NAME)

deploy-dev:
	gcloud run deploy $(WEBAPP_IMAGE_NAME) \
		--platform=managed \
		--image=$(GCLOUD_DOCKER_NAME_PREFIX)/$(WEBAPP_IMAGE_NAME)  \
		--region=us-west4 \
		--allow-unauthenticated
		

