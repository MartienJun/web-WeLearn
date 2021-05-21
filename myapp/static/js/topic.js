const openModuleDetail = (e, detailId) => {
    for(let i = 1; i < 14; ++i) {
        document.getElementById("moduleDetail".concat(i.toString())).style.display = "none";
    }

    document.getElementById("moduleDetail".concat(detailId)).style.display = "block";
}