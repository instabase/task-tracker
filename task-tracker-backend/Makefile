BACKEND_IMAGE_NAME=appx-backend
GCLOUD_CONTAINER_URL=gcr.io
GCLOUD_PROJ_NAME=instabase-appx
GCLOUD_DOCKER_NAME_PREFIX=$(GCLOUD_CONTAINER_URL)/$(GCLOUD_PROJ_NAME)

# Set current working directory to /workspace/task-tracker-backend if PWD is undefined
# (PWD doesn't work on google cloud, so this is the hard-coded backup)
CWD=$(PWD)
ifeq ($(CWD),)
CWD=/workspace/task-tracker-backend
endif

# Use git to get branch name if it's not specified via environment variable
# Branch name is not accessible via git in cloud build
ifeq ($(BRANCH_NAME),)
BRANCH_NAME=$$(git rev-parse --abbrev-ref HEAD)
endif

# Docker image tag name cannot contain hyphens but branches typically do
IMAGE_TAG=$$(echo $(BRANCH_NAME) | sed 's:/:-:g')


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
	docker run -v $(CWD):/workspace $(BACKEND_IMAGE_NAME) python -m pytest /workspace/app/tests

push-docker: 
	docker tag $(BACKEND_IMAGE_NAME) $(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME):$(IMAGE_TAG)
	docker push $(GCLOUD_DOCKER_NAME_PREFIX)/$(BACKEND_IMAGE_NAME):$(IMAGE_TAG)

