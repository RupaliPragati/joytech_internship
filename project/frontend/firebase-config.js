// ============================================================
// FIREBASE APP
// ============================================================

import {
    initializeApp
} from "https://www.gstatic.com/firebasejs/10.13.2/firebase-app.js";


// ============================================================
// FIREBASE AUTH
// ============================================================

import {
    getAuth,
    GoogleAuthProvider,
    signInWithRedirect,
    getRedirectResult,
    onAuthStateChanged,
    signOut
} from "https://www.gstatic.com/firebasejs/10.13.2/firebase-auth.js";


// ============================================================
// FIREBASE WEB APP CONFIGURATION
// ============================================================

const firebaseConfig = {

    apiKey: "AIzaSyCRbvTxCSjiaMhLFYbk7uMw5B6vhLPE1XY",

    authDomain:
        "cert-sat.firebaseapp.com",

    projectId:
        "cert-sat",

    storageBucket:
        "cert-sat.firebasestorage.app",

    messagingSenderId:
        "57886320656",

    appId:
        "1:57886320656:web:d3359b9e9f8bfebf730295",

    measurementId:
        "G-W9YRTESNEK"
};


// ============================================================
// INITIALIZE FIREBASE
// ============================================================

const app =
    initializeApp(firebaseConfig);


// ============================================================
// INITIALIZE FIREBASE AUTH
// ============================================================

const auth =
    getAuth(app);


// ============================================================
// GOOGLE AUTH PROVIDER
// ============================================================

const provider =
    new GoogleAuthProvider();


// ============================================================
// EXPORT
// ============================================================

export {
    auth,
    provider,
    signInWithRedirect,
    getRedirectResult,
    onAuthStateChanged,
    signOut
};