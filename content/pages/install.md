Title: Add the Native-Webos Repository
URL: install
save_as: install.html
status: hidden

In Homebrew Channel, open **Settings → Repositories → Add repository** and enter:

```
https://native-webos.github.io/webos-apps-repo/api/apps.json
```

Return to the app browser and refresh. The initial catalog is empty until applications are approved.
For closed-source applications, separately add:

```
https://native-webos.github.io/webos-apps-repo/api/non-free/apps.json
```

This source accepts native applications only.

Choose an app, open its details and select Install. Refresh after a release, then open the app's
page and select Update. Homebrew Channel compares version strings for equality; this source must
not regress package versions. Downloads are checked against the manifest's SHA-256.

A functioning Homebrew Channel and installation permissions are required. Developer Mode is
supported by recent Homebrew Channel releases; keep the Developer Mode session active.
Apps requiring root cannot gain root from repository registration. Check each app's requirements.
Repository browsing does not prove that a native app is compatible with a particular firmware.
