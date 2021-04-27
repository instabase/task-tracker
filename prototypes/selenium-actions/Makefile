BACKEND_IMAGE_NAME=backend-selenium


build-docker:
	docker build . -t $(BACKEND_IMAGE_NAME)

run-docker:
	docker run $(BACKEND_IMAGE_NAME) python scripts/update_dob.py --new-dob 11/15/1992

