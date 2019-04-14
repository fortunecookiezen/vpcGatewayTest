# vpcGatewayTest

Lambda function to test vpc connectitivity

Original Lambda Author: John Pope

Original Lambda source: https://github.com/pope-tech/aws-lambda-nat-gateway-test  

I forked this and then cut it down from John's original demo to just include http endpoint functionality. Use this as a quick and dirty way of determining if your lambda functions operating in vpc can reach http endpoints. For the test to succeed, you must pick an endpoint that will return a 200 response. I use it to validate things like TransitGateway routes are working correctly without the need to spin up an EC2 instance in an account just to run `curl`

Use with a test like:

```bash
{
  "url": "https://api.ipify.org?format=json",
  "method": "GET"
}
```

The included CloudFormation will deploy the Lambda into a VPC and create the necessary IAM Role.

ToDo: Include Lambda Test in cloudformation (Q: is this even a thing? A: nope, cloudformation does not support this. You will need to add the tests by hand through the console after deployment)

--jim
