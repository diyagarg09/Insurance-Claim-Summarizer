document.addEventListener('DOMContentLoaded', () => {
    const app = document.getElementById('app');
    app.innerHTML = `
        <div style="max-width: 500px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px; font-family: sans-serif;">
            <h2>Insurance Summarizer</h2>
            <input type="file" id="pdfFile" accept=".pdf" style="margin-bottom: 15px;">
            <button id="btn" style="width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Process PDF
            </button>
            <p id="status" style="margin-top: 10px;"></p>
            <div id="result" style="display: none; margin-top: 20px; background: #f8f9fa; padding: 10px; border-radius: 5px;">
                <strong>Summary:</strong>
                <p id="summaryText"></p>
            </div>
        </div>
    `;

    document.getElementById('btn').addEventListener('click', startProcess);
});

async function startProcess() {
    const fileInput = document.getElementById('pdfFile');
    const status = document.getElementById('status');
    const resultDiv = document.getElementById('result');
    const summaryText = document.getElementById('summaryText');

    if (!fileInput.files[0]) return alert("Select a PDF!");

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    status.innerText = "Analyzing Report...";
    
    try {
        const response = await fetch('/upload', { method: 'POST', body: formData });
        const data = await response.json();
        
        summaryText.innerText = data.summary;
        resultDiv.style.display = 'block';
        status.innerText = "Done!";
    } catch (e) {
        status.innerText = "Error connecting to backend.";
    }
}