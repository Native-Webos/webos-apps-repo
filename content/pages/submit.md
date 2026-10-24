Title: Submit a Native App
URL: submit
save_as: submit.html
status: hidden
Description: Submit a native LG webOS application to the Native-Webos repository.

Native-Webos accepts **native LG webOS applications only**. Both the release manifest and the
IPK's `appinfo.json` must declare `type: native`. Web applications and web wrappers are not eligible.
Submissions are reviewed for functionality, compatibility and distribution rights.

## Build with the Native App Kit

The [Native-Webos Native App Kit](https://github.com/Native-Webos/webos-native-app-kit) is our
recommended starting point for building, packaging and verifying native webOS apps.
Independently developed native applications are welcome; using the kit is not required.

## Prepare your release

1. Build and test your native application on a compatible LG webOS TV.
2. Publish the `.ipk` and a matching Homebrew manifest in public GitHub Releases.
3. Include the exact package version, a fixed IPK download URL and its SHA-256 checksum.
4. Document supported firmware, CPU architecture, root requirements and test results.

## Register your application

Submit a YAML registration under `packages/<application-id>.yml` through a pull request to
[Native-Webos/webos-apps-repo](https://github.com/Native-Webos/webos-apps-repo).
Read the [application registration guide](https://github.com/Native-Webos/webos-apps-repo/blob/main/docs/ADD_APP.md)
for the complete format. Checks validate native type, package identity, version and checksum before publication.

Keep IPKs in Releases and preserve installed app IDs. Respect licences and redistribution rights.
No piracy, DRM bypass or firmware modifications. Only approved apps appear in the catalog.

For repository problems, [open an issue](https://github.com/Native-Webos/webos-apps-repo/issues/new/choose).
