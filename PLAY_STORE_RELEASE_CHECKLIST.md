# FocusForge Play Store Release Checklist

This checklist is prepared for a first Google Play submission. It is not a guarantee of approval; Google Play makes the final policy decision after reviewing the owner’s package, account declarations, metadata, and release artifact.

## Completed in this project

| Area | Release preparation |
| --- | --- |
| Android API target | The app config requests compile and target SDK **36** for the August 2026 Play requirement.[1] |
| Release versioning | Android `versionCode` is set to `1`; increment it for every future Play upload. |
| App visibility | `QUERY_ALL_PACKAGES` has been removed. The Play release uses a private manual emergency-app checklist instead of scanning the device app inventory.[2] |
| Advertising integration | The Focus dashboard contains a compact banner and a voluntary rewarded ad that grants 12 locally stored ad-free hours. Google test IDs are configured for safe verification only; replace them with the owner’s AdMob IDs before a revenue release. |
| Privacy and consent | The app gathers Google ad consent where required before initializing the ad SDK. Privacy-policy and Data safety answers must be updated from the final production SDK configuration.[3] |
| Android cues | The installed build creates selectable Classic/Bright/Calm v4 cue channels that request sound and DND bypass, with in-app diagnostics. Real-device testing remains required. |
| Floating session bubble | The user-visible background-session bubble requires Android’s Display over other apps permission, is user-toggleable in Settings, and must be tested in the final build. |
| Store asset preparation | The existing 512 × 512 launcher icon and a 1024 × 500 feature graphic are prepared. Final screenshots must come from the installed build.[4] |

## Required owner actions before submission

1. Create or use your own Google Play developer account, choose a package name that you control, and supply a real developer contact email and privacy-policy URL.
2. Host `PRIVACY_POLICY.md` at a public, non-geofenced HTTPS URL. Do not submit the local project file path as the policy URL.
3. Build a **signed Android App Bundle (`.aab`)** through the project publishing interface or your approved Android build service. New Google Play apps are distributed through Android App Bundles.[5]
4. Upload the AAB to an **internal testing** track first. Run the Android device tests below before promoting it.
5. In Play Console → **App content**, complete: Data safety, privacy policy, ads declaration, content rating, target audience/content, app access, and any current permission declarations. Review every answer against the exact uploaded build.[3]
6. In the Data safety form, disclose the final advertising SDK’s data practices exactly as shown in the current Google Play and AdMob documentation. Do **not** declare “no data collected or shared” once the ad SDK is included. The owner remains responsible for the declaration’s accuracy.[3]
7. Review the exact-alarm request. Keep it only if the final release genuinely needs precise user-facing study timer cues; otherwise remove it. Validate the relevant Android special-access behavior on the target test devices.[6]
8. Add the app icon, feature graphic, store copy, and genuine final-build screenshots using `PLAY_STORE_LISTING.md`.
9. Review the final build’s **Display over other apps** request in Play Console. Its user-visible purpose is a compact active-session counter that opens FocusForge or can be dismissed; do not use it for ads, unrelated prompts, or imitating another app.[7]
10. In Play Console → App content, select **Yes, my app contains ads**. Before submitting a revenue build, replace the Google test App ID and banner/rewarded unit IDs with IDs from the owner’s AdMob account, then rerun internal testing.[8]

## Mandatory device acceptance tests

| Test | Pass condition |
| --- | --- |
| Fresh install | The internal-test AAB installs, opens, and preserves the intended portrait layout. |
| Notification channels | After choosing each available cue sound, Settings → Locked-screen Cue Check finds its matching v4 round/rest channels with sound and DND-bypass requests. |
| Locked-screen rhythm | With Android notification permission, audible channels, compatible DND settings, and unrestricted battery use, the installed app gives one cue after rounds 1–3, three at the rest boundary, and one when rest ends. |
| DND | Priority DND silences non-priority interruptions according to Android’s own mode settings while the FocusForge cue channels are allowed. |
| Floating session bubble | With Display over other apps granted, backgrounding an unpaused session shows a compact counter. The arrow returns to FocusForge and × removes only the bubble, not the session. |
| Banner and reward | The Focus dashboard shows the test banner below study controls. A completed test rewarded ad grants exactly 12 hours without banners; closing or skipping it grants no reward. |
| Manual allowlist | Phone, WhatsApp, Messenger, and a typed custom app can be selected as a local setup checklist; Android DND settings remain the actual enforcement authority. |
| Screen Pinning | The owner verifies that pinning restricts leaving FocusForge and understands that it also prevents opening allowed apps until unpinned. |
| Local data | Study history, notes, folders/tags, and routine blocks remain on the device after a normal app restart. |

## References

[1]: https://developer.android.com/google/play/requirements/target-sdk "Android Developers: Target API level requirement"
[2]: https://support.google.com/googleplay/android-developer/answer/10158779?hl=en "Google Play Help: Broad package visibility permission"
[3]: https://support.google.com/googleplay/android-developer/answer/10787469?hl=en-GB "Google Play Help: Data safety section"
[4]: https://support.google.com/googleplay/android-developer/answer/9866151?hl=en "Play Console Help: Preview assets"
[5]: https://developer.android.com/guide/app-bundle "Android Developers: Android App Bundle"
[6]: https://developer.android.com/develop/background-work/services/alarms "Android Developers: Schedule alarms"
[7]: https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW "Android Developers: SYSTEM_ALERT_WINDOW"
[8]: https://support.google.com/googleplay/android-developer/answer/9857753 "Google Play Help: Ads"
