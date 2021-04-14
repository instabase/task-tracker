BACKEND_IMAGE_NAME=appx-backend
GCLOUD_CONTAINER_URL=gcr.io
GCLOUD_PROJ_NAME=instabase-appx
GCLOUD_DOCKER_NAME_PREFIX=$(GCLOUD_CONTAINER_URL)/$(GCLOUD_PROJ_NAME)
CI_BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)


build-docker:
	docker build . -t $(BACKEND_IMAGE_NAME):$(USER)

build-and-push-docker-ci: 
	docker build . -t $(BACKEND_IMAGE_NAME)
	docker tag $(BACKEND_IMAGE_NAME) $(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME):$(CI_BRANCH_NAME)
	docker push $(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME):$(CI_BRANCH_NAME)

deploy-dev:
	gcloud run deploy $(BACKEND_IMAGE_NAME) \
		--platform=managed \
		--image=$(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME)  \
		--region=us-west4 \
		--allow-unauthenticated

test:
	pytest app/tests


