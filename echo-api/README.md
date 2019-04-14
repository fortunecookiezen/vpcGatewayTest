# echo-api

Api Gateway exposing a Lambda function at /echo that accepts a POST to provide an ip-echo endpoint for vpc connectitivity testing

Use this with a test client such as `curl` or my vpcGatewayTest Lambda function.
Use with a test like:

```bash
curl --request POST curl --request POST https://foobahdobabar.execute-api.us-east-1.amazonaws.com/echo
```

which will return something like:

```bash
{
  "ip": "10.15.3.47"
}
```

The included CloudFormation will deploy the entire stack for a public edge echo api or a private vpclink api. The vpc link api requires a vpc endpoint in the same vpc. `endpoint.yaml` can be used to create one. If you're concerned about the wide-open api policy, the security group applied to the vpc endpoint can be used to restrict access.

--jim
