#!/bin/sh

gcloud run deploy appx-webapp-staging \
    --platform=managed \
    --image=gcr.io/instabase-appx/webapp:main \
    --region=us-west4 \
    --allow-unauthenticated \
    --update-env-vars=[BACKEND_URL=www.staging.urlwontwork.com]

gcloud run deploy appx-backend-staging \
    --platform=managed \
    --image=gcr.io/instabase-appx/backend:main \
    --region=us-west4 \
    --allow-unauthenticated \
    --update-env-vars=[DB_URL=mongodb+srv://appx-app:Xgd9LayEiGmMMHkI@cluster0.dcecc.mongodb.net/tasks?retryWrites=true&w=majority]
