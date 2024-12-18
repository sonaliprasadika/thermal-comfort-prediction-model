// function for nodered
// calculates the latency and prepares message payload to be sent to influxdb
// for humidity and pressure, change all 'temp' and 'temperature' words with the
// corresponding measurement type

let data = msg.payload;

if (data.temperature) {
  let temperature = parseFloat(data.temperature);

  // generate new timestamp
  // current time (ms) when the message is received in Node-RED
  let receivedTimestamp = Date.now();
  // calculate the latency
  let latency = Math.abs(receivedTimestamp - data.timestamp);

  // construct for InfluxDB
  msg.payload = {
    measurement: "temp+latency",
    value: temperature,
    latency: latency,
  };
} else {
  //drop invalid messages abd warn
  node.warn("Invalid temperature: " + data.temperature);
  return null;
}

return msg;
