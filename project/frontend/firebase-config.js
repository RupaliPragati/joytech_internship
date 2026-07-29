import { initializeApp } from "https://www.gstatic.com/firebasejs/11.10.0/firebase-app.js";

import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
  signOut
} from "https://www.gstatic.com/firebasejs/11.10.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyCRbvTxCSjiaMhLFYbk7uMw5B6vhLPE1XY",
  authDomain: "cert-sat.firebaseapp.com",
  projectId: "cert-sat",
  storageBucket: "cert-sat.firebasestorage.app",
  messagingSenderId: "57886320656",
  appId: "1:57886320656:web:0f3a29124ebbf894730295",
  measurementId: "G-Y29HJWL3X9"
};


const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export {
    auth,
    provider,
    signInWithPopup,
    signOut
};

