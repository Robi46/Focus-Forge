# FocusForge Play Store Research Notes

## Official findings gathered on 23 August 2026

1. Google’s Android Developers guidance states that from **31 August 2026**, new apps and updates submitted to Google Play must target **Android 16 / API level 36** or higher. FocusForge’s effective release target must be verified and, if below 36, updated before submission. [1]
2. Google Play lists the app icon, short description, feature graphic, screenshots, and optional video as preview assets. The preview-asset requirements are mandatory where stated, and the assets must follow the Developer Program Policies. [2]
3. Google Play treats the installed-app inventory accessed through `QUERY_ALL_PACKAGES` as personal and sensitive information. The permission is allowed only when broad app search is necessary for the app’s core user-facing purpose, when a less intrusive method is insufficient, and with an accurate Permissions Declaration Form. For a study timer whose primary value is timing and local planning, the safe release decision is to remove broad installed-app scanning and retain a manual emergency-app checklist. [3]
4. Google Play requires developers to complete and maintain an accurate Data safety section, including app and third-party SDK behavior. The Play form includes a privacy-policy requirement. FocusForge’s planned release configuration is local-only: study history, goals, notes, routines, and selected emergency-app labels remain on the device and are not transmitted to a developer server. This declaration must be rechecked if analytics, ads, accounts, cloud backup, or third-party SDKs are later added. [4]

## Immediate release risks to resolve

| Risk | Current state | Planned response |
| --- | --- | --- |
| Target SDK | Not yet verified at API 36 | Verify effective Expo/Android target; upgrade tooling or build settings if necessary. |
| Broad package visibility | `QUERY_ALL_PACKAGES` declared for installed-app scanning | Prefer removal for the Play release unless a clearly eligible core use case and declaration can be substantiated. |
| DND policy access | Used only to request/enable user-approved Priority DND | Keep feature opt-in, explain Android ownership of exceptions, and disclose behavior accurately. |
| Locked-screen cues | Requires local notifications, user notification permission, channel sound settings, and a fresh installed APK | Keep channel diagnostics and publish an explicit test checklist. |

## Sources

[1]: https://developer.android.com/google/play/requirements/target-sdk "Android Developers: Target API level requirement"
[2]: https://support.google.com/googleplay/android-developer/answer/9866151?hl=en "Play Console Help: Add preview assets to showcase your app"
[3]: https://support.google.com/googleplay/android-developer/answer/10158779?hl=en "Google Play Help: Use of the broad package (App) visibility permission"
[4]: https://support.google.com/googleplay/android-developer/answer/10787469?hl=en-GB "Google Play Help: Provide information for Google Play's Data safety section"
