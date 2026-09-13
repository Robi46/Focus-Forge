# Audio Diagnostic Notes

The browser preview intentionally reports `preview-only` when **Test beep** is pressed. This prevents the preview surface from being mistaken for Android notification-channel or background-audio verification.

The Android test path is the newly built APK: enable **Audible study cues**, allow notifications, then open **Settings** and press **Test beep**. The app reports whether playback was requested, disabled, or unavailable.
