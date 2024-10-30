from tutor import hooks

hooks.Filters.CONFIG_DEFAULTS.add_item(
    ("JCECC_PLATFORM_IS_PUBLIC", False)
)

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        "FEATURES['ALLOW_PUBLIC_ACCOUNT_CREATION'] = {% if JCECC_PLATFORM_IS_PUBLIC %}True{% else %}False{% endif %}",
    )
)
