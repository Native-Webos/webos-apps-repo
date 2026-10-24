# Testing

Automated checks cover valid empty feeds, more apps than a pagination page, inline and linked
manifest schema compatibility, project-prefixed local manifest URLs, package IDs/versions/hashes,
registered-app completeness and generated HTML links. Synthetic records are test-only.
CI also retains upstream package lint and firmware compatibility checks for registration PRs.

Physical TV acceptance remains required on LG OLED65C1PTB, webOS 6.5.3:

1. Record Homebrew Channel version, webOS release and Developer Mode status.
2. Add the complete feed URL and refresh; an empty catalog should load without a repository error.
3. Once a real approved app exists, verify title, icon, details and requirements.
4. Install, launch and record the installed version. Collect installer errors and app logs.
5. Publish a higher package version with matching manifest/hash, refresh the repository after deployment,
   confirm Update is enabled, install and relaunch.
6. Verify persistence after Homebrew restart; test unavailable icons/downloads and malformed feeds in
   a separate test source, never by breaking the production feed.

Use Developer Mode tools or Dev Manager for installation/log collection when root is unnecessary.
Native kit apps may provide /tmp/<app-id>/events.log. Log locations for other apps depend on the app.
Do not report a TV installation as passing until actually observed.
