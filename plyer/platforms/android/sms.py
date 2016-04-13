'''
Android SMS
-----------
'''

from jnius import autoclass
from plyer.facades import Sms
from . import activity

SmsManager = autoclass('android.telephony.SmsManager')
Intent = autoclass('android.content.Intent')

class AndroidSms(Sms):

    def _send(self, **kwargs):
        sms = SmsManager.getDefault()

        recipient = kwargs.get('recipient')
        message = kwargs.get('message')

        if sms:
            sms.sendTextMessage(recipient, None, message, None, None)

    def _edit(self, **kwargs):
        intent = Intent(Intent.ACTION_VIEW)
        intent.setType("vnd.android-dir/mms-sms")
        if 'recipient' in kwargs:
            intent.putExtra("address", str(kwargs.get('recipient')))

        if 'message' in kwargs:
            intent.putExtra("sms_body", str(kwargs.get('message')))

        activity.startActivity(intent)


def instance():
    return AndroidSms()
