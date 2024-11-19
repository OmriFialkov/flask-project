// static/app.js
document.getElementById('fetch-quote').addEventListener('click', async () => {
    const response = await fetch('/get-quote');
    const data = await response.json();

    // Update the quote and author in the HTML
    document.getElementById('quote').innerText = `"${data.content}"`;
    document.getElementById('author').innerText = `— ${data.author}`;
});
