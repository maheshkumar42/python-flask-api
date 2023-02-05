FROM python:3.10.0-alpine3.14

# Install dependencies
RUN apk update
RUN pip3 install --no-cache-dir pipenv

# Copy the Pipfile and Pipfile.lock
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY cashman ./cashman

# Install API dependencies
RUN pipenv install --system --deploy --dev

# Run the API
EXPOSE 5001
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
