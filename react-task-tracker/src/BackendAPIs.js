const {GoogleAuth} = require('google-auth-library');
const auth = new GoogleAuth();

let googleAuthClient;
const BACKEND_URL = 'https://appx-backend-cn4iaeqs6q-wn.a.run.app'
const WEBAPP_URL = 'https://appx-webapp-cn4iaeqs6q-wn.a.run.app'

// renderRequest creates a new HTTP request with IAM ID Token credential.
// This token is automatically handled by private Cloud Run (fully managed) and Cloud Functions.
const renderRequest = async (route, serviceRequestOptions) => {
  const url = `${BACKEND_URL}/${route}`
  console.log(`Sending request ${route} to ${BACKEND_URL}`)
  if (!('headers' in serviceRequestOptions)) {
    serviceRequestOptions.headers = {}
  }
  serviceRequestOptions.headers['Access-Control-Allow-Origin'] = WEBAPP_URL
  
  try {
    // serviceResponse converts the Markdown plaintext to HTML.
    const serviceResponse = await fetch(url, serviceRequestOptions);
    console.log('Received message from backend')
    return serviceResponse;
  } catch (err) {
    throw Error('request to rendering service failed: ', err);
  }
};

export default renderRequest;