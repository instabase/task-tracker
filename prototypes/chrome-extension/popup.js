'use strict';

// Initialize button 
let page = document.getElementById("buttonDiv");
chrome.storage.sync.get("people", ({ people }) => {
    constructButtons(people);
});


function autofill() {
    chrome.storage.sync.get("person_obj", ({ person_obj }) => {

        const field2classes = {
            'first_name': ['ember-view z-textField js-z-textField z-text-field--basic js-z-text-field--basic js-glue-hiring-first-name', 'z-textField-input js-z-textField-input ember-view ember-text-field'],
            'last_name': ['ember-view z-textField js-z-textField z-text-field--basic js-z-text-field--basic js-glue-hiring-last-name', 'z-textField-input js-z-textField-input ember-view ember-text-field'],
            'email_address': ['  ember-view z-textField js-z-textField z-textField--email js-glue-hiring-email', 'z-textField-input js-z-textField-input ember-view ember-text-field'],
            'confirm_email': ['  ember-view z-textField js-z-textField z-textField--email js-glue-hiring-confirm-email', 'z-textField-input js-z-textField-input ember-view ember-text-field']
        };

        for (let field_name in field2classes) {
            const classes = field2classes[field_name];
            let element = document;
            while (classes.length > 0) {
                let class_name = classes.shift();
                element = element.getElementsByClassName(class_name)[0];
            }
            const field_value = person_obj[field_name];
            element.select();
            element.value = field_value;
            console.log(field_name, field_value, element);
        }
    });
}

// Add a button to the page for each person
function constructButtons(people) {
    for (let i = 0; i < people.length; i++) {
        let person = people[i];

        let button = document.createElement("button");
        button.textContent = person.first_name;
        button.style.width = person.first_name.length * 2 + 'ch';
        button.person = person;

        button.onclick = async function () {

            // Store the person for whom the button was pressed
            chrome.storage.sync.set({ person_obj: this.person });

            // autofill the page with the information
            let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
            chrome.scripting.executeScript({
                target: { tabId: tab.id },
                function: autofill
            });
        }

        page.appendChild(button);
    }
}