// const twilio = require("twilio"); // Or, for ESM: 
import twilio from "twilio";
import dotenv from "dotenv";
dotenv.config();
// Find your Account SID and Auth Token at twilio.com/console
// and set the environment variables. See http://twil.io/secure
const accountSid = "ACcbeab1da4dc567d3ee34617fe01d98ef";
const authToken = process.env.token;
const client = twilio(accountSid, authToken);

async function createMessage() {
  const message = await client.messages.create({
    body: "take medicine at ",
    from: "+19494461393",
    to: "+919014276932",
  });

  console.log(message.body);
}

createMessage();