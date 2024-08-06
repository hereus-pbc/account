let includedDomain = false;
let animating = false;

function replaceAnimation(element, newText, until) {
    let interval1 = setInterval(() => {
        if ((() => {
            if (until && until !== "") { return !element.get().endsWith(until);}
            else { return element.get().length !== 0; }
        })()) { element.set(element.get().substring(0, element.get().length - 1)); } else {
            clearInterval(interval1);
            if (element.get().length !== 0) {
                element.set(element.get().substring(0, element.get().length - 1));
            }
            if (newText !== "") {
                let interval2 = setInterval(() => {
                    if (newText.length) {
                        element.set(element.get() + newText[0]);
                        newText = newText.substring(1, newText.length);
                    } else {
                        clearInterval(interval2);
                    }
                }, 50);
            }
        }
    }, 50);
}

function load_message(text) {
    let label = document.getElementById("message");
    let cLabel = {
        set: (text) => {
            label.innerHTML = text;
        }, get: () => {
            return label.innerHTML;
        }
    };
    replaceAnimation(cLabel, text, null);
}

function branding() {
    let email_box = document.getElementById("email");
    let cEmail = {
        set: (text) => {
            email_box.value = text;
        }, get: () => {
            return email_box.value;
        }
    };
    let email_label = document.getElementById("email_label");
    let cLabel = {
        set: (text) => {
            email_label.innerHTML = text;
        }, get: () => {
            return email_label.innerHTML;
        }
    };
    let cTitle = {
        set: (text) => {
            document.title = text;
        }, get: () => {
            return document.title;
        }
    };
    if (email_box.value.includes("@")) {
        if (email_box.value.split("@")[1] === "hereus.net") {
            includedDomain = true;
            setTimeout(() => {
                includedDomain = false;
                if (cLabel.get().startsWith("Username")) {
                    replaceAnimation(cLabel, "", "(");
                }
            }, 10000);
            replaceAnimation(cEmail, "", "@");
        }
        if (cLabel.get().includes("Username")) {
            cTitle.set("Login - TheProtocols Account (HereUS Client)");
            replaceAnimation(cLabel, "Email", null);
        }
    } else if (!email_box.value.includes("@") && cLabel.get().includes("Email")) {
        cTitle.set("Login - HereUS Account");
        replaceAnimation(
            cLabel,
            "Username" + (() => {
                if (includedDomain) {
                    return " (You don't have to type @hereus.net on this site)";
                } else {
                    return "";
                }
            })(),
            null
        );
    }
}

setInterval(branding, 500);
