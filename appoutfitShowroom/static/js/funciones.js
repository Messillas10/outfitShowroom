function showToast() {
    const t = document.getElementById("toast");
    if (!t) return;

    t.classList.add("show");

    setTimeout(() => {
        t.classList.remove("show");
    }, 3000);
}