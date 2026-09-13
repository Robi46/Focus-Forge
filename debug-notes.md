# Stability Repair Notes

The initial Focus screen could remain on “Preparing your focus space…” because provider startup awaited storage and notification calls without a recovery path. Startup now renders immediately, validates restored local data, and completes hydration safely even if an optional platform service fails.

The preview service was repeatedly OOM-killed while bundling because the template launched both an unused server process and Metro, while web also loaded the native notification module. FocusForge now starts Metro only, has a web notification shim, and avoids the unused data-client runtime.

The browser did not show the system Alert used for ending a session. The app now uses an in-app confirmation sheet that is available on Android, iOS, and web.

Final live regression: the Focus dashboard rendered after startup; start, pause, resume, end confirmation, confirmed end, history navigation, and local session persistence all completed successfully in the browser preview.
