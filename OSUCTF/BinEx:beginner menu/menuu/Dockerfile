# Use a base image that includes necessary libraries for binary exploitation challenges, such as Ubuntu.
FROM ubuntu:latest

# Install any dependencies your challenge might need.
# For a basic pwn challenge, you might not need anything,
# but you can use this section to install libraries, debugging tools, etc.
RUN apt-get update && apt-get install -y \
    socat \
 && rm -rf /var/lib/apt/lists/*

# Create a directory for your challenge
WORKDIR /ctf

# Copy the executable and the flag into the container.
COPY menu /ctf/menu
COPY flag.txt /ctf/flag.txt

# Make sure the executable is runnable
RUN chmod +x /ctf/menu

# Expose the port your challenge will run on
EXPOSE 101010

# Use socat to listen on the exposed port and run the executable when a connection is made.
# Adjust the command according to your challenge's requirements.
CMD ["socat", "TCP-LISTEN:101010,reuseaddr,fork", "EXEC:/ctf/menu,stderr"]
