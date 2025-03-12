function submitForm(event) {
    event.preventDefault(); // Prevents the form from submitting in the traditional way

    const name = document.querySelector("#name");
    const text = document.querySelector("#comments");
    const email = document.querySelector("#email");
    const form = document.querySelector(".form");
    const subject = document.querySelector("#subject");
    const successMessage = document.querySelector(".screen-reader-response"); // Assuming you have an element for success messages
    const fromAddress = "kfnfmax@gmail.com";

    // Email format validation using regular expression
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (
        name.value.trim() !== '' &&
        email.value.trim() !== '' &&
        emailRegex.test(email.value.trim()) &&
        subject.value.trim() !== '' &&
        text.value.trim() !== ''
    ) {
        Email.send({
            Host: "smtp.elasticemail.com",
            Username: "kfnfmax@gmail.com",
            Password: "0AF343E9BDCC7BDF44785F9EF673F216907A",
            To: 'maxw.zim@gmail.com',
            From: fromAddress,
            Subject: `${subject.value} von: ${email.value}`,
            Body: `I'm ${name.value}, <br> ${text.value}`
        }).then(function (message) {
            // Check if the email is sent successfully
            if (message.includes("OK")) {
                successMessage.innerHTML = '<div class="alert alert-success"><strong>Success!</strong> Email has been sent successfully.</div>';
                successMessage.style.display = 'block';

                // Clear form fields
                name.value = '';
                email.value = '';
                subject.value = '';
                text.value = '';

                // Optionally, reload the page after a delay
                setTimeout(function () {
                    window.location.reload();
                }, 100);
            } else {
                // Display an error message if the email is not sent successfully
                successMessage.innerHTML = '<div class="alert alert-danger"><strong>Error!</strong> Unable to send the email.</div>';
                successMessage.style.display = 'block';
            }
        });
    } else {
        // Display an error message for invalid or empty form fields
        successMessage.innerHTML = '<div class="alert alert-danger"><strong>Error!</strong> Please fill in all fields correctly.</div>';
        successMessage.style.display = 'block';
    }
}
