// This script uses the Fetch API to send requests to the server
// and tries to mimic the behavior of a real user.

// First, we need to get the form data and the bot protection token
fetch('https://www.paxifico.com/bot-protection/', {
    method: 'GET',
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive',
      'Upgrade-Insecure-Requests': '1'
    }
  })
  .then(response => response.text())
  .then(html => {
    // We need to parse the HTML to get the form data and the bot protection token
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const form = doc.querySelector('form');
    const formData = new FormData(form);
    const botProtectionToken = doc.querySelector('input[name="bot_protection_token"]').value;
  
    // Now we need to send a request to the server to get the bot protection challenge
    fetch('https://www.paxifico.com/bot-protection/challenge', {
      method: 'POST',
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x
  

        