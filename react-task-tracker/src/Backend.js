const {GoogleAuth} = require('google-auth-library');
const auth = new GoogleAuth();

let googleAuthClient;
const BACKEND_URL = 'https://appx-backend-cn4iaeqs6q-wn.a.run.app'

// renderRequest creates a new HTTP request with IAM ID Token credential.
// This token is automatically handled by private Cloud Run (fully managed) and Cloud Functions.
const renderRequest = async (route, serviceRequestOptions) => {
  const url = `${BACKEND_URL}/${route}`
  console.log(`Sending request ${route} to ${BACKEND_URL}`)
  try {
    // Create a Google Auth client with the Renderer service url as the target audience.
    if (!googleAuthClient) googleAuthClient = await auth.getIdTokenClient(url);
    // Fetch the client request headers and add them to the service request headers.
    // The client request headers include an ID token that authenticates the request.
    const clientHeaders = await googleAuthClient.getRequestHeaders();
    serviceRequestOptions.headers['Authorization'] =
      clientHeaders['Authorization'];
    console.log('Received gcloud auth token')
  } catch (err) {
    throw Error('could not create an identity token: ', err);
  }

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