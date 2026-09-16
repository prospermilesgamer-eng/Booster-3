[app]
title = Boost Max Rocket
package.name = boostmaxrocket
package.domain = com.ug.booster
source.dir =.
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3==3.10.12,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.permissions = INTERNET
p4a.bootstrap = sdl2
