# Architecture

App repository Releases (IPK + Homebrew manifest) → reviewed packages/<id>.yml → upstream repogen/Pelican
→ validation → GitHub Pages artifact → website and /api/apps.json → Homebrew Channel.
Homebrew downloads the IPK directly from Releases, verifies SHA-256 and calls webOS appInstallService.
The same upstream metadata drives the feed and website. Main/non-free pools remain separate.

Use upstream's generator rather than a replacement catalog system. The Native-Webos changes are
project URL handling, empty-catalog initialization, documentation, YAML-only registration and validation.
The external upstream theme remains a constrained dependency. No new custom app-store frontend is built.

Failure recovery preserves the last good deployment. Every build verifies registered app completeness.
No unsupported architecture/dependency selection is advertised; compatibility is recorded and tested per app.
The native app kit can supply packages, but the repository has no build-time dependency on it.
See TESTING.md for automated and TV checks and RELEASES.md for update lifecycle and rollback risks.
