# Image-recognition-using-IBM-Watson-MacOS

### Before you begin
* You need an [IBM Cloud](https://cloud.ibm.com/registration?target=/developer/watson&cm_sp=WatsonPlatform-WatsonServices-_-OnPageNavLink-IBMWatson_SDKs-_-Python "IBM Cloud website") account.

### Installation
* To install, use `pip`

 Watson
```bash
pip3 install --upgrade watson-developer-cloud
```
 Json
```bash
pip3 install jsonlib-python3
```
 gTTS
```bash
pip3 install gTTS
```
 OpenCV
```bash
pip3 install opencv-python
```
 Abspath
```bash
pip3 install abspath
```

### IAM

IBM Cloud has migrated to token-based Identity and Access Management (IAM) authentication. IAM authentication uses a service API key to get an access token that is passed with the call. Access tokens are valid for approximately one hour and must be regenerated.

You supply either an IAM service **API key** or an **access token**:

- Use the API key to have the SDK manage the lifecycle of the access token. The SDK requests an access token, ensures that the access token is valid, and refreshes it if necessary.
- Use the access token if you want to manage the lifecycle yourself. For details, see [Authenticating with IAM tokens](https://cloud.ibm.com/docs/services/watson?topic=watson-iam).
- Use a server-side to generate access tokens using your IAM API key for untrusted environments like client-side scripts. The generated access tokens will be valid for one hour and can be refreshed.

