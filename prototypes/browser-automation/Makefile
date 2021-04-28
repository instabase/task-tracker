BACKEND_IMAGE_NAME=backend-browtomation


build-docker:
	docker build . -t $(BACKEND_IMAGE_NAME)

run-docker-selenium:
	docker run $(BACKEND_IMAGE_NAME) python scripts/update_dob_selenium.py --new-dob 11/15/1992

run-docker-playwright:
	docker run $(BACKEND_IMAGE_NAME) python scripts/update_dob_playwright.py --new-dob 11/15/1992


