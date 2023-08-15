FROM fluent/fluentd:edge-debian

USER root

# Installing required tools and Python
RUN apt-get update -y && \
    apt-get install -y build-essential libstdc++-10-dev python3

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and Fluentd configuration to the /app directory
COPY dummy_logs.py .
COPY fluentd/fluentd.conf .
COPY fluentd/log/dummy.log .

# Installing gems
RUN gem install fluent-plugin-kubernetes_metadata_filter -v 3.2.0
RUN gem install elasticsearch -v 7.10.1
RUN gem install fluent-plugin-elasticsearch -v 5.0.5
