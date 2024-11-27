
 function sendMessage(a,b) {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === 'hi') return 'hello';

    // Display user's message
    addMessage(userInput, 'user');

    // Clear input field
    document.getElementById('user-input').value = '';

    // Generate bot's response (simple hardcoded responses for demonstration)
    const botResponse = getBotResponse(userInput);
    setTimeout(() => {
        addMessage(botResponse, 'bot');
    }, 500); // Simulate a delay for the bot response
}

function addMessage(text, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.className = `message ${sender}`;
    messageElement.textContent = text;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

function getBotResponse(userInput) {
    // Simple responses
    if (userInput.toLowerCase().includes('hello')) return 'Hi there!';
    if (userInput.toLowerCase().includes('how are you')) return 'I am just a bot, but I am doing great!';
    if (userInput.toLowerCase().includes('bye')) return 'Goodbye!';
    if (userInput.toLowerCase().includes('owner')) return 'venki!';
    if(userInput.toLowerCase().includes('about')) return 'Here , this is the blog website by venkatesan!';
   
    return 'Sorry, I do not understand that.';
}

