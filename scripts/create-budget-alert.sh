#!/bin/bash

aws budgets create-budget \
  --account-id YOUR_ACCOUNT_ID \
  --budget file://budget.json \
  --notifications-with-subscribers file://notification.json
Add script to create AWS budget and alert policy
