from tutor import hooks
hooks.Filters.ENV_PATCHES.add_item( 
  ( 
    "common-env-features", 
    """
ADVANCED_SECURITY: true
ALLOW_AUTOMATED_SIGNUPS: true
ALLOW_COURSE_STAFF_GRADE_DOWNLOADS: true
ALLOW_EMAIL_ADDRESS_CHANGE: true
ALLOW_HIDING_DISCUSSION_TAB: true
ALLOW_PUBLIC_ACCOUNT_CREATION: true
AUTH_USE_CAS: true
BATCH_ENROLLMENT_NOTIFY_USERS_DEFAULT: false
COURSES_ARE_BROWSABLE: false
COURSES_INVITE_ONLY: true
DEFAULT_MOBILE_AVAILABLE: true
DISABLE_COURSE_CREATION: true
DISABLE_LOGIN_BUTTON: false
DISABLE_UNENROLLMENT: false
ENABLE_ACCOUNT_DELETION: true
ENABLE_BULK_ENROLLMENT_VIEW: true
ENABLE_BULK_USER_RETIREMENT: true
ENABLE_CHANGE_USER_PASSWORD_ADMIN: true
ENABLE_COURSE_ASSESSMENT_GRADE_CHANGE_SIGNAL: true
ENABLE_CORS_HEADERS: true
ENABLE_CROSS_DOMAIN_CSRF_COOKIE: true
ENABLE_DISCUSSION_HOME_PANEL: true
ENABLE_DISCUSSION_SERVICE: true
ENABLE_GRADE_DOWNLOADS: true
ENABLE_HELP_LINK: false
ENABLE_LTI_PROVIDER: true
ENABLE_NEW_BULK_EMAIL_EXPERIENCE: true
ENABLE_OAUTH2_PROVIDER: true
ENABLE_PREREQUISITE_COURSES: true
ENABLE_REQUIRE_THIRD_PARTY_AUTH: false
ENABLE_SPECIAL_EXAMS: true
ENABLE_SYSADMIN_DASHBOARD: false
ENABLE_THIRD_PARTY_AUTH: true
ENABLE_UNICODE_USERNAME: true
ENTRANCE_EXAMS: true
HIDE_DASHBOARD_COURSES_UNTIL_ACTIVATED: false
SHOW_FOOTER_LANGUAGE_SELECTOR: false
SHOW_REGISTRATION_LINKS: true
SKIP_EMAIL_VALIDATION: true
"""
  )
)

hooks.Filters.ENV_PATCHES.add_item(
  (
    "lms-env",
    """
CORS_ORIGIN_WHITELIST: [
    "learn.jcecc.hk",
    "studio.learn.jcecc.hk",
    "notes.learn.jcecc.hk",
    "learn-v2.jcecc.hk",
    "studio.learn-v2.jcecc.hk",
    "apps.learn-v2.jcecc.hk",
    "notes.learn-v2.jcecc.hk",
    "data.learn-v2.jcecc.hk",
    "xqueue.learn-v2.jcecc.hk",
    "preview.learn-v2.jcecc.hk",
    "foss.hku.hk",
    "nfs1.talic.hku.hk"
]
CROSS_DOMAIN_CSRF_COOKIE_DOMAIN: ".jcecc.hk"
CROSS_DOMAIN_CSRF_COOKIE_NAME: "jcecc"
CSRF_COOKIE_SECURE: false
CORS_ORIGIN_ALLOW_ALL: true
LANGUAGE_COOKIE_NAME: "jcecc-lang"
LOGIN_REDIRECT_WHITELIST: [
    "learn.jcecc.hk",
    "studio.learn.jcecc.hk",
    "notes.learn.jcecc.hk",
    "learn-v2.jcecc.hk",
    "studio.learn-v2.jcecc.hk",
    "apps.learn-v2.jcecc.hk",
    "notes.learn-v2.jcecc.hk",
    "data.learn-v2.jcecc.hk",
    "xqueue.learn-v2.jcecc.hk",
    "preview.learn-v2.jcecc.hk",
    "foss.hku.hk",
    "nfs1.talic.hku.hk"
]
THIRD_PARTY_AUTH_ONLY_DOMAIN: [
    "learn.jcecc.hk",
    "studio.learn.jcecc.hk",
    "notes.learn.jcecc.hk",
    "learn-v2.jcecc.hk",
    "studio.learn-v2.jcecc.hk",
    "apps.learn-v2.jcecc.hk",
    "notes.learn-v2.jcecc.hk",
    "data.learn-v2.jcecc.hk",
    "xqueue.learn-v2.jcecc.hk",
    "preview.learn-v2.jcecc.hk",
    "foss.hku.hk",
    "nfs1.talic.hku.hk"
]
SESSION_COOKIE_DOMAIN: ".jcecc.hk"
SESSION_COOKIE_SECURE: false
TIME_ZONE: "Asia/Hong_Kong"
CAS_IGNORE_REFERER: True
CAS_REDIRECT_URL: "https://learn-v2.jcecc.hk/dashboard"
CAS_SERVER_URL: "https://learn-v2.jcecc.hk/cas/login"
CAS_VERSION: "2"
CAS_APPLY_ATTRIBUTES_TO_USER: true
CAS_LOGO_URL: "https://learn.jcecc.hk/static/images/logo.10c657faf969.png"
CAS_COMPONENT_URLS: {
    "bootstrap3_css": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
    "bootstrap3_js": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js",
    "html5shiv": "//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js",
    "respond": "//oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js",
    "bootstrap4_css": "//stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css",
    "bootstrap4_js": "//stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js",
    "jquery": "//code.jquery.com/jquery.min.js"
}
CAS_SHOW_POWERED: false
CAS_SHOW_SERVICE_MESSAGES: false
CAS_NEW_VERSION_HTML_WARNING: false
CAS_NEW_VERSION_EMAIL_WARNING: false
RATELIMIT_ENABLE: false
REGISTRATION_RATELIMIT: "10000/1d"
REGISTRATION_VALIDATION_RATELIMIT: "10000/1d"
USERNAME_REGEX_PARTIAL: '[\w._+-@]+'
WIKI_ENABLED: false
"""
  )
)

