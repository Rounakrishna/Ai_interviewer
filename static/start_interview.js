// Function to update output-box content with result
function updateOutputBox(result) {
    var outputBox = document.getElementById('outputBox');
    outputBox.innerHTML = '<p>' + result + '</p>'; // Assuming the result is a string, modify accordingly if it's an object
}

// Example usage: updateOutputBox('Your result here');

// Fetch data from Flask backend
fetch('/start_interview')
    .then(response => response.json())
    .then(data => {
        updateOutputBox(data.result); // Assuming the result is stored in 'result' key
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
