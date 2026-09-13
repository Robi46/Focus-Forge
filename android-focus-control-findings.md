# Android Focus-Control Findings

## Play-safe Android app

Android 11 and higher filters installed-app visibility by default. Google’s documentation states that an app cannot detect all installed apps unless it declares a permitted use case through `<queries>`; broad `QUERY_ALL_PACKAGES` access is subject to Google Play approval. Installed-app lists are treated as personal and sensitive user data.

A normal Play-distributed app can request notification permission, create notification channels, and guide the user to configure Android Do Not Disturb or Modes. It cannot silently configure the user’s DND exception list, reliably intercept all third-party calls/messages, or prevent Home and Recents navigation.

## Device-owner / kiosk Android app

Android lock task mode is the supported kiosk mechanism for a dedicated device. An approved device policy controller (DPC) must allowlist the packages with `DevicePolicyManager.setLockTaskPackages()`. Lock task mode can restrict the device to one app or an allowlisted set of apps and can prevent access to non-allowlisted apps and the Home screen unless the Home activity is allowlisted.

This is a separate provisioning model from a normal Play install. It requires device-owner or DPC provisioning and should be treated as a dedicated-device build, not as a promise that an ordinary Play Store installation can enforce kiosk restrictions.

## Product decision

The Play-safe variant should provide accurate setup guidance, permission/status checks, DND routing, Screen Pinning instructions, and reliable scheduled cues. The device-owner variant can add a native DPC/lock-task layer for a user-owned provisioned phone, with explicit warnings about provisioning, reset risk, emergency access, and OEM differences.

Sources:

- https://developer.android.com/training/package-visibility
- https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode
