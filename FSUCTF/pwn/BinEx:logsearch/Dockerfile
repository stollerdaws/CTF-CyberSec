FROM ubuntu:20.04

# Enable multi-arch support for i386 (32-bit)
RUN dpkg --add-architecture i386

# Update packages and install necessary 32-bit libraries
RUN apt-get update && apt-get install -y \
    socat \
    libc6:i386 \
    libncurses5:i386 \
    libstdc++6:i386

# Copy your challenge files and any other necessary files
COPY ./logsearch /logsearch
COPY ./logs.txt /logs.txt
COPY ./flag.txt /flag.txt
COPY ./start.sh /start.sh

# Expose the necessary port (adjust if different)
EXPOSE 1993

# Set the entrypoint to your start script
ENTRYPOINT ["/start.sh"]
