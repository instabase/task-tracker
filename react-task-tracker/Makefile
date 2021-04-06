WEBAPP_IMAGE_NAME=appx-webapp


build-docker:
	docker build . -t $(WEBAPP_IMAGE_NAME):$(USER)

push-docker:
	docker tag $(WEBAPP_IMAGE_NAME):$(USER) gcr.io/instabase-appx/$(WEBAPP_IMAGE_NAME)
	docker push gcr.io/instabase-appx/$(WEBAPP_IMAGE_NAME)

deploy-dev:
	gcloud run deploy $(WEBAPP_IMAGE_NAME) \
		--platform=managed \
		--image=gcr.io/instabase-appx/$(WEBAPP_IMAGE_NAME)  \
		--region=us-west4 \
		--allow-unauthenticated
		

