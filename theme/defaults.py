from mezzanine.conf import register_setting

from django.utils.translation import ugettext_lazy as _

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("Sequence of setting names available within templates."),
    editable=False,
    append=True,
    default=("SOCIAL_LINK_FACEBOOK", "SOCIAL_LINK_LINKEDIN", "SOCIAL_LINK_TWITTER", 
        "SOCIAL_LINK_SOUNDCLOUD", "SOCIAL_LINK_YOUTUBE", "SOCIAL_LINK_GITHUB",),
)

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the footer."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_LINKEDIN",
    label=_("LinkedIn link"),
    description=_("If present a LinkedIn icon linking here will be in the footer."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label="Twitter link",
    description="If present a Twitter icon linking here will be in the footer.",
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_SOUNDCLOUD",
    label="SoundCloud link",
    description="If present a SoundCloud icon linking here will be in the footer.",
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_YOUTUBE",
    label="YouTube link",
    description="If present a YouTube icon linking here will be in the footer.",
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_GITHUB",
    label="GitHub link",
    description="If present a GitHub icon linking here will be in the footer.",
    editable=True,
    default="",
)

