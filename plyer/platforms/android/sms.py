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
        recipient = kwargs.get('recipient')
        address = recipient or ""
        message = kwargs.get('message')
        sms_body = message or ""
        intent.putExtra("address", str(address))
        intent.putExtra("sms_body", str(sms_body))
        activity.startActivity(intent)


def instance():
    return AndroidSms()
