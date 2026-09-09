---
name: device-testing
description: Plan and run mobile tests across representative devices, OS versions, lifecycle transitions, networks, permissions, upgrades, and hardware constraints.
---

# Device Testing

Build a risk-based matrix rather than attempting every device combination.

## Matrix

Include the minimum/maximum supported OS, common current OS, small and large screens, constrained memory/CPU, relevant hardware, locale/RTL, accessibility settings, and clean install versus upgrade.

## Scenarios

- Startup, background/foreground, process death, state restoration, rotation/resizing, and interruption.
- Offline, slow, lossy, captive, and changing networks; timeout, retry, and duplicate-action behavior.
- Permission granted, denied, restricted, revoked, and changed in settings.
- Authentication expiry, deep links, notifications, file/media access, camera/location, and purchases where applicable.
- Battery, storage, thermal, memory, crash, and responsiveness signals.

Record device/OS/build, setup, exact steps, expected/actual behavior, logs, screenshots when useful, and reproducibility. Distinguish simulator/emulator evidence from physical-device verification.
