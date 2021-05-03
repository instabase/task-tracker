const naveen = {
  first_name: 'Naveen',
  last_name: 'Kashyap',
  email_address: "fake@email.com",
  confirm_email: "fake@email.com"
};
const courtney = {
  first_name: "Courtney",
  last_name: "Wallace",
  email_address: "anotherfake@email.com",
  confirm_email: "anotherfake@email.com"
}

const people = [naveen, courtney];

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ people });
  console.log(`saved people as ${people}`);
});