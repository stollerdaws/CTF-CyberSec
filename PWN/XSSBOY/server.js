const express = require('express');
const path = require('path');
const fs = require('fs');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;
const puppeteer = require('puppeteer');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'static')));

// Serve index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'static', 'index.html'));
});

// Serve admin.html
app.get('/admin-bot', (req, res) => {
    res.sendFile(path.join(__dirname, 'static', 'admin.html'));
});

// Handle admin bot POST request
app.post('/admin-bot', async (req, res) => {
    const url = req.body.url;

    // Read the flag from flag.txt
    const flag = fs.readFileSync(path.join(__dirname, 'static', 'flag.txt'), 'utf8');

    try {
        const browser = await puppeteer.launch({
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });        
        const page = await browser.newPage();

        // Set the flag as a cookie in the headless browser
        await page.setCookie({
            name: 'flag',
            value: flag,
            domain: 'localhost:3000', // Set the correct domain
            httpOnly: true
        });
        
        // Navigate to the provided URL
        await page.goto(url, { waitUntil: 'networkidle2' });

        // Perform any additional actions with the page here if necessary

        await browser.close();

        res.send('Admin bot visited the page.');
    } catch (error) {
        console.error('Error in admin bot:', error);
        res.status(500).send('An error occurred in the admin bot');
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
