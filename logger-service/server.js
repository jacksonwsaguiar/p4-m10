const express = require("express");
const mongoose = require("mongoose");
const amqp = require('amqplib');

const app = express();
app.use(express.json());

mongoose.connect("mongodb+srv://jacksonaguiar:fGZAQgHzjlyIXcSJ@cluster0.zkykwzk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const LogSchema = new mongoose.Schema({
  action: String,
  username: String,
  timestamp: { type: Date, default: Date.now },
});

const Log = mongoose.model("Log", LogSchema);

async function consumeFromQueue() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();
  const queue = "logger";

  await channel.assertQueue(queue, {
    durable: true,
  });

  channel.consume(queue, async (msg) => {
    if (msg !== null) {
      const content = JSON.parse(msg.content.toString());
      const { action, username } = content;
      try {
        const log = new Log({ action, username });
        await log.save();
      } catch (error) {
        console.error("Error saving log:", error);
      }
      channel.ack(msg);
    }
  });
}


app.listen(3004, () => {
  console.log("Log service listening on port 3002");
  consumeFromQueue();
});
