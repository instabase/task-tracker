WEBAPP_IMAGE_NAME=appx-webapp
NODE_CONTAINER=node:12.16
GCLOUD_CONTAINER_URL=gcr.io
GCLOUD_PROJ_NAME=instabase-appx
GCLOUD_DOCKER_NAME_PREFIX=$(GCLOUD_CONTAINER_URL)/$(GCLOUD_PROJ_NAME)

# Set current working directory to /workspace/task-tracker-backend if PWD is undefined
# (PWD doesn't work on google cloud, so this is the hard-coded backup)
CWD=$(PWD)
ifeq ($(CWD),)
CWD=/workspace/react-task-tracker
endif

# Docker image tag name cannot contain hyphens but branches typically do
IMAGE_TAG=$$(echo $(BRANCH_NAME) | sed 's:/:-:g')

build-from-scratch:
	npm install
	npm run build

build-docker:
	docker run -v $(CWD):/workspace -w /workspace $(NODE_CONTAINER) make build-from-scratch
	docker build . -t $(WEBAPP_IMAGE_NAME)

deploy-dev:
	gcloud run deploy $(WEBAPP_IMAGE_NAME) \
		--platform=managed \
		--image=$(GCLOUD_DOCKER_NAME_PREFIX)/$(WEBAPP_IMAGE_NAME)  \
		--region=us-west4 \
		--allow-unauthenticated


push-docker:
	docker tag $(WEBAPP_IMAGE_NAME) $(GCLOUD_DOCKER_NAME_PREFIX)/$(WEBAPP_IMAGE_NAME)
	docker push $(GCLOUD_DOCKER_NAME_PREFIX)/$(WEBAPP_IMAGE_NAME)

test:
	# CI=true disables watch mode + prevents saving new screenshots
	CI=true npm run test

test-docker:
	docker run -v $(CWD):/workspace -w /workspace $(NODE_CONTAINER) make test

		

