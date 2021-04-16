# CD process

### Goals

- Keep it simple, no need for google scale, or even IB scale complexity
- Enable automatically updated staging, prod
- Enable manually updated dev-specific environments
- Enable folks to set up multiple environments if they want to

### What works now

- Production is automatically updated with the latest release branch (_not_ the latest release tagged-branch, we should resolve this before actually using this system)
- Staging is automatically updated each time a new branch is merged to master

### What needs to be done:

- The environment-specific variables are passed in, but the code hasn't been changed to use them (instead of hard-coded values that all point to prod). As a result, backend on staging won't get any traffic (all the traffic from the webapp in staging goes to the backend in prod).
- Walkthroughs need to be created on how developers can create and upgrade their specific environments.
