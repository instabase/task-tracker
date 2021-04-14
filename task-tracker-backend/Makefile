BACKEND_IMAGE_NAME=appx-backend
GCLOUD_CONTAINER_URL=gcr.io
GCLOUD_PROJ_NAME=instabase-appx
GCLOUD_DOCKER_NAME_PREFIX=$(GCLOUD_CONTAINER_URL)/$(GCLOUD_PROJ_NAME)


build-docker:
	docker build . -t $(BACKEND_IMAGE_NAME)

deploy-dev:
	gcloud run deploy $(BACKEND_IMAGE_NAME) \
		--platform=managed \
		--image=$(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME)  \
		--region=us-west4 \
		--allow-unauthenticated

test:
	pytest app/tests

test-docker:
	docker run -v $(PWD):/workspace $(BACKEND_IMAGE_NAME) python -m pytest /workspace/app/tests

cloud-build-ci: build-docker test-docker
	docker tag $(BACKEND_IMAGE_NAME) $(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME):$(BRANCH_NAME)
	docker push $(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME):$(BRANCH_NAME)

