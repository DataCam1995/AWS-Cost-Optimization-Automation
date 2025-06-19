# AWS-Cost-Optimization-Automation
# AWS Cost Optimization & Automation

## Overview
Developed an automated AWS cost monitoring and optimization solution using CloudWatch, Budgets, and Lambda. This project proactively reduces monthly cloud expenses by shutting down unused EC2 instances and alerting on budget thresholds.

## Architecture
- **CloudWatch** monitors EC2 usage and costs
- **AWS Budgets** triggers alerts when thresholds are exceeded
- **Lambda** shuts down idle EC2 instances
- **SNS** sends email notifications

## Tools & Services
- Amazon CloudWatch
- AWS Budgets
- AWS Lambda
- EC2
- IAM & SNS

## Outcome
- Reduced monthly AWS costs by 15%
- Achieved proactive cloud governance with minimal manual intervention

## Future Enhancements
- Extend automation to RDS and EBS volumes
- Add Slack integration for budget
