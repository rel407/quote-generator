/* Script that is "listening" for the user to click the quote-button and in return,
it will return a random quote and corresponding author from the quotes-proj database */

document.getElementById("quote-button").addEventListener("click", function() {
    console.log("Button clicked!");

    // Show loading state while fetching
    document.getElementById("quote").textContent = "Loading...";
    document.getElementById("author").textContent = "";

    //fetch("http://127.0.0.1:5000/random_quote")
    fetch("https://https://quote-generator-mu-henna.vercel.app/api/database")
        .then(response => response.json())
        .then(data => {
            console.log("Data received:", data);

            if (data && data.quote && data.author) {
                // Set the quote and author text directly
                document.getElementById("quote").textContent = `"${data.quote}"`;
                document.getElementById("author").textContent = `- ${data.author}`;
            } else {
                console.error("Received data is missing quote or author");
                document.getElementById("quote").textContent = "Sorry, no quote available.";
                document.getElementById("author").textContent = "";
            }
        })
        .catch(error => {
            console.error("Error fetching quote:", error);
            document.getElementById("quote").textContent = "Sorry, an error occurred while fetching the quote.";
            document.getElementById("author").textContent = "";
        });
});
