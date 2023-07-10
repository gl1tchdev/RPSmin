function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function run(url) {
    toast1inst= document.getElementById('wait1');
    var toast1 = new bootstrap.Toast(toast1inst);
    toast1.show();
    await sleep(1000);
    toast2inst = document.getElementById('wait2');
    var toast2 = new bootstrap.Toast(toast2inst);
    toast2.show();
    await sleep(1000);
    toast3inst = document.getElementById('wait3');
    var toast3 = new bootstrap.Toast(toast3inst);
    toast3.show();
    await sleep(1000);
    window.open(url, '_self')
}
