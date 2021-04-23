const BACKEND_URL = "https://appx-backend-cn4iaeqs6q-wn.a.run.app";
const WEBAPP_URL = "https://appx.instabase.com";

// renderRequest creates a new HTTP request with IAM ID Token credential.
// This token is automatically handled by private Cloud Run (fully managed) and Cloud Functions.
const renderRequest = async (route, serviceRequestOptions) => {
  const url = `${BACKEND_URL}/${route}`;
  if (!("headers" in serviceRequestOptions)) {
    serviceRequestOptions.headers = {};
  }
  serviceRequestOptions.headers["Access-Control-Allow-Origin"] = WEBAPP_URL;

  const serviceResponse = await fetch(url, serviceRequestOptions);
  return serviceResponse;
};

export default renderRequest;
