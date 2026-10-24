# Research baseline

Research date: 2026-10-24. Upstream apps-repo commit:
291da2bce269fbc901a0716b645caf64f709e3dc. Homebrew Channel source inspected at
1a2b969e992617c9ba4b8a891542cb93a9e07b0a and release v0.7.3.

Verified from frontend/views/SettingsPanel.js and configutils.js: users add a complete JSON URL,
stored in localStorage. BrowserPanel.js consumes packages and does not follow pagination.
DetailsPanel.js uses an inline manifest or fetches manifestUrl, resolves download URLs, displays
rootRequired and enables updates on version inequality rather than semantic ordering.
services/service.ts downloads, checks SHA-256 and calls com.webos.appInstallService/dev/install.
Developer Mode routing exists; v0.7.2 release notes document its fix. No TV test was performed.

Upstream apidata.py emits a whole-feed apps.json, numbered pages, per-app latest JSON and HTML
descriptions. Metadata comes from packages YAML and external release manifests. Upstream schemas
needed two corrections: permit both manifest and manifestUrl, and describe emitted paging metadata.
Empty feeds work in source; physical-TV acceptance is still required.

Categories and screenshots support the website; the inspected HBC has no category browser or dedicated
screenshot binding. Requirements are not enforced by HBC. Developer/vendor, dependencies and CPU
selection are not supported client features. Root metadata is descriptive. Integrity hashes do not
authenticate publishers. Package metadata must agree across control, appinfo and manifest.

Pages supports static JSON and project paths. Releases are appropriate for binaries; the official
feed already uses public GitHub Release downloads. No runtime server is required. Organization
policies, target-TV TLS/redirect behavior and first real app availability require deployment/hardware checks.

Sources:
- https://github.com/webosbrew/webos-homebrew-channel/tree/1a2b969e992617c9ba4b8a891542cb93a9e07b0a
- https://github.com/webosbrew/apps-repo/tree/291da2bce269fbc901a0716b645caf64f709e3dc
- https://repo.webosbrew.org/api/apps.json
- https://github.com/throwaway96/apps-repo/tree/4742639cbd30635e05034d51428b7ab1204ec1ef
- https://github.com/Native-Webos/webos-native-app-kit/tree/96eecfbfe6448d56f212dbed76c0d61d02694bc3
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- https://webostv.developer.lge.com/develop/getting-started/developer-mode-app
