# Native-Webos Apps Repository

This repository accepts **native LG webOS applications only**. Both the release manifest and
IPK `appinfo.json` must use `type: native`. Web apps and web wrappers are not accepted.
Start building with the [Native-Webos Native App Kit](https://github.com/Native-Webos/webos-native-app-kit).
Independently built native apps are welcome; the kit is recommended, not mandatory.

An independent LG webOS Homebrew Channel source, adapted from
[webosbrew/apps-repo](https://github.com/webosbrew/apps-repo). It retains upstream's
YAML registrations, Python/Pelican generator, website and scheduled manifest refreshes.
It is not the official webosbrew repository.

## Add to Homebrew Channel

Open **Settings → Repositories → Add repository** and enter:

```
https://native-webos.github.io/webos-apps-repo/api/apps.json
```

Website: https://native-webos.github.io/webos-apps-repo/

The initial catalog contains no applications. Only reviewed registrations appear.
The optional non-free pool is a separate source at
`https://native-webos.github.io/webos-apps-repo/api/non-free/apps.json`.

## Register an application

1. Publish a real `.ipk` and Homebrew manifest in the application's public GitHub Releases.
2. Add `packages/<application-id>.yml`, using the upstream registration format.
3. Submit a pull request here. Metadata, IPK identity/version/hash and generated output are checked.
4. After review and merge, Pages publishes the app. Scheduled builds refresh registered manifests
   every three hours; maintainers can also run **Site: Deploy** manually.

See [ADD_APP](docs/ADD_APP.md), [RELEASES](docs/RELEASES.md) and
[CONTRIBUTING](CONTRIBUTING.md). IPKs stay in their application's Releases, rather than in Git or Pages.
There is no organization-wide automatic app discovery. Moving manifest URLs must resolve to a
version-specific IPK whose bytes match `ipkHash.sha256`. Never replace an existing release asset.

## Development

Python 3.11 or newer:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m repogen.validate_repo
CI=true invoke build
python -m repogen.verify_site
```

`invoke reserve` builds and serves locally at http://localhost:8000.
`REPO_SITE_URL` overrides the production base URL when testing another deployment.
No custom domain is configured. See [DEPLOYMENT](docs/DEPLOYMENT.md).

## Compatibility and updates

Use a recent Homebrew Channel release with Developer Mode support (0.7.2 or newer).
An active Developer Mode session is required for that installation route; root-only apps
still require root. Homebrew Channel enables Update when versions differ, so publishers must
increase the three-part package version. There is no unattended update mechanism here.
Refresh the browser and open the application's details to install an update.

Native firmware compatibility and actual installation require TV testing; feed validation alone
cannot establish them. See [TESTING](docs/TESTING.md) and [TROUBLESHOOTING](docs/TROUBLESHOOTING.md).

## Attribution

Based on upstream commit `291da2bce269fbc901a0716b645caf64f709e3dc`.
The upstream history and Apache-2.0 [LICENSE](LICENSE) are retained. The upstream theme is reused.
Native-Webos changes configure project-path Pages hosting, initialize an empty catalog, disable
Python application registrations, adapt documentation and add validation. See
[RESEARCH](docs/RESEARCH.md) and [ARCHITECTURE](docs/ARCHITECTURE.md).

Report repository issues at https://github.com/Native-Webos/webos-apps-repo/issues.
