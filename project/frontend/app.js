import {
    auth,
    provider,
    signInWithPopup,
    signOut
} from "./firebase-config.js";

const loginBtn = document.getElementById("loginBtn");
const userData = document.getElementById("userData");
const responseBox = document.getElementById("response");
const toast = document.getElementById("toast");

const apiStatus = document.getElementById("apiStatus");
const authStatus = document.getElementById("authStatus");

const BACKEND_URL =
    "https://crispy-space-yodel-5gr5gx9vpgrrh66p-8000.app.github.dev/api/v1/google-login";

loginBtn.addEventListener("click", async () => {

    try {

        const result = await signInWithPopup(auth, provider);

        const user = result.user;

        const idToken = await user.getIdToken();

        const response = await fetch(BACKEND_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                id_token: idToken
            })

        });

        const data = await response.json();

        userData.innerHTML = `
            <img src="${user.photoURL}" width="70" style="border-radius:50%;margin-bottom:10px;">
            <h3>${user.displayName}</h3>
            <p>${user.email}</p>
            <small>${user.uid}</small>
        `;

        responseBox.textContent =
            JSON.stringify(data, null, 2);

        apiStatus.textContent = "● Online";
        apiStatus.className = "online";

        authStatus.textContent = "● Authenticated";
        authStatus.className = "online";

        toast.classList.add("show");

        setTimeout(() => {

            toast.classList.remove("show");

        }, 3000);

        loginBtn.textContent = "Logout";

        loginBtn.onclick = async () => {

            await signOut(auth);

            location.reload();

        };

    }

    catch (err) {

        console.error(err);

        responseBox.textContent =
            JSON.stringify(err, null, 2);

    }

});
const predictBtn = document.getElementById("predictBtn");
const predictionResult = document.getElementById("predictionResult");

const PREDICT_URL =
"https://crispy-space-yodel-5gr5gx9vpgrrh66p-8000.app.github.dev/api/v1/predict";

predictBtn.addEventListener("click", async () => {

    console.log("Predict button clicked");

    try {

        const payload = {
            satellite_id: "SAT-001",
            timestamp: new Date().toISOString(),
            battery_voltage: Number(document.getElementById("battery").value),
            temperature: Number(document.getElementById("temperature").value),
            cpu_usage: Number(document.getElementById("cpu").value),
            signal_strength: Number(document.getElementById("signal").value)
        };

        console.log("Sending:", payload);

        const response = await fetch(PREDICT_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        console.log("Status:", response.status);

        const data = await response.json();

        console.log(data);

        predictionResult.textContent =
            JSON.stringify(data, null, 2);

    } catch (err) {

        console.error(err);

        predictionResult.textContent =
            err.message;

    }

});

const data=await response.json();

predictionResult.textContent=
JSON.stringify(data,null,2);

