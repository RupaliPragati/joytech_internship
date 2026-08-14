import {
    auth,
    provider,
    signInWithRedirect,
    onAuthStateChanged,
    signOut
} from "./firebase-config.js?v=3";


// ============================================================
// ELEMENTS
// ============================================================

const loginBtn = document.getElementById("loginBtn");
const userData = document.getElementById("userData");
const responseBox = document.getElementById("response");
const toast = document.getElementById("toast");

const apiStatus = document.getElementById("apiStatus");
const authStatus = document.getElementById("authStatus");

const predictBtn = document.getElementById("predictBtn");
const predictionResult =
    document.getElementById("predictionResult");


// ============================================================
// BACKEND
// ============================================================

const BACKEND_URL =
    "https://crispy-space-yodel-5gr5gx9vpgrrh66p-8000.app.github.dev";

const LOGIN_URL =
    `${BACKEND_URL}/api/v1/google-login`;

const PREDICT_URL =
    `${BACKEND_URL}/api/v1/predict`;


// ============================================================
// GOOGLE LOGIN
// ============================================================

if (loginBtn) {

    loginBtn.addEventListener("click", async () => {

        try {

            console.log("Starting Google login...");

            await signInWithRedirect(
                auth,
                provider
            );

        } catch (error) {

            console.error(
                "Google login error:",
                error
            );

            if (responseBox) {
                responseBox.textContent =
                    `Login Error:\n\n${error.message}`;
            }

        }

    });

}


// ============================================================
// FIREBASE AUTH STATE
// ============================================================

onAuthStateChanged(auth, async (user) => {

    console.log(
        "Firebase auth state:",
        user
    );


    // ========================================================
    // USER NOT LOGGED IN
    // ========================================================

    if (!user) {

        console.log(
            "No authenticated user."
        );

        if (authStatus) {

            authStatus.textContent =
                "● Not Authenticated";

            authStatus.className =
                "offline";
        }

        if (loginBtn) {
            loginBtn.textContent =
                "Continue with Google";
        }

        return;
    }


    // ========================================================
    // USER IS LOGGED IN
    // ========================================================

    console.log(
        "User successfully authenticated:",
        user.email
    );


    try {

        // ====================================================
        // GET FIREBASE ID TOKEN
        // ====================================================

        const idToken =
            await user.getIdToken();

        console.log(
            "Firebase ID token received."
        );


        // ====================================================
        // SEND TOKEN TO FASTAPI
        // ====================================================

        const response =
            await fetch(
                `${BACKEND_URL}/api/v1/google-login`,
    {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        id_token: idToken
                    })
                }
            );


        console.log(
            "Backend response status:",
            response.status
        );


        // ====================================================
        // BACKEND RESPONSE
        // ====================================================

        const data =
            await response.json();

        console.log(
            "Backend response:",
            data
        );


        if (!response.ok) {

            throw new Error(
                data.detail ||
                `Backend returned ${response.status}`
            );
        }


        // ====================================================
        // DISPLAY USER
        // ====================================================

        if (userData) {

            userData.innerHTML = `

                <img
                    src="${user.photoURL || ""}"
                    width="70"
                    height="70"
                    style="
                        border-radius:50%;
                        margin-bottom:10px;
                    "
                >

                <h3>
                    ${user.displayName || "Google User"}
                </h3>

                <p>
                    ${user.email || ""}
                </p>

                <small>
                    ${user.uid}
                </small>

            `;
        }


        // ====================================================
        // BACKEND RESPONSE
        // ====================================================

        if (responseBox) {

            responseBox.textContent =
                JSON.stringify(
                    data,
                    null,
                    2
                );
        }


        // ====================================================
        // STATUS
        // ====================================================

        if (apiStatus) {

            apiStatus.textContent =
                "● Online";

            apiStatus.className =
                "online";
        }


        if (authStatus) {

            authStatus.textContent =
                "● Authenticated";

            authStatus.className =
                "online";
        }


        // ====================================================
        // LOGIN BUTTON → LOGOUT
        // ====================================================

        if (loginBtn) {

            loginBtn.textContent =
                "Logout";

            loginBtn.onclick =
                async () => {

                    try {

                        await signOut(auth);

                        location.reload();

                    } catch (error) {

                        console.error(
                            "Logout error:",
                            error
                        );

                    }

                };
        }


        // ====================================================
        // SUCCESS MESSAGE
        // ====================================================

        if (toast) {

            toast.textContent =
                "Google Authentication Successful";

            toast.classList.add("show");

            setTimeout(() => {

                toast.classList.remove("show");

            }, 3000);

        }

    } catch (error) {

        console.error(
            "Backend authentication error:",
            error
        );

        if (responseBox) {

            responseBox.textContent =
                `Backend Authentication Error:\n\n${error.message}`;

        }

        if (authStatus) {

            authStatus.textContent =
                "● Backend Authentication Failed";

            authStatus.className =
                "offline";
        }

    }

});


// ============================================================
// TELEMETRY PREDICTION
// ============================================================

if (predictBtn) {

    predictBtn.addEventListener(
        "click",
        async () => {

            try {

                const payload = {

                    satellite_id:
                        "SAT-001",

                    timestamp:
                        new Date().toISOString(),

                    battery_voltage:
                        Number(
                            document.getElementById(
                                "battery"
                            ).value
                        ),

                    temperature:
                        Number(
                            document.getElementById(
                                "temperature"
                            ).value
                        ),

                    cpu_usage:
                        Number(
                            document.getElementById(
                                "cpu"
                            ).value
                        ),

                    signal_strength:
                        Number(
                            document.getElementById(
                                "signal"
                            ).value
                        )

                };


                console.log(
                    "Sending telemetry:",
                    payload
                );


                const response =
                    await fetch(
                        PREDICT_URL,
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body:
                                JSON.stringify(
                                    payload
                                )
                        }
                    );


                const data =
                    await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        `Prediction failed: ${response.status}`
                    );
                }


                predictionResult.textContent =
                    JSON.stringify(
                        data,
                        null,
                        2
                    );

            } catch (error) {

                console.error(
                    "Prediction error:",
                    error
                );

                if (predictionResult) {

                    predictionResult.textContent =
                        `Prediction Error:\n\n${error.message}`;

                }

            }

        }
    );

}