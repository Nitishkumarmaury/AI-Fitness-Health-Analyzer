### Issues Encountered

1. **ECR Tagging Error**:
   - The command `docker tag "$ECR_REPOSITORY:latest" $fullEcrUri` failed because the `$fullEcrUri` variable was not correctly formatted. The correct command should be:
     ```powershell
     docker tag "$ECR_REPOSITORY:latest" "$fullEcrUri"
     ```

2. **Image Push Failure**:
   - The image push failed because the image was not tagged correctly. Once you fix the tagging issue, this should resolve itself.

3. **IAM Role Creation Access Denied**:
   - You received an `AccessDenied` error when trying to create the ECS task execution role. This indicates that the IAM user you are using does not have the necessary permissions to create roles. You will need to ensure that your IAM user has the `iam:CreateRole` and `iam:AttachRolePolicy` permissions.

4. **Invalid JSON Error**:
   - The error regarding the task definition registration indicates that there might be a Byte Order Mark (BOM) at the beginning of your JSON file. This can happen if the file was saved with UTF-8 encoding with BOM. To fix this, you can use the following command to create the JSON file without BOM:
     ```powershell
     $taskDefJson | Out-File -FilePath "task-definition.json" -Encoding ASCII
     ```

### Suggested Fixes

Here’s a revised version of the relevant parts of your script:

```powershell
# Step 8: Tag image for ECR
Write-Host "🏷️ Tagging image for ECR..." -ForegroundColor Yellow
docker tag "$ECR_REPOSITORY:latest" "$fullEcrUri"

# Step 9: Push image to ECR
Write-Host " Pushing image to ECR..." -ForegroundColor Yellow
docker push "$fullEcrUri"

# Step 12: Create task execution role (if not exists)
# Ensure you have the necessary permissions to create roles

# Step 13: Create task definition
Write-Host " Creating task definition..." -ForegroundColor Yellow
$taskDefinition = @{
    family = $TASK_DEFINITION
    networkMode = "awsvpc"
    requiresCompatibilities = @("FARGATE")
    cpu = "512"
    memory = "1024"
    executionRoleArn = "arn:aws:iam::$accountId:role/ecsTaskExecutionRole"
    containerDefinitions = @(
        @{
            name = "ai-fitness-container"
            image = $fullEcrUri
            portMappings = @(
                @{
                    containerPort = 8501
                    protocol = "tcp"
                }
            )
            environment = @(
                @{
                    name = "GEMINI_API_KEY"
                    value = "AIzaSyCmCit_f6F6EBC6yEIeith1apjJ8AH3rWY"
                }
            )
            logConfiguration = @{
                logDriver = "awslogs"
                options = @{
                    "awslogs-group" = "/ecs/ai-fitness-analyzer"
                    "awslogs-region" = $AWS_REGION
                    "awslogs-stream-prefix" = "ecs"
                }
            }
            essential = $true
        }
    )
}

$taskDefJson = $taskDefinition | ConvertTo-Json -Depth 10
$taskDefJson | Out-File -FilePath "task-definition.json" -Encoding ASCII

aws ecs register-task-definition --cli-input-json file://task-definition.json --region $AWS_REGION
```

### Next Steps

1. **Check IAM Permissions**: Ensure your IAM user has the necessary permissions to create roles and attach policies.
2. **Fix the JSON Encoding**: Use the ASCII encoding when saving the task definition JSON to avoid BOM issues.
3. **Retry the Deployment**: After making these changes, run the script again from the beginning.

If you encounter any further issues, please provide the error messages, and I'll be happy to assist you!