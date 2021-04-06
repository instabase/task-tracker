1. Install google cloud:

```bash
bash -c "curl -sSL https://sdk.cloud.google.com > /tmp/gcl" > install-gcloud.log
bash /tmp/gcl --disable-prompts >> install-gcloud.log
```

2. Authenticate the CLI

```bash
gcloud auth login # requires user interaction
```

3. Go into the webapp and deploy it:

```bash
cd react-task-tracker
make build-docker run-docker deploy-dev
```

4. Go into the backend app and deploy it:

```bash
# to be done / added
```
