function generateDocument() {
    const documentType = document.getElementById("documentType").value;
    const details = document.getElementById("details").value;
    const preview = document.getElementById("preview");

    if (documentType === "" || details.trim() === "") {
        preview.innerHTML = "Please select a document type and enter the required details.";
        return;
    }

    const documentName =
        document.getElementById("documentType").options[
            document.getElementById("documentType").selectedIndex
        ].text;

    preview.innerHTML = `
        <h3>${documentName}</h3>
        <p>${details}</p>
        <p><strong>Status:</strong> Draft generated successfully.</p>
    `;
}
