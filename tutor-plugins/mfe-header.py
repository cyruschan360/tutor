from tutor import hooks
from tutormfe.hooks import MFE_APPS

@MFE_APPS.add()
def _add_learning_mfe(mfes):
    mfes["learning"] = {
        "repository": "https://github.com/cyruschan360/frontend-app-learning.git",
        "port": 2000,
        "version": "master", # optional, will default to the Open edX current tag.
    }
    return mfes

@MFE_APPS.add()
def _add_authn_mfe(mfes):
    mfes["authn"] = {
        "repository": "https://github.com/cyruschan360/frontend-app-authn.git",
        "port": 1999,
        "version": "master", # optional, will default to the Open edX current tag.
    }
    return mfes
