#!/bin/sh

gcloud run deploy appx-webapp-{{ENV}} \
    --platform=managed \
    --image=gcr.io/instabase-appx/webapp:{{WEBAPP_IMAGE_TAG}} \
    --region=us-west4 \
    --allow-unauthenticated \
    --update-env-vars=[BACKEND_URL={{BACKEND_URL}}]

gcloud run deploy appx-backend-{{ENV}} \
    --platform=managed \
    --image=gcr.io/instabase-appx/backend:{{BACKEND_IMAGE_TAG}} \
    --region=us-west4 \
    --allow-unauthenticated \
    --update-env-vars=[DB_URL={{DB_URL}}]
