const BACKEND_URL = '34.125.9.86:80'
const WEBAPP_URL = '34.125.150.14:8080'

// renderRequest creates a new HTTP request with IAM ID Token credential.
// This token is automatically handled by private Cloud Run (fully managed) and Cloud Functions.
const renderRequest = async (route, serviceRequestOptions) => {
  const url = `${BACKEND_URL}/${route}`
  if (!('headers' in serviceRequestOptions)) {
    serviceRequestOptions.headers = {}
  }
  serviceRequestOptions.headers['Access-Control-Allow-Origin'] = WEBAPP_URL
  
  const serviceResponse = await fetch(url, serviceRequestOptions);
  return serviceResponse;
};

export default renderRequest;