const express = require("express");
const amqp = require("amqplib");
const fs = require("fs");
const path = require("path");
const Jimp = require("jimp");

const app = express();
app.use(express.json());

async function sendToQueue(message, queue) {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertQueue(queue, {
    durable: true,
  });

  channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)));
  console.log("Message sent to queue:", message);

  setTimeout(() => {
    connection.close();
  }, 500);
}

app.post("/upload", upload.single("image"), async (req, res) => {
  const username = req.body.username;
  const imagePath = req.file.path;

  const imageBuffer = fs.readFileSync(imagePath);
  const imageBase64 = imageBuffer.toString("base64");

  const inputPath = path.join(
    __dirname,
    "processed",
    "input-" + req.file.originalname
  );
  const outputPath = path.join(
    __dirname,
    "processed",
    "bw-" + req.file.originalname
  );

  fs.writeFileSync(inputPath, imageBase64);

  await sendToQueue({ action: "image-uploaded", username }, "logger");

  Jimp.read(inputPath)
    .then((img) => {
      return img.greyscale().write(outputPath);
    })
    .then(async () => {
      console.log(
        `Image converted to black and white and saved to ${outputPath}`
      );

      await sendToQueue({ action: "image-proccesed", username }, "logger");
      await sendToQueue(
        {
          title: "imagem processada",
          message: "finish image conversion",
          username,
        },
        "notification"
      );

      return res.json({
        message: "Image uploaded and processed",
        image: outputPath,
      });
    })
    .then(() => {
      console.log("Notification sent to", username);
      channel.ack(msg);
    })
    .catch((err) => {
      console.error("Error processing image:", err);
      channel.nack(msg);
    });
  console.log(`Image saved to ${outputPath}`);
  return res.json({ message: "not possible process" });
});

app.listen(3002, () => {
  console.log("Notification service listening on port 3004");
  consumeFromQueue();
});
