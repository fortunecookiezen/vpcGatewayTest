# vpcGatewayTest
Lambda function to test vpc connectitivity

Original Lambda Author: John Pope

Original Lambda source: https://github.com/pope-tech/aws-lambda-nat-gateway-test  

I forked this and then cut it down from John's original demo to just include http endpoint functionality. Use this as a quick and dirty way of determining if your lambda functions operating in vpc can reach http endpoints. For the test to succeed, you must pick an endpoint that will return a 200 response.

Use with a test like:

```
{
  "url": "https://api.ipify.org?format=json"
}
```
The included CloudFormation will deploy the Lambda into a VPC and create the necessary IAM Role.

ToDo: Include Lambda Test in cloudformation (is this even a thing?)

--jim
