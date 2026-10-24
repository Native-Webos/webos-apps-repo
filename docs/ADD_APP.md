# Add an application

Use the existing upstream format. Each real application has one `packages/<id>.yml` registration.
No placeholder applications are published. The following is documentation only: replace every
example URL and ID with verified values before submitting it.

```yaml
title: Your Application
iconUri: https://github.com/OWNER/APP/releases/download/v1.0.0/icon.png
manifestUrl: https://github.com/OWNER/APP/releases/latest/download/manifest.json
category: utility
pool: main
description: |
  Describe what the application does, its compatibility and any root requirement.
```

The release manifest must contain `id`, `title`, `version`, `type`, `iconUri`, `ipkUrl`
and `ipkHash: {sha256: <64 lowercase hex characters>}`. Use an absolute, version-specific
HTTPS IPK URL and calculate the digest from that exact package. Add `sourceUrl` for source code,
`rootRequired` as true/false/optional, and `appDescription` where applicable.
The filename ID, manifest ID and IPK application ID must agree. Control, appinfo and manifest
versions must agree. Package versions use three integers, such as `1.2.3`.

Categories: multimedia, game, system, utility, screensaver, launcher, amblight, internet.
Use `main` for open source and `non-free` otherwise; non-free has a separate feed.
Optional registration fields include screenshots, detailIconUri, funding and requirements.
Use `requirements.webosRelease` only for evidence-backed compatibility claims; Homebrew Channel
does not enforce those constraints in the inspected client.

Publish IPKs in the app repository's GitHub Releases, or an authorized release in this repository.
A public direct IPK URL is also compatible: the release manifest can point to it.
The catalog does not build the app or depend on webos-native-app-kit.
Only YAML registrations are enabled; application definitions cannot execute Python during generation.
Never submit code that modifies firmware/system partitions. Respect upstream licences and distribution rights.
