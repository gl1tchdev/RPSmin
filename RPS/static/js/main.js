function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
document.querySelectorAll('.form-outline').forEach((formOutline) => {
  new mdb.Input(formOutline).init();
});
document.querySelectorAll('.form-outline').forEach((formOutline) => {
  new mdb.Input(formOutline).update();
});
