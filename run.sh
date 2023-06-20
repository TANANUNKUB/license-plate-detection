docker pull python:3.10

docker build --tag license-plate-detection .

docker run --name license-plate-detection -p 80:80 -d license-plate-detection

echo "server is running on http://localhost:80"
