#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################
### Extracted from platform version: 2.3.2
#################################################
AOSP_PERMISSIONS = {
    'android.permission.BIND_WALLPAPER': {
        'permissionGroup': '',
        'description':
        'Allows the holder to bind to the top-level interface of a wallpaper. Should never be needed for normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'bind to a wallpaper'
    },
    'android.permission.FORCE_BACK': {
        'permissionGroup': '',
        'description':
        'Allows an application to force any activity that is in the foreground to close and go back. Should never be needed for normal applications.',
        'protectionLevel': 'signature',
        'label': 'force application to close'
    },
    'android.permission.READ_CALENDAR': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to read all of the calendar events stored on your phone. Malicious applications can use this to send your calendar events to other people.',
        'protectionLevel': 'dangerous',
        'label': 'read calendar events'
    },
    'android.permission.READ_FRAME_BUFFER': {
        'permissionGroup': '',
        'description':
        'Allows application to read the content of the frame buffer.',
        'protectionLevel': 'signature',
        'label': 'read frame buffer'
    },
    'android.permission.READ_SYNC_STATS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to read the sync stats; e.g., the history of syncs that have occurred.',
        'protectionLevel': 'normal',
        'label': 'read sync statistics'
    },
    'android.permission.SHUTDOWN': {
        'permissionGroup': '',
        'description':
        'Puts the activity manager into a shutdown state. Does not perform a complete shutdown.',
        'protectionLevel': 'signature',
        'label': 'partial shutdown'
    },
    'android.permission.ACCESS_NETWORK_STATE': {
        'permissionGroup': 'android.permission-group.NETWORK',
        'description':
        'Allows an application to view the state of all networks.',
        'protectionLevel': 'normal',
        'label': 'view network state'
    },
    'android.permission.INTERNET': {
        'permissionGroup': 'android.permission-group.NETWORK',
        'description': 'Allows an application to create network sockets.',
        'protectionLevel': 'dangerous',
        'label': 'full Internet access'
    },
    'android.permission.CHANGE_CONFIGURATION': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to change the current configuration, such as the locale or overall font size.',
        'protectionLevel': 'dangerous',
        'label': 'change your UI settings'
    },
    'android.permission.READ_CONTACTS': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to read all of the contact (address) data stored on your phone. Malicious applications can use this to send your data to other people.',
        'protectionLevel': 'dangerous',
        'label': 'read contact data'
    },
    'android.permission.HARDWARE_TEST': {
        'permissionGroup': 'android.permission-group.HARDWARE_CONTROLS',
        'description':
        'Allows the application to control various peripherals for the purpose of hardware testing.',
        'protectionLevel': 'signature',
        'label': 'test hardware'
    },
    'android.permission.ACCESS_DOWNLOAD_MANAGER_ADVANCED': {
        'permissionGroup': '',
        'description':
        'Allows the application to access the download manager\'s advanced functions. Malicious applications can use this to disrupt downloads and access private information.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'Advanced download manager functions.'
    },
    'com.android.launcher.permission.INSTALL_SHORTCUT': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to add shortcuts without user intervention.',
        'protectionLevel': 'normal',
        'label': 'install shortcuts'
    },
    'android.permission.CHANGE_WIFI_MULTICAST_STATE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to receive packets not directly addressed to your device. This can be useful when discovering services offered near by. It uses more power than the non-multicast mode.',
        'protectionLevel': 'dangerous',
        'label': 'allow Wi-Fi Multicast reception'
    },
    'android.permission.VIBRATE': {
        'permissionGroup': 'android.permission-group.HARDWARE_CONTROLS',
        'description': 'Allows the application to control the vibrator.',
        'protectionLevel': 'normal',
        'label': 'control vibrator'
    },
    'android.permission.BIND_INPUT_METHOD': {
        'permissionGroup': '',
        'description':
        'Allows the holder to bind to the top-level interface of an input method. Should never be needed for normal applications.',
        'protectionLevel': 'signature',
        'label': 'bind to an input method'
    },
    'android.permission.SET_TIME_ZONE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to change the phone\'s time zone.',
        'protectionLevel': 'dangerous',
        'label': 'set time zone'
    },
    'android.permission.ACCESS_CACHE_FILESYSTEM': {
        'permissionGroup': '',
        'description':
        'Allows an application to read and write the cache filesystem.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'access the cache filesystem'
    },
    'android.permission.DOWNLOAD_CACHE_NON_PURGEABLE': {
        'permissionGroup': '',
        'description':
        'Allows the application to download files to the download cache which cannot be automatically deleted when the download manager needs more space.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'Reserve space in the download cache'
    },
    'android.permission.WRITE_SYNC_SETTINGS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to modify the sync settings, such as whether sync is enabled for Contacts.',
        'protectionLevel': 'dangerous',
        'label': 'write sync settings'
    },
    'android.permission.READ_LOGS': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to read from the system\'s various log files. This allows it to discover general information about what you are doing with the phone, potentially including personal or private information.',
        'protectionLevel': 'dangerous',
        'label': 'read sensitive log data'
    },
    'android.permission.DUMP': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows application to retrieve internal state of the system. Malicious applications may retrieve a wide variety of private and secure information that they should never normally need.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'retrieve system internal state'
    },
    'android.permission.WRITE_GSERVICES': {
        'permissionGroup': '',
        'description':
        'Allows an application to modify the Google services map. Not for use by normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'modify the Google services map'
    },
    'android.permission.INJECT_EVENTS': {
        'permissionGroup': '',
        'description':
        'Allows an application to deliver its own input events (key presses, etc.) to other applications. Malicious applications can use this to take over the phone.',
        'protectionLevel': 'signature',
        'label': 'press keys and control buttons'
    },
    'android.permission.BIND_DEVICE_ADMIN': {
        'permissionGroup': '',
        'description':
        'Allows the holder to send intents to a device administrator. Should never be needed for normal applications.',
        'protectionLevel': 'signature',
        'label': 'interact with a device admin'
    },
    'android.permission.FORCE_STOP_PACKAGES': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to forcibly stop other applications.',
        'protectionLevel': 'signature',
        'label': 'force stop other applications'
    },
    'com.android.frameworks.coretests.permission.TEST_DENIED': {
        'permissionGroup': '',
        'description':
        'Used for running unit tests, for testing operations where we do not have the permission.',
        'protectionLevel': 'normal',
        'label': 'Test Denied'
    },
    'android.permission.WRITE_SECURE_SETTINGS': {
        'permissionGroup': '',
        'description':
        'Allows an application to modify the system\'s secure settings data. Not for use by normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'modify secure system settings'
    },
    'android.permission.UPDATE_DEVICE_STATS': {
        'permissionGroup': '',
        'description':
        'Allows the modification of collected battery statistics. Not for use by normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'modify battery statistics'
    },
    'android.permission.BROADCAST_PACKAGE_REMOVED': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to broadcast a notification that an application package has been removed. Malicious applications may use this to kill any other running application.',
        'protectionLevel': 'signature',
        'label': 'send package removed broadcast'
    },
    'android.permission.SYSTEM_ALERT_WINDOW': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to show system alert windows. Malicious applications can take over the entire screen of the phone.',
        'protectionLevel': 'dangerous',
        'label': 'display system-level alerts'
    },
    'com.android.cts.permissionNotUsedWithSignature': {
        'permissionGroup': '',
        'description': '',
        'protectionLevel': 'signature',
        'label': ''
    },
    'android.permission.ACCESS_LOCATION_EXTRA_COMMANDS': {
        'permissionGroup': 'android.permission-group.LOCATION',
        'description':
        'Access extra location provider commands. Malicious applications could use this to interfere with the operation of the GPS or other location sources.',
        'protectionLevel': 'normal',
        'label': 'access extra location provider commands'
    },
    'android.permission.BRICK': {
        'permissionGroup': '',
        'description':
        'Allows the application to disable the entire phone permanently. This is very dangerous.',
        'protectionLevel': 'signature',
        'label': 'permanently disable phone'
    },
    'com.android.browser.permission.WRITE_HISTORY_BOOKMARKS': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to modify the Browser\'s history or bookmarks stored on your phone. Malicious applications can use this to erase or modify your Browser\'s data.',
        'protectionLevel': 'dangerous',
        'label': 'write Browser\'s history and bookmarks'
    },
    'android.permission.CHANGE_WIFI_STATE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to connect to and disconnect from Wi-Fi access points, and to make changes to configured Wi-Fi networks.',
        'protectionLevel': 'dangerous',
        'label': 'change Wi-Fi state'
    },
    'android.permission.RECORD_AUDIO': {
        'permissionGroup': 'android.permission-group.HARDWARE_CONTROLS',
        'description': 'Allows application to access the audio record path.',
        'protectionLevel': 'dangerous',
        'label': 'record audio'
    },
    'android.permission.MODIFY_PHONE_STATE': {
        'permissionGroup': 'android.permission-group.PHONE_CALLS',
        'description':
        'Allows the application to control the phone features of the device. An application with this permission can switch networks, turn the phone radio on and off and the like without ever notifying you.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'modify phone state'
    },
    'android.permission.ACCOUNT_MANAGER': {
        'permissionGroup': 'android.permission-group.ACCOUNTS',
        'description':
        'Allows an application to make calls to AccountAuthenticators',
        'protectionLevel': 'signature',
        'label': 'act as the AccountManagerService'
    },
    'android.permission.SET_ANIMATION_SCALE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to change the global animation speed (faster or slower animations) at any time.',
        'protectionLevel': 'dangerous',
        'label': 'modify global animation speed'
    },
    'android.permission.SET_PROCESS_LIMIT': {
        'permissionGroup': 'android.permission-group.DEVELOPMENT_TOOLS',
        'description':
        'Allows an application to control the maximum number of processes that will run. Never needed for normal applications.',
        'protectionLevel': 'dangerous',
        'label': 'limit number of running processes'
    },
    'android.permission.SET_PREFERRED_APPLICATIONS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to modify your preferred applications. This can allow malicious applications to silently change the applications that are run, spoofing your existing applications to collect private data from you.',
        'protectionLevel': 'signature',
        'label': 'set preferred applications'
    },
    'com.android.cts.permissionAllowedWithSignature': {
        'permissionGroup': '',
        'description': '',
        'protectionLevel': 'signature',
        'label': ''
    },
    'android.permission.SET_DEBUG_APP': {
        'permissionGroup': 'android.permission-group.DEVELOPMENT_TOOLS',
        'description':
        'Allows an application to turn on debugging for another application. Malicious applications can use this to kill other applications.',
        'protectionLevel': 'dangerous',
        'label': 'enable application debugging'
    },
    'android.permission.INSTALL_DRM': {
        'permissionGroup': '',
        'description': 'Allows application to install DRM-protected content.',
        'protectionLevel': 'normal',
        'label': 'Install DRM content.'
    },
    'android.permission.BLUETOOTH': {
        'permissionGroup': 'android.permission-group.NETWORK',
        'description':
        'Allows an application to view configuration of the local Bluetooth phone, and to make and accept connections with paired devices.',
        'protectionLevel': 'dangerous',
        'label': 'create Bluetooth connections'
    },
    'android.permission.CAMERA': {
        'permissionGroup': 'android.permission-group.HARDWARE_CONTROLS',
        'description':
        'Allows application to take pictures and videos with the camera. This allows the application at any time to collect images the camera is seeing.',
        'protectionLevel': 'dangerous',
        'label': 'take pictures and videos'
    },
    'android.permission.SET_WALLPAPER_HINTS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows the application to set the system wallpaper size hints.',
        'protectionLevel': 'normal',
        'label': 'set wallpaper size hints'
    },
    'android.permission.WAKE_LOCK': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to prevent the phone from going to sleep.',
        'protectionLevel': 'dangerous',
        'label': 'prevent phone from sleeping'
    },
    'android.permission.REBOOT': {
        'permissionGroup': '',
        'description': 'Allows the application to force the phone to reboot.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'force phone reboot'
    },
    'android.permission.BROADCAST_WAP_PUSH': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows an application to broadcast a notification that a WAP PUSH message has been received. Malicious applications may use this to forge MMS message receipt or to silently replace the content of any web page with malicious variants.',
        'protectionLevel': 'signature',
        'label': 'send WAP-PUSH-received broadcast'
    },
    'android.permission.SET_WALLPAPER_COMPONENT': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': '',
        'protectionLevel': 'signatureOrSystem',
        'label': ''
    },
    'android.permission.ACCESS_BLUETOOTH_SHARE': {
        'permissionGroup': '',
        'description':
        'Allows the application to access the BluetoothShare manager and to use it to transfer files.',
        'protectionLevel': 'signature',
        'label': 'Access download manager.'
    },
    'android.intent.category.MASTER_CLEAR.permission.C2D_MESSAGE': {
        'permissionGroup': '',
        'description': '',
        'protectionLevel': 'signature',
        'label': ''
    },
    'android.permission.STATUS_BAR': {
        'permissionGroup': '',
        'description':
        'Allows application to disable the status bar or add and remove system icons.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'disable or modify status bar'
    },
    'android.permission.WRITE_USER_DICTIONARY': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to write new words into the user dictionary.',
        'protectionLevel': 'normal',
        'label': 'write to user defined dictionary'
    },
    'com.android.browser.permission.READ_HISTORY_BOOKMARKS': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows the application to read all the URLs that the Browser has visited, and all of the Browser\'s bookmarks.',
        'protectionLevel': 'dangerous',
        'label': 'read Browser\'s history and bookmarks'
    },
    'android.permission.ACCESS_DRM': {
        'permissionGroup': '',
        'description': 'Allows application to access DRM-protected content.',
        'protectionLevel': 'signature',
        'label': 'Access DRM content.'
    },
    'android.permission.RECEIVE_SMS': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows application to receive and process SMS messages. Malicious applications may monitor your messages or delete them without showing them to you.',
        'protectionLevel': 'dangerous',
        'label': 'receive SMS'
    },
    'android.permission.WRITE_CONTACTS': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to modify the contact (address) data stored on your phone. Malicious applications can use this to erase or modify your contact data.',
        'protectionLevel': 'dangerous',
        'label': 'write contact data'
    },
    'android.permission.CONTROL_LOCATION_UPDATES': {
        'permissionGroup': '',
        'description':
        'Allows enabling/disabling location update notifications from the radio. Not for use by normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'control location update notifications'
    },
    'android.permission.BIND_APPWIDGET': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows the application to tell the system which widgets can be used by which application. With this permission, applications can give access to personal data to other applications. Not for use by normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'choose widgets'
    },
    'com.android.frameworks.coretests.permission.TEST_GRANTED': {
        'permissionGroup': '',
        'description':
        'Used for running unit tests, for testing operations where we have the permission.',
        'protectionLevel': 'normal',
        'label': 'Test Granted'
    },
    'android.permission.SIGNAL_PERSISTENT_PROCESSES': {
        'permissionGroup': 'android.permission-group.DEVELOPMENT_TOOLS',
        'description':
        'Allows application to request that the supplied signal be sent to all persistent processes.',
        'protectionLevel': 'dangerous',
        'label': 'send Linux signals to applications'
    },
    'android.permission.ASEC_CREATE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': 'Allows the application to create internal storage.',
        'protectionLevel': 'signature',
        'label': 'create internal storage'
    },
    'android.permission.INSTALL_LOCATION_PROVIDER': {
        'permissionGroup': '',
        'description':
        'Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real location sources such as GPS or Network providers or monitor and report your location to an external source.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'permission to install a location provider'
    },
    'android.permission.SEND_DOWNLOAD_COMPLETED_INTENTS': {
        'permissionGroup': '',
        'description':
        'Allows the application to send notifications about completed downloads. Malicious applications can use this to confuse other applications that download files.',
        'protectionLevel': 'signature',
        'label': 'Send download notifications.'
    },
    'android.permission.WRITE_SETTINGS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to modify the system\'s settings data. Malicious applications can corrupt your system\'s configuration.',
        'protectionLevel': 'dangerous',
        'label': 'modify global system settings'
    },
    'android.permission.MASTER_CLEAR': {
        'permissionGroup': '',
        'description':
        'Allows an application to completely reset the system to its factory settings, erasing all data, configuration, and installed applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'reset system to factory defaults'
    },
    'android.permission.READ_INPUT_STATE': {
        'permissionGroup': '',
        'description':
        'Allows applications to watch the keys you press even when interacting with another application (such as entering a password). Should never be needed for normal applications.',
        'protectionLevel': 'signature',
        'label': 'record what you type and actions you take'
    },
    'android.permission.MANAGE_APP_TOKENS': {
        'permissionGroup': '',
        'description':
        'Allows applications to create and manage their own tokens, bypassing their normal Z-ordering. Should never be needed for normal applications.',
        'protectionLevel': 'signature',
        'label': 'manage application tokens'
    },
    'com.android.email.permission.ACCESS_PROVIDER': {
        'permissionGroup': '',
        'description':
        'Allows this application to access your Email database, including received messages, sent messages, usernames and passwords.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'Access Email provider data'
    },
    'com.android.frameworks.coretests.DANGEROUS': {
        'permissionGroup': 'android.permission-group.COST_MONEY',
        'description': '',
        'protectionLevel': 'dangerous',
        'label': ''
    },
    'com.android.launcher.permission.WRITE_SETTINGS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to change the settings and shortcuts in Home.',
        'protectionLevel': 'normal',
        'label': 'write Home settings and shortcuts'
    },
    'android.permission.MODIFY_AUDIO_SETTINGS': {
        'permissionGroup': 'android.permission-group.HARDWARE_CONTROLS',
        'description':
        'Allows application to modify global audio settings such as volume and routing.',
        'protectionLevel': 'dangerous',
        'label': 'change your audio settings'
    },
    'android.permission.ASEC_ACCESS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows the application to get information on internal storage.',
        'protectionLevel': 'signature',
        'label': 'get information on internal storage'
    },
    'android.permission.USE_SIP': {
        'permissionGroup': 'android.permission-group.NETWORK',
        'description':
        'Allows an application to use the SIP service to make/receive Internet calls.',
        'protectionLevel': 'dangerous',
        'label': 'make/receive Internet calls'
    },
    'android.permission.CHANGE_NETWORK_STATE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to change the state of network connectivity.',
        'protectionLevel': 'dangerous',
        'label': 'change network connectivity'
    },
    'android.permission.WRITE_APN_SETTINGS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to modify the APN settings, such as Proxy and Port of any APN.',
        'protectionLevel': 'dangerous',
        'label': 'write Access Point Name settings'
    },
    'android.permission.ACCESS_SURFACE_FLINGER': {
        'permissionGroup': '',
        'description':
        'Allows application to use SurfaceFlinger low-level features.',
        'protectionLevel': 'signature',
        'label': 'access SurfaceFlinger'
    },
    'android.permission.MOVE_PACKAGE': {
        'permissionGroup': '',
        'description':
        'Allows an application to move application resources from internal to external media and vice versa.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'Move application resources'
    },
    'android.permission.FACTORY_TEST': {
        'permissionGroup': '',
        'description':
        'Run as a low-level manufacturer test, allowing complete access to the phone hardware. Only available when a phone is running in manufacturer test mode.',
        'protectionLevel': 'signature',
        'label': 'run in factory test mode'
    },
    'android.permission.CHANGE_BACKGROUND_DATA_SETTING': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to change the background data usage setting.',
        'protectionLevel': 'signature',
        'label': 'change background data usage setting'
    },
    'android.permission.PROCESS_OUTGOING_CALLS': {
        'permissionGroup': 'android.permission-group.PHONE_CALLS',
        'description':
        'Allows application to process outgoing calls and change the number to be dialed. Malicious applications may monitor, redirect, or prevent outgoing calls.',
        'protectionLevel': 'dangerous',
        'label': 'intercept outgoing calls'
    },
    'android.permission.CALL_PRIVILEGED': {
        'permissionGroup': '',
        'description':
        'Allows the application to call any phone number, including emergency numbers, without your intervention. Malicious applications may place unnecessary and illegal calls to emergency services.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'directly call any phone numbers'
    },
    'android.permission.WRITE_CALENDAR': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to add or change the events on your calendar, which may send email to guests. Malicious applications can use this to erase or modify your calendar events or to send email to guests.',
        'protectionLevel': 'dangerous',
        'label': 'add or modify calendar events and send email to guests'
    },
    'android.permission.NFC': {
        'permissionGroup': 'android.permission-group.NETWORK',
        'description':
        'Allows an application to communicate with Near Field Communication (NFC) tags, cards, and readers.',
        'protectionLevel': 'dangerous',
        'label': 'control Near Field Communication'
    },
    'android.permission.MANAGE_ACCOUNTS': {
        'permissionGroup': 'android.permission-group.ACCOUNTS',
        'description':
        'Allows an application to perform operations like adding, and removing accounts and deleting their password.',
        'protectionLevel': 'dangerous',
        'label': 'manage the accounts list'
    },
    'android.permission.SEND_SMS': {
        'permissionGroup': 'android.permission-group.COST_MONEY',
        'description':
        'Allows application to send SMS messages. Malicious applications may cost you money by sending messages without your confirmation.',
        'protectionLevel': 'dangerous',
        'label': 'send SMS messages'
    },
    'android.permission.CLEAR_APP_USER_DATA': {
        'permissionGroup': '',
        'description': 'Allows an application to clear user data.',
        'protectionLevel': 'signature',
        'label': 'delete other applications\' data'
    },
    'android.permission.ACCESS_MOCK_LOCATION': {
        'permissionGroup': 'android.permission-group.LOCATION',
        'description':
        'Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real location sources such as GPS or Network providers.',
        'protectionLevel': 'dangerous',
        'label': 'mock location sources for testing'
    },
    'android.permission.PERFORM_CDMA_PROVISIONING': {
        'permissionGroup': '',
        'description':
        'Allows the application to start CDMA provisioning. Malicious applications may unnecessarily start CDMA provisioning',
        'protectionLevel': 'signatureOrSystem',
        'label': 'directly start CDMA phone setup'
    },
    'android.permission.WRITE_SMS': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows application to write to SMS messages stored on your phone or SIM card. Malicious applications may delete your messages.',
        'protectionLevel': 'dangerous',
        'label': 'edit SMS or MMS'
    },
    'android.permission.ACCESS_ALL_DOWNLOADS': {
        'permissionGroup': '',
        'description':
        'Allows the application to view and modify all initiated by any application on the system.',
        'protectionLevel': 'signature',
        'label': 'Access all system downloads'
    },
    'android.permission.DELETE_PACKAGES': {
        'permissionGroup': '',
        'description':
        'Allows an application to delete Android packages. Malicious applications can use this to delete important applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'delete applications'
    },
    'android.permission.COPY_PROTECTED_DATA': {
        'permissionGroup': '',
        'description':
        'Allows to invoke default container service to copy content. Not for use by normal applications.',
        'protectionLevel': 'signature',
        'label':
        'Allows to invoke default container service to copy content. Not for use by normal applications.'
    },
    'android.permission.ACCESS_CHECKIN_PROPERTIES': {
        'permissionGroup': '',
        'description':
        'Allows read/write access to properties uploaded by the checkin service. Not for use by normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'access checkin properties'
    },
    'android.permission.DOWNLOAD_WITHOUT_NOTIFICATION': {
        'permissionGroup': 'android.permission-group.NETWORK',
        'description':
        'Allows the application to download files through the download manager without any notification being shown to the user.',
        'protectionLevel': 'normal',
        'label': 'download files without notification'
    },
    'com.android.email.permission.READ_ATTACHMENT': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows this application to read your Email attachments.',
        'protectionLevel': 'dangerous',
        'label': 'Read Email attachments'
    },
    'android.permission.SET_TIME': {
        'permissionGroup': '',
        'description':
        'Allows an application to change the phone\'s clock time.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'set time'
    },
    'android.permission.BATTERY_STATS': {
        'permissionGroup': '',
        'description':
        'Allows the modification of collected battery statistics. Not for use by normal applications.',
        'protectionLevel': 'normal',
        'label': 'modify battery statistics'
    },
    'android.app.cts.permission.TEST_GRANTED': {
        'permissionGroup': '',
        'description':
        'Used for running CTS tests, for testing operations where we have the permission.',
        'protectionLevel': 'normal',
        'label': 'Test Granted'
    },
    'android.permission.DIAGNOSTIC': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to read and write to any resource owned by the diag group; for example, files in /dev. This could potentially affect system stability and security. This should be ONLY be used for hardware-specific diagnostics by the manufacturer or operator.',
        'protectionLevel': 'signature',
        'label': 'read/write to resources owned by diag'
    },
    'android.permission.CALL_PHONE': {
        'permissionGroup': 'android.permission-group.COST_MONEY',
        'description':
        'Allows the application to call phone numbers without your intervention. Malicious applications may cause unexpected calls on your phone bill. Note that this does not allow the application to call emergency numbers.',
        'protectionLevel': 'dangerous',
        'label': 'directly call phone numbers'
    },
    'android.permission.MOUNT_FORMAT_FILESYSTEMS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': 'Allows the application to format removable storage.',
        'protectionLevel': 'dangerous',
        'label': 'format external storage'
    },
    'android.permission.READ_PHONE_STATE': {
        'permissionGroup': 'android.permission-group.PHONE_CALLS',
        'description':
        'Allows the application to access the phone features of the device. An application with this permission can determine the phone number and serial number of this phone, whether a call is active, the number that call is connected to and the like.',
        'protectionLevel': 'dangerous',
        'label': 'read phone state and identity'
    },
    'android.permission.ACCESS_COARSE_LOCATION': {
        'permissionGroup': 'android.permission-group.LOCATION',
        'description':
        'Access coarse location sources such as the cellular network database to determine an approximate phone location, where available. Malicious applications can use this to determine approximately where you are.',
        'protectionLevel': 'dangerous',
        'label': 'coarse (network-based) location'
    },
    'android.permission.BROADCAST_SMS': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows an application to broadcast a notification that an SMS message has been received. Malicious applications may use this to forge incoming SMS messages.',
        'protectionLevel': 'signature',
        'label': 'send SMS-received broadcast'
    },
    'android.permission.KILL_BACKGROUND_PROCESSES': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to kill background processes of other applications, even if memory isn\'t low.',
        'protectionLevel': 'normal',
        'label': 'kill background processes'
    },
    'android.permission.STOP_APP_SWITCHES': {
        'permissionGroup': '',
        'description':
        'Prevents the user from switching to another application.',
        'protectionLevel': 'signature',
        'label': 'prevent app switches'
    },
    'android.permission.ACCESS_WIFI_STATE': {
        'permissionGroup': 'android.permission-group.NETWORK',
        'description':
        'Allows an application to view the information about the state of Wi-Fi.',
        'protectionLevel': 'normal',
        'label': 'view Wi-Fi state'
    },
    'android.permission.RECEIVE_MMS': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows application to receive and process MMS messages. Malicious applications may monitor your messages or delete them without showing them to you.',
        'protectionLevel': 'dangerous',
        'label': 'receive MMS'
    },
    'android.permission.GLOBAL_SEARCH_CONTROL': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': '',
        'protectionLevel': 'signature',
        'label': ''
    },
    'android.permission.ACCESS_DOWNLOAD_MANAGER': {
        'permissionGroup': '',
        'description':
        'Allows the application to access the download manager and to use it to download files. Malicious applications can use this to disrupt downloads and access private information.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'Access download manager.'
    },
    'android.permission.STATUS_BAR_SERVICE': {
        'permissionGroup': '',
        'description': 'Allows the application to be the status bar.',
        'protectionLevel': 'signature',
        'label': 'status bar'
    },
    'android.permission.DELETE_CACHE_FILES': {
        'permissionGroup': '',
        'description': 'Allows an application to delete cache files.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'delete other applications\' caches'
    },
    'android.permission.RESTART_PACKAGES': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to kill background processes of other applications, even if memory isn\'t low.',
        'protectionLevel': 'normal',
        'label': 'kill background processes'
    },
    'android.permission.GET_ACCOUNTS': {
        'permissionGroup': 'android.permission-group.ACCOUNTS',
        'description':
        'Allows an application to get the list of accounts known by the phone.',
        'protectionLevel': 'normal',
        'label': 'discover known accounts'
    },
    'android.permission.SUBSCRIBED_FEEDS_READ': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to get details about the currently synced feeds.',
        'protectionLevel': 'normal',
        'label': 'read subscribed feeds'
    },
    'android.permission.READ_SYNC_SETTINGS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to read the sync settings, such as whether sync is enabled for Contacts.',
        'protectionLevel': 'normal',
        'label': 'read sync settings'
    },
    'android.permission.DISABLE_KEYGUARD': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to disable the keylock and any associated password security. A legitimate example of this is the phone disabling the keylock when receiving an incoming phone call, then re-enabling the keylock when the call is finished.',
        'protectionLevel': 'dangerous',
        'label': 'disable keylock'
    },
    'com.android.launcher.permission.UNINSTALL_SHORTCUT': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to remove shortcuts without user intervention.',
        'protectionLevel': 'normal',
        'label': 'uninstall shortcuts'
    },
    'android.permission.USE_CREDENTIALS': {
        'permissionGroup': 'android.permission-group.ACCOUNTS',
        'description':
        'Allows an application to request authentication tokens.',
        'protectionLevel': 'dangerous',
        'label': 'use the authentication credentials of an account'
    },
    'android.permission.SUBSCRIBED_FEEDS_WRITE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to modify your currently synced feeds. This could allow a malicious application to change your synced feeds.',
        'protectionLevel': 'dangerous',
        'label': 'write subscribed feeds'
    },
    'android.permission.READ_USER_DICTIONARY': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows an application to read any private words, names and phrases that the user may have stored in the user dictionary.',
        'protectionLevel': 'dangerous',
        'label': 'read user defined dictionary'
    },
    'android.permission.CHANGE_COMPONENT_ENABLED_STATE': {
        'permissionGroup': '',
        'description':
        'Allows an application to change whether a component of another application is enabled or not. Malicious applications can use this to disable important phone capabilities. Care must be used with permission, as it is possible to get application components into an unusable, inconsistent, or unstable state.',
        'protectionLevel': 'signature',
        'label': 'enable or disable application components'
    },
    'android.permission.RECEIVE_BOOT_COMPLETED': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to have itself started as soon as the system has finished booting. This can make it take longer to start the phone and allow the application to slow down the overall phone by always running.',
        'protectionLevel': 'normal',
        'label': 'automatically start at boot'
    },
    'android.permission.BACKUP': {
        'permissionGroup': '',
        'description':
        'Allows the application to control the system\'s backup and restore mechanism. Not for use by normal applications.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'control system backup and restore'
    },
    'android.permission.EXPAND_STATUS_BAR': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows application to expand or collapse the status bar.',
        'protectionLevel': 'normal',
        'label': 'expand/collapse status bar'
    },
    'android.permission.ACCESS_USB': {
        'permissionGroup': 'android.permission-group.HARDWARE_CONTROLS',
        'description': 'Allows the application to access USB devices.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'access USB devices'
    },
    'android.permission.ACCESS_FINE_LOCATION': {
        'permissionGroup': 'android.permission-group.LOCATION',
        'description':
        'Access fine location sources such as the Global Positioning System on the phone, where available. Malicious applications can use this to determine where you are, and may consume additional battery power.',
        'protectionLevel': 'dangerous',
        'label': 'fine (GPS) location'
    },
    'android.permission.ASEC_RENAME': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': 'Allows the application to rename internal storage.',
        'protectionLevel': 'signature',
        'label': 'rename internal storage'
    },
    'android.permission.PERSISTENT_ACTIVITY': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to make parts of itself persistent, so the system can\'t use it for other applications.',
        'protectionLevel': 'dangerous',
        'label': 'make application always run'
    },
    'android.permission.REORDER_TASKS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to move tasks to the foreground and background. Malicious applications can force themselves to the front without your control.',
        'protectionLevel': 'dangerous',
        'label': 'reorder running applications'
    },
    'android.permission.RECEIVE_WAP_PUSH': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows application to receive and process WAP messages. Malicious applications may monitor your messages or delete them without showing them to you.',
        'protectionLevel': 'dangerous',
        'label': 'receive WAP'
    },
    'android.permission.DEVICE_POWER': {
        'permissionGroup': '',
        'description': 'Allows the application to turn the phone on or off.',
        'protectionLevel': 'signature',
        'label': 'power phone on or off'
    },
    'android.permission.SET_WALLPAPER': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': 'Allows the application to set the system wallpaper.',
        'protectionLevel': 'normal',
        'label': 'set wallpaper'
    },
    'android.permission.ASEC_DESTROY': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': 'Allows the application to destroy internal storage.',
        'protectionLevel': 'signature',
        'label': 'destroy internal storage'
    },
    'android.permission.BLUETOOTH_ADMIN': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to configure the local Bluetooth phone, and to discover and pair with remote devices.',
        'protectionLevel': 'dangerous',
        'label': 'bluetooth administration'
    },
    'android.permission.WRITE_EXTERNAL_STORAGE': {
        'permissionGroup': 'android.permission-group.STORAGE',
        'description': 'Allows an application to write to the SD card.',
        'protectionLevel': 'dangerous',
        'label': 'modify/delete SD card contents'
    },
    'android.permission.GET_PACKAGE_SIZE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to retrieve its code, data, and cache sizes',
        'protectionLevel': 'normal',
        'label': 'measure application storage space'
    },
    'android.permission.ASEC_MOUNT_UNMOUNT': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows the application to mount / unmount internal storage.',
        'protectionLevel': 'signature',
        'label': 'mount / unmount internal storage'
    },
    'android.permission.INSTALL_PACKAGES': {
        'permissionGroup': '',
        'description':
        'Allows an application to install new or updated Android packages. Malicious applications can use this to add new applications with arbitrarily powerful permissions.',
        'protectionLevel': 'signatureOrSystem',
        'label': 'directly install applications'
    },
    'android.permission.AUTHENTICATE_ACCOUNTS': {
        'permissionGroup': 'android.permission-group.ACCOUNTS',
        'description':
        'Allows an application to use the account authenticator capabilities of the AccountManager, including creating accounts and getting and setting their passwords.',
        'protectionLevel': 'dangerous',
        'label': 'act as an account authenticator'
    },
    'com.android.frameworks.coretests.SIGNATURE': {
        'permissionGroup': 'android.permission-group.COST_MONEY',
        'description': '',
        'protectionLevel': 'signature',
        'label': ''
    },
    'com.android.launcher.permission.READ_SETTINGS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to read the settings and shortcuts in Home.',
        'protectionLevel': 'normal',
        'label': 'read Home settings and shortcuts'
    },
    'com.android.alarm.permission.SET_ALARM': {
        'permissionGroup': 'android.permission-group.PERSONAL_INFO',
        'description':
        'Allows the application to set an alarm in an installed alarm clock application. Some alarm clock applications may not implement this feature.',
        'protectionLevel': 'normal',
        'label': 'set alarm in alarm clock'
    },
    'android.permission.INTERNAL_SYSTEM_WINDOW': {
        'permissionGroup': '',
        'description':
        'Allows the creation of windows that are intended to be used by the internal system user interface. Not for use by normal applications.',
        'protectionLevel': 'signature',
        'label': 'display unauthorized windows'
    },
    'android.permission.GET_TASKS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows application to retrieve information about currently and recently running tasks. May allow malicious applications to discover private information about other applications.',
        'protectionLevel': 'dangerous',
        'label': 'retrieve running applications'
    },
    'android.permission.SET_ORIENTATION': {
        'permissionGroup': '',
        'description':
        'Allows an application to change the rotation of the screen at any time. Should never be needed for normal applications.',
        'protectionLevel': 'signature',
        'label': 'change screen orientation'
    },
    'android.permission.SET_ACTIVITY_WATCHER': {
        'permissionGroup': '',
        'description':
        'Allows an application to monitor and control how the system launches activities. Malicious applications may completely compromise the system. This permission is only needed for development, never for normal phone usage.',
        'protectionLevel': 'signature',
        'label': 'monitor and control all application launching'
    },
    'com.android.frameworks.coretests.NORMAL': {
        'permissionGroup': 'android.permission-group.COST_MONEY',
        'description': '',
        'protectionLevel': 'normal',
        'label': ''
    },
    'android.permission.READ_SMS': {
        'permissionGroup': 'android.permission-group.MESSAGES',
        'description':
        'Allows application to read SMS messages stored on your phone or SIM card. Malicious applications may read your confidential messages.',
        'protectionLevel': 'dangerous',
        'label': 'read SMS or MMS'
    },
    'android.permission.BROADCAST_STICKY': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to send sticky broadcasts, which remain after the broadcast ends. Malicious applications can make the phone slow or unstable by causing it to use too much memory.',
        'protectionLevel': 'normal',
        'label': 'send sticky broadcast'
    },
    'android.permission.GLOBAL_SEARCH': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description': '',
        'protectionLevel': 'signatureOrSystem',
        'label': ''
    },
    'com.android.cts.permissionWithSignature': {
        'permissionGroup': '',
        'description': '',
        'protectionLevel': 'signature',
        'label': ''
    },
    'android.permission.PACKAGE_USAGE_STATS': {
        'permissionGroup': '',
        'description':
        'Allows the modification of collected component usage statistics. Not for use by normal applications.',
        'protectionLevel': 'signature',
        'label': 'update component usage statistics'
    },
    'android.permission.SET_ALWAYS_FINISH': {
        'permissionGroup': 'android.permission-group.DEVELOPMENT_TOOLS',
        'description':
        'Allows an application to control whether activities are always finished as soon as they go to the background. Never needed for normal applications.',
        'protectionLevel': 'dangerous',
        'label': 'make all background applications close'
    },
    'android.permission.CLEAR_APP_CACHE': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows an application to free phone storage by deleting files in application cache directory. Access is very restricted usually to system process.',
        'protectionLevel': 'dangerous',
        'label': 'delete all application cache data'
    },
    'android.permission.MOUNT_UNMOUNT_FILESYSTEMS': {
        'permissionGroup': 'android.permission-group.SYSTEM_TOOLS',
        'description':
        'Allows the application to mount and unmount filesystems for removable storage.',
        'protectionLevel': 'dangerous',
        'label': 'mount and unmount filesystems'
    },
    'android.permission.FLASHLIGHT': {
        'permissionGroup': 'android.permission-group.HARDWARE_CONTROLS',
        'description': 'Allows the application to control the flashlight.',
        'protectionLevel': 'normal',
        'label': 'control flashlight'
    },
}

