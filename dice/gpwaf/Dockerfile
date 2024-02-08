FROM node:21-alpine

WORKDIR /app

COPY flag.txt /flag.txt
COPY package* .
RUN npm ci
ENV OPENAI_API_KEY=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
COPY index.js .

CMD node index.js