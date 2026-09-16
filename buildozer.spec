[app]
title = Booster-3
package.name = booster3
package.domain = com.booster3.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.permissions = INTERNET
p4a.branch = master
