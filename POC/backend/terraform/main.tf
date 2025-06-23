provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "data_pura_vida" {
  name = "data-pura-vida-cluster"
}

resource "aws_ecs_task_definition" "flask_app" {
  family                   = "data-pura-vida-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  container_definitions = jsonencode([{
    name  = "flask-app"
    image = "your_docker_image"
    portMappings = [{ containerPort = 5000, hostPort = 5000 }]
  }])
}

resource "aws_ecs_service" "data_pura_vida_service" {
  name            = "data-pura-vida-service"
  cluster         = aws_ecs_cluster.data_pura_vida.id
  task_definition = aws_ecs_task_definition.flask_app.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    subnets         = ["subnet-12345678"]
    security_groups = ["sg-12345678"]
    assign_public_ip = true
  }
}