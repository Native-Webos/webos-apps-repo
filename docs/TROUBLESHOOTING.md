# Troubleshooting

- Repository error: enter the full api/apps.json URL, verify public HTTP 200 and JSON, and refresh.
- No apps: initial catalog is intentionally empty; check registration, pool and latest successful build.
- Missing icons: check absolute HTTPS URLs and the project path in generated links.
- Download or checksum failure: inspect the version-specific release asset and recompute SHA-256;
  never bypass hash checking or overwrite a released package.
- Installation failure: record the installer error, Developer Mode session, free space and firmware ABI.
- Updates absent: confirm a different three-part package version and successful Pages refresh.
- Pages 404: enable Actions publishing and check github-pages environment and main-branch permissions.
- Workflow failure: distinguish invalid submission from source/network/tool failure; retry only transient errors.
- API limits: respect retry-after and reset headers. Never place private tokens in public assets.