AOSP_PERMISSION_GROUPS = {
    'android.permission-group.NETWORK': {
        'description': 'Allow applications to access various network features.',
        'label': 'Network communication'
    },
    'android.permission-group.STORAGE':
    {'description': 'Access the SD card.',
     'label': 'Storage'},
    'android.permission-group.MESSAGES': {
        'description': 'Read and write your SMS, e-mail, and other messages.',
        'label': 'Your messages'
    },
    'android.permission-group.PERSONAL_INFO': {
        'description':
        'Direct access to your contacts and calendar stored on the phone.',
        'label': 'Your personal information'
    },
    'android.permission-group.DEVELOPMENT_TOOLS': {
        'description': 'Features only needed for application developers.',
        'label': 'Development tools'
    },
    'android.permission-group.COST_MONEY': {'description': '',
                                            'label': ''},
    'android.permission-group.ACCOUNTS': {
        'description': 'Access the available accounts.',
        'label': 'Your accounts'
    },
    'android.permission-group.LOCATION': {
        'description': 'Monitor your physical location',
        'label': 'Your location'
    },
    'android.permission-group.HARDWARE_CONTROLS': {
        'description': 'Direct access to hardware on the handset.',
        'label': 'Hardware controls'
    },
    'android.permission-group.SYSTEM_TOOLS': {
        'description': 'Lower-level access and control of the system.',
        'label': 'System tools'
    },
    'android.permission-group.PHONE_CALLS': {
        'description': 'Monitor, record, and process phone calls.',
        'label': 'Phone calls'
    },
}
#################################################
