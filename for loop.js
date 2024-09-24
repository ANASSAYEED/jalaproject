

for (let property in fruit) {
    console.log(property, fruit[property]);
}


/* <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For/In Loop Example</title>
</head>
<body>

    <h1>Fruit Details</h1>

    <!-- Button to trigger the for/in loop -->
    <button onclick="displayFruitDetails()">Display Fruit Details</button>

    <!-- Div to show the results -->
    <div id="output"></div>

    <script>
        // Object representing a fruit with its details
        const fruit = {
            name: "Mango",
            color: "Yellow",
            taste: "Sweet",
            origin: "Tropical regions"
        };

        // Function to display the properties of the fruit object
        function displayFruitDetails() {
            // Get the output div
            const outputDiv = document.getElementById('output');
            outputDiv.innerHTML = '';  // Clear any existing content

            // Use a for/in loop to iterate through the properties of the object
            for (let property in fruit) {
                // Display the property and its value
                outputDiv.innerHTML += `<p><strong>${property}:</strong> ${fruit[property]}</p>`;
            }
        }
    </script>

</body>
</html> */