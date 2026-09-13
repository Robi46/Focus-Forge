# FocusForge: Local Android Build Debugging

This project now has two explicit EAS Android build profiles in `eas.json`: `preview` creates an installable APK, and `production` creates an Android App Bundle (AAB) for Google Play. The profiles do not alter the FocusForge timer, local data, growth worlds, or Android permissions.

## What the local audit found

| Check | Result |
|---|---|
| Expo SDK dependencies | Up to date for SDK 54 |
| Managed app configuration | Resolves successfully |
| Forced Android API overrides | None present |
| Generated Gradle Wrapper | 8.14.3 |
| Minimum Android SDK | 24 |
| Google Mobile Ads package | 16.5.0 installed |
| Managed Android prebuild | Succeeds |

The cloud alert does not expose the failing Gradle line, so it cannot identify a further safe source change. A local build will print the full Gradle output to your terminal and save it to a file.

## Before you start

Use a Linux or macOS computer. Expo documents Windows local builds through WSL as possible, but not officially supported. Install Node.js, pnpm, Android Studio, an Android SDK and NDK, plus a JDK. EAS local builds require you to supply the Android SDK/NDK locally. [1]

Download the project source, open a terminal in its folder, and run:

```sh
pnpm install
npx eas-cli@latest login
```

If EAS says the project is not linked to your Expo account, run `npx eas-cli@latest build:configure` once and follow its prompts. This can create or update EAS account linkage; do not run it if EAS already recognizes the project.

## Run the exact local EAS-style APK build

This command uses the `preview` profile, retains the temporary EAS working directory, writes an APK to `eas-artifacts`, and saves everything printed by the build to `eas-local-build.log`.

```sh
mkdir -p eas-artifacts eas-local-work
EAS_LOCAL_BUILD_SKIP_CLEANUP=1 \
EAS_LOCAL_BUILD_WORKINGDIR="$PWD/eas-local-work" \
npx eas-cli@latest build --platform android --profile preview --local --clear-cache \
  --output "$PWD/eas-artifacts/focusforge.apk" 2>&1 | tee eas-local-build.log
```

After a failure, open `eas-local-build.log` and search for the first `FAILURE:`, `What went wrong:`, `Execution failed`, or `Caused by:` line. The EAS local-build guide documents the `--local` command plus the working-directory and cleanup variables used above. [1]

## Get a direct Gradle stack trace

If the EAS-style local build still does not make the cause clear, create the Android project locally and invoke Gradle with its detailed error flags:

```sh
npx expo prebuild --platform android --clean
cd android
./gradlew assembleRelease --stacktrace --info --no-daemon 2>&1 | tee ../gradle-stacktrace.log
cd ..
```

The first `FAILURE:` section in `gradle-stacktrace.log`, with the preceding 30–60 lines, is the information needed to diagnose the next app-side fix. If this is a managed Expo project, do not commit the generated `android/` folder unless you intentionally switch to a native-project workflow.

## Windows: recommended PowerShell route

For a Windows computer, use the direct Gradle route first. It does not depend on an EAS local container, and it writes the full native build output to one file. Install Android Studio, then use its SDK Manager to install an Android SDK, Android SDK Build-Tools, Android SDK Command-line Tools, and the NDK. Use a JDK that Android Studio supports; the standard Android Studio JBR location is used below. [3]

Open **PowerShell** in the downloaded FocusForge project folder and run the following commands. Replace `C:\Program Files\Android\Android Studio\jbr` only if Android Studio is installed in a different location.

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
$env:ANDROID_HOME = "$env:LOCALAPPDATA\Android\Sdk"
$env:ANDROID_SDK_ROOT = $env:ANDROID_HOME
$env:Path = "$env:JAVA_HOME\bin;$env:ANDROID_HOME\platform-tools;$env:Path"

pnpm install
npx expo-doctor
npx expo prebuild --platform android --clean

Set-Location android
.\gradlew.bat assembleRelease --stacktrace --info --no-daemon 2>&1 |
  Tee-Object -FilePath ..\gradle-stacktrace.log
Set-Location ..
```

When it stops, open `gradle-stacktrace.log` in Notepad and find the first `FAILURE:` line. The most useful evidence is the first `* What went wrong:` section and the nearby `Caused by:` lines. To make a debug APK instead, replace `assembleRelease` with `assembleDebug`.

### If `npx expo-doctor` stops while reading `app.config.ts`

Expo Doctor first runs Expo's configuration command. If it only says that `expo config --json --full` exited with code 1, first run Expo's smaller public-config command directly with Expo debug output enabled. This avoids a large JSON file obscuring the error and writes the terminal output to `expo-config-error.log`.

```powershell
$env:EXPO_DEBUG = "1"
npx expo config --type public 2>&1 |
  Tee-Object -FilePath .\expo-config-error.log
Remove-Item Env:EXPO_DEBUG -ErrorAction SilentlyContinue

Select-String -Path .\expo-config-error.log `
  -Pattern "Error|ERROR|TypeError|ReferenceError|SyntaxError|Cannot|Failed|app\.config" `
  -Context 6,16
```

If the command fails, send the output printed by `Select-String`. If it finds no matching line, run `Get-Content .\expo-config-error.log -TotalCount 120` and send that output instead. Do not change `app.config.ts`, `eas.json`, or package versions based only on Expo Doctor's short summary.

## Windows: EAS local build through WSL

Expo allows local EAS builds through WSL, but documents Windows/WSL as not officially supported. Use this only after the PowerShell Gradle command above, because it adds another layer to diagnose. [1]

First install Ubuntu WSL from an **Administrator PowerShell** window, reboot if asked, then open the Ubuntu application:

```powershell
wsl --install -d Ubuntu
```

Inside the Ubuntu terminal, ensure that the Android SDK/NDK and Java are available in the Linux environment. Then open the project through its Windows-mounted path and run the EAS build. Replace `<WindowsUser>` with your Windows user folder name.

```bash
cd /mnt/c/Users/<WindowsUser>/Downloads/focusforge-study-timer
pnpm install
npx eas-cli@latest login
mkdir -p eas-artifacts eas-local-work

EAS_LOCAL_BUILD_SKIP_CLEANUP=1 \
EAS_LOCAL_BUILD_WORKINGDIR="$PWD/eas-local-work" \
npx eas-cli@latest build --platform android --profile preview --local --clear-cache \
  --output "$PWD/eas-artifacts/focusforge.apk" 2>&1 | tee eas-local-build.log
```

Open `eas-local-build.log` in Windows Explorer from the project folder. The preserved `eas-local-work` directory is also useful if EAS reports another error. Do not share keystore passwords, `EXPO_TOKEN`, or private signing files when sending the log.

## Check or change EAS profiles

Open `eas.json` in the project root. Use `preview` for a personal-installable APK and `production` for the Play Store AAB:

```sh
npx eas-cli@latest build --platform android --profile preview --local
npx eas-cli@latest build --platform android --profile production
```

Do not add `compileSdkVersion`, `targetSdkVersion`, or arbitrary Gradle versions to `app.config.ts` merely to retry a build. FocusForge relies on Expo SDK 54’s managed Android toolchain. The prior forced Android API overrides were already removed because they could conflict with the native dependency set.

## References

[1]: https://docs.expo.dev/build-reference/local-builds/ "Expo: Run EAS Build locally"
[2]: https://docs.expo.dev/build/eas-json/ "Expo: Configure EAS Build with eas.json"
[3]: https://docs.expo.dev/guides/local-app-production/ "Expo: Create a release build locally"
