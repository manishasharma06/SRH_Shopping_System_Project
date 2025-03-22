exports = function(changeEvent) {
    const fullDocument = changeEvent.fullDocument;
    const accountSid = "AC12aff653ced9b00654404c75956e287b";
    const authToken = "f319450a29d88f5b689a1a3a7b59c2cb";
    const client = require('twilio')(accountSid, authToken);
    client.messages
    .create({
         body: 'Your total order amount is ' + fullDocument['amount'] + '₹.Thanks for ordering. ',
         from: '+12057076299',
         to: '+49176 59699123'
    }) .then(message => console.log(message.sid));
};