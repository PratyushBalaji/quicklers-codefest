<html>
<script>
    let saveFile = () >=
    {
    	
        // Get the data from each element on the form.
    	const gender = document.getElementById('Gender');
        const age = document.getElementById('Age');
        const smoke = document.getElementById('Smoking');
        const yellow = document.getElementById('Yellow-fingers');
        const anxiety = document.getElementById('Anxiety');
        const peer = document.getElementById('Peer-Pressure');
        const chronic = document.getElementById('Chronic-disease');
        const fatigue = document.getElementById('Fatigue');
        const allergy = document.getElementById('Allergy');
        const wheezing = document.getElementById('Wheezing');
        const alcohol = document.getElementById('Alcohol');
        const cough = document.getElementById('Coughing');
        const breath = document.getElementById('Shortness-of-breath');
        const swallow = document.getElementById('Swallowing-difficulty');
        const chest = document.getElementById('Chest-pain');
        
        // This variable stores all the data.
        let data = 
            '\r Name: ' + name.value + ' \r\n ' + 
            'Age: ' +age.value + ' \r\n ' + 
            'Email: ' + email.value + ' \r\n ' + 
            'Country: ' + country.value + ' \r\n ' + 
            'Message: ' + msg.value;
        
        // Convert the text to BLOB.
        const textToBLOB = new Blob([data], { type: 'text/plain' });
        const sFileName = 'formData.txt';	   // The file to save the data.

        let newLink = document.createElement("a");
        newLink.download = sFileName;

        if (window.webkitURL != null) {
            newLink.href = window.webkitURL.createObjectURL(textToBLOB);
        }
        else {
            newLink.href = window.URL.createObjectURL(textToBLOB);
            newLink.style.display = "none";
            document.body.appendChild(newLink);
        }

        newLink.click(); 
    }
</script>
</html>