// firebase-messaging-sw.js
var static_url = "{% get_static_prefix %}";
var media_url = "{% get_media_prefix %}";
importScripts(static_url + 'js/vvg/firebase-app.js');
importScripts(static_url + 'js/vvg/firebase-messaging.js');

firebase.initializeApp({
    messagingSenderId: '1012634719343'
});

