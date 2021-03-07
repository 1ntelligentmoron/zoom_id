function validateAdd() {
    const add = document.forms["add"]
    const inputs = String(add["subject"].value) + ": " + String(add["pmi"].value);
    alert(inputs) 
}