hooks.Filters.ENV_PATCHES.add_item(
  (
    "cms-env",
    """
CORS_ORIGIN_WHITELIST: [
    "learn.jcecc.hk",
    "studio.learn.jcecc.hk",
    "notes.learn.jcecc.hk",
    "learn-v2.jcecc.hk",
    "studio.learn-v2.jcecc.hk",
    "apps.learn-v2.jcecc.hk",
    "notes.learn-v2.jcecc.hk",
    "data.learn-v2.jcecc.hk",
    "xqueue.learn-v2.jcecc.hk",
    "preview.learn-v2.jcecc.hk",
    "foss.hku.hk",
    "nfs1.talic.hku.hk"
]
CROSS_DOMAIN_CSRF_COOKIE_DOMAIN: ".jcecc.hk"
CROSS_DOMAIN_CSRF_COOKIE_NAME: "jcecc"
CSRF_COOKIE_SECURE: false
CORS_ORIGIN_ALLOW_ALL: true
LOGIN_REDIRECT_WHITELIST: [
    "learn.jcecc.hk",
    "studio.learn.jcecc.hk",
    "notes.learn.jcecc.hk",
    "learn-v2.jcecc.hk",
    "studio.learn-v2.jcecc.hk",
    "apps.learn-v2.jcecc.hk",
    "notes.learn-v2.jcecc.hk",
    "data.learn-v2.jcecc.hk",
    "xqueue.learn-v2.jcecc.hk",
    "preview.learn-v2.jcecc.hk",
    "foss.hku.hk",
    "nfs1.talic.hku.hk"
]
THIRD_PARTY_AUTH_ONLY_DOMAIN: [
    "learn.jcecc.hk",
    "studio.learn.jcecc.hk",
    "notes.learn.jcecc.hk",
    "learn-v2.jcecc.hk",
    "studio.learn-v2.jcecc.hk",
    "apps.learn-v2.jcecc.hk",
    "notes.learn-v2.jcecc.hk",
    "data.learn-v2.jcecc.hk",
    "xqueue.learn-v2.jcecc.hk",
    "preview.learn-v2.jcecc.hk",
    "foss.hku.hk",
    "nfs1.talic.hku.hk"
]
SESSION_COOKIE_DOMAIN: ".jcecc.hk"
SESSION_COOKIE_SECURE: false
SESSION_COOKIE_NAME: "studio_session_id"
TIME_ZONE: "Asia/Hong_Kong"
CAS_SERVER_URL: "https://learn-v2.jcecc.hk/cas/login"
CAS_VERSION: "2"
CAS_APPLY_ATTRIBUTES_TO_USER: true
CAS_LOGO_URL: "https://learn.jcecc.hk/static/images/logo.10c657faf969.png"
CAS_COMPONENT_URLS: {
    "bootstrap3_css": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
    "bootstrap3_js": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js",
    "html5shiv": "//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js",
    "respond": "//oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js",
    "bootstrap4_css": "//stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css",
    "bootstrap4_js": "//stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js",
    "jquery": "//code.jquery.com/jquery.min.js"
}
CAS_SHOW_POWERED: false
CAS_SHOW_SERVICE_MESSAGES: false
CAS_NEW_VERSION_HTML_WARNING: false
CAS_NEW_VERSION_EMAIL_WARNING: false
JWT_IN_COOKIE_EXPIRATION: 86400
OAUTH_ID_TOKEN_EXPIRATION: 86400
RATELIMIT_ENABLE: false
REGISTRATION_RATELIMIT: "10000/1d"
REGISTRATION_VALIDATION_RATELIMIT: "10000/1d"
USERNAME_REGEX_PARTIAL: '[\w._+-@]+'
WIKI_ENABLED: false
"""
  )
)

hooks.Filters.ENV_PATCHES.add_item(
  (
    "openedx-lms-production-settings",
     'CORS_ORIGIN_WHITELIST.append("https://learn-v2.jcecc.hk")'
  ),
)

hooks.Filters.ENV_PATCHES.add_item(
  (
    "openedx-lms-production-settings",
     'CORS_ORIGIN_WHITELIST.append("https://studio.learn-v2.jcecc.hk")'
  ),
)
