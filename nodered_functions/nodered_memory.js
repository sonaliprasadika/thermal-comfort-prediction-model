// nodered function for memory usage information
// source: Internet of Things course material (code shown in exercise session), slightly altered by team
let newMsg = {}; // Declare newMsg
// Ensure msg.payload is treated as a string
let payloadStr = String(msg.payload);
newMsg.payload = parseFloat(payloadStr.slice(0, 8)); // Extract and parse the first 8 characters
return newMsg;
