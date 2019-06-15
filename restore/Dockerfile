# ──────────────────────────────────────────────────────────────────────
#  Build Vue Application
# ──────────────────────────────────────────────────────────────────────

FROM node:alpine as builder
COPY . .
RUN npm install
RUN npm run build

# ──────────────────────────────────────────────────────────────────────
#  Run Flask Server
# ──────────────────────────────────────────────────────────────────────

FROM python:3.7-alpine
COPY --from=builder /dist /dist
COPY requirements.txt .
COPY restore.py .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "restore.py" ]

