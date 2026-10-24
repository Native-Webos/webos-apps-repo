# Releases and refreshes

This repository follows upstream: registrations point to public Homebrew manifests, commonly a
`releases/latest/download/manifest.json` asset. Scheduled Pages builds resolve those manifests every
three hours, validate registered packages, and regenerate the website and both feeds. No custom
release-discovery service or catalog lock format is introduced.

In each application repository: build and test the IPK, calculate SHA-256, publish it with a matching
manifest, and make that release current only when both assets are available. The manifest must
point to a fixed version-specific package URL. Never overwrite an IPK or reduce its version.
GitHub release tags may start with v; the package/manifest version itself must be three integers.
Drafts are not publicly installable. Keep prereleases away from the stable manifest; this catalog
does not implement a separate prerelease-selection engine.

An upstream outage stops validation/deployment, preserving the previous Pages deployment.
An upstream cached manifest may be reused by the inherited generator on fetch failure; scheduled
validation still requires the selected package to be downloadable and match its checksum.
Maintainers should inspect failed runs and retry when the source recovers.

To deprecate an app, explain its status in its description and preserve assets for installed users.
Remove a registration only after review. This does not uninstall copies already on TVs.
Rolling back the site can advertise older versions as updates, so review version behavior first.
