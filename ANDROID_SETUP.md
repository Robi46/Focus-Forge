# FocusForge: Android Focus Protection and APK Installation

## What FocusForge Can and Cannot Enforce

FocusForge maintains the study timer, its study/rest rhythm, and its local cues. Android deliberately reserves system-wide blocking, call policy, notification policy, and app switching to the device owner and Android system settings. A regular installed app therefore cannot automatically prevent Home/Recents, selectively open WhatsApp or Messenger only for emergencies, or rewrite your call exceptions.

| Goal | Use this Android control | Important trade-off |
| --- | --- | --- |
| Silence distracting notifications while retaining emergency contacts | **Do Not Disturb / a custom Mode** | You can still leave FocusForge to read allowed WhatsApp or Messenger notifications. |
| Keep FocusForge on screen and resist Home/Recents | **Screen Pinning / App pinning** | You cannot normally leave to read WhatsApp or Messenger. Unpin deliberately when needed. |
| Let the display turn off while studying | Turn **Keep display awake** off in FocusForge | Use the installed APK, not Expo Go, for Android background cue behavior. |

> **Recommended balance:** Use **Do Not Disturb without Screen Pinning** if you truly need to open emergency WhatsApp or Messenger messages. Use **Do Not Disturb plus Screen Pinning** only when stopping app switching matters more than accessing those messages during the session.

## Configure Emergency Exceptions

Android Modes and Do Not Disturb can silence interruptions and control who or what may interrupt you. The exact names differ by Android manufacturer and version. Google documents that Modes/Do Not Disturb can be opened from Quick Settings and configured with interruption settings.[1]

1. In **FocusForge → Focus Shield**, select **Allowed interruptions**.
2. Select the supplied emergency labels or type your own, such as Phone, WhatsApp, or Messenger. The private list is a planning checklist; it does not scan your installed apps or alter Android settings automatically.
3. Open your Android settings, then search for **Do Not Disturb** or **DND**. On an Infinix Hot 10 this is commonly under **Sound** or **Sound & vibration**; it can also appear in the Quick Settings tiles.
4. Create a custom mode named **Study** or edit Do Not Disturb.
5. Under **People**, allow calls and messages from the contacts you personally consider emergency contacts. Enable repeat callers only if you want that rule.
6. Under **Apps**, allow the same selected apps where your phone exposes the option. On some Android phones this permits notification alerts only; it does not guarantee a separate call-routing rule for WhatsApp or Messenger.
7. Block other app notifications and visual pop-ups. Keep alarms or safety alerts enabled if you want them.
8. Add the Study mode to Quick Settings for a one-tap start before FocusForge.

> **Selection and enforcement boundary:** the current Play-safe build does **not** scan the phone’s installed apps and does not switch Android into DND automatically. Android keeps ownership of exact people and app exceptions. The FocusForge list is therefore a private setup checklist, not a way to silently rewrite WhatsApp, Messenger, call, or per-app notification exceptions.

## Optional: Pin FocusForge to the Screen

Screen Pinning is Android’s user-managed feature for keeping one app in front. Google’s Android instructions place it under a security setting named **App pinning** on many devices.[2]

1. Open **Settings** and search for **App pinning** or **Screen pinning**.
2. Turn on **Use app pinning** and turn on the option that requires your PIN, pattern, or password to unpin.
3. Turn on your Study Do Not Disturb mode.
4. Start a FocusForge session, then open Android **Recents**.
5. Tap the FocusForge app icon and select **Pin** or **Pin this app**.
6. When the study session is over, use your phone’s unpin gesture and authenticate.

**Do not use Screen Pinning if you must be able to open WhatsApp or Messenger during a session.** Pinning is intended to stop leaving the app; Do Not Disturb is the appropriate control for selective emergency notifications.

## Optional: Floating Session Bubble

The floating bubble is a compact Android overlay for an active, unpaused study session. It is not shown on the Android lock screen; it appears after you leave FocusForge for another app and gives a small live round/rest counter without occupying a large part of the display.

