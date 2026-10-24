# Deployment

Target: Native-Webos/webos-apps-repo. GitHub Pages source must be GitHub Actions.
No CNAME is published. Production base: https://native-webos.github.io/webos-apps-repo.

The inherited Site: Deploy workflow runs on main pushes, every three hours, and manual dispatch.
Its reusable generate job installs constrained Python dependencies, runs tests and app validation,
builds with Pelican, verifies generated links/feeds and uploads a Pages artifact. Only the deploy
job needs pages:write and id-token:write; generation needs contents:read. The github-pages environment
must allow main. PR checks build/validate without deployment privileges.

The repository's scheduled refresh consumes release manifests, not a database or GitHub API-driven
app discovery system. Do not add tokens to feed files or artifacts. Public release downloads need
no credentials. Keep build jobs unprivileged and review workflow changes before merging.

To recover: inspect the failing run, correct metadata or retry source availability, then manually
run Site: Deploy. Keep the previous successful deployment until the new build passes.
For a deliberate rollback, review all advertised app versions first.