1. Install a **fresh APK** containing the bubble feature. Expo Go and browser preview cannot provide it.
2. In **FocusForge → Settings**, turn on **Floating session bubble**.
3. Read the in-app explanation and tap **Open Android settings**. Android opens a page named **Display over other apps**, **Appear on top**, or similar. Find FocusForge and allow it.
4. Return to FocusForge. It confirms that the bubble is ready. If Android did not grant permission, the app leaves the feature off and you can try again later.
5. Start an unpaused session, then leave FocusForge for another app. The compact bubble should show the current round or rest countdown.
6. Tap the **arrow** in the bubble to return to the Focus dashboard. Tap **×** to remove only the bubble; it does not pause or end the session. Turn the Settings switch off at any time to prevent future bubbles.

> **Permission boundary:** Display over other apps is a user-controlled Android special permission. FocusForge requests it only for this visible active-session control. Do not enable it if you do not want the optional bubble.

## Build and Install the APK

### Create the Android build

1. Open the latest FocusForge project version in the management panel.
2. Select **Publish**. The platform will build the Android package; wait for the completed APK download option.
3. Download the APK to your computer or directly to your phone.

### Install by USB file transfer

1. Connect your Android phone to the computer using a USB cable.
2. On the phone, choose **File transfer** or **Android Auto/File Transfer** from the USB notification.
3. Copy the downloaded FocusForge APK into the phone’s **Downloads** folder.
4. On the phone, open **Files** or **My Files**, open the APK, and select **Install**.
5. If Android blocks the installation, select **Settings** when prompted and allow your Files app to install unknown apps. Then return and install the APK.

### Install by file transfer without a cable

Transfer the APK to your own phone using a private method such as Google Drive, Quick Share, Bluetooth, or your own USB storage. Open it from the Android Files app and follow the same installation steps above.

### Optional: Install from a computer using ADB

If you already use Android Platform Tools, enable **Developer options → USB debugging**, connect the phone, accept the computer’s fingerprint prompt, then run:

```bash
adb install -r FocusForge.apk
```

This is optional. File transfer is simpler and does not require USB debugging.

## First-Run Checklist

1. Open FocusForge and go to **Settings**.
2. Enable **Audible study cues** and tap **Test loud beep**.
3. Allow notifications when Android asks.
4. Turn **Keep display awake** off if you want the display to lock normally.
5. Configure your Android Study Do Not Disturb mode.
6. In **Focus Shield → Allowed interruptions**, record your emergency apps, then match them manually in the Android Study mode.
7. Build and install a **fresh APK** after native/configuration changes. In **FocusForge → Settings**, choose Classic, Bright, or Calm under **Locked-screen cue sound**. The installed version creates the matching v4 FocusForge channels; Expo Go and browser preview cannot verify this locked-screen behavior. If Settings says **Background beeps need the newest Android build**, or the dashboard shows an Ads native-module red screen, you are still using Expo Go or an older APK—close it and install the new APK before testing again.
8. In **FocusForge → Settings → Locked-screen Cue Check**, tap **Check**, then tap **Test with screen locked** and lock the display immediately. This test schedules a real Android notification 15 seconds later.
9. If the test is silent, open **Android Settings → Apps → FocusForge → Notifications**. Confirm that the selected **FocusForge [sound] round beeps** and **FocusForge [sound] rest beeps** channels both allow sound and, where the phone exposes it, allow the channels to **override / bypass Do Not Disturb**.
10. On an Infinix Hot 10, open **Android Settings → Apps → FocusForge → Battery** and select the least restrictive option available, such as **No restrictions** or **Don’t optimize**. Turn off Power Marathon/Ultra Power mode for the test. Android power saving can defer alarms while the display is off.[3]
11. Start a session, lock the screen, and leave the session running. Android should queue one sound at the end of rounds 1–3, three sounds at the round-4 rest boundary, and one sound when the rest ends and round 1 restarts. Do not end or pause the session.
12. If you want a compact timer after leaving FocusForge, enable **Floating session bubble** in Settings, then grant **Display over other apps** from Focus Shield. Turn it off in Settings at any time to prevent future bubbles.
13. If you want strict app-exit resistance, pin FocusForge after starting.

## References

[1]: https://support.google.com/android/answer/9069335?hl=en "Google Android Help: Limit interruptions with Modes & Do Not Disturb"
[2]: https://support.google.com/android/answer/9455138?hl=en "Google Android Help: Pin & unpin screens"
[3]: https://developer.android.com/training/monitoring-device-state/doze-standby "Android Developers: Optimize for Doze and App Standby"
