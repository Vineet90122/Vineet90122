const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const authRoutes = require('./routes/authRoutes');
const path = require("path");
const fs = require('fs'); 
const uploadRoutes = require("./routes/uploadRoutes");

require('dotenv').config(); 

const app = express();
app.use(express.json());

app.use((req, res, next) => {
  console.log("📥 Request received:");
  console.log("➡️ Method:", req.method);
  console.log("➡️ URL:", req.url);
  console.log("📦 Body:", req.body);
  next();
});
console.log("🔑 Email user:", process.env.EMAIL_USER);
console.log("🔑 Email pass:", process.env.EMAIL_PASS ? "✔️ Loaded" : "❌ Not Loaded");
console.log("🔑 Key:", process.env.RESEND_API_KEY);

app.use(cors());

const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir);
}
app.use("/uploads", express.static(path.join(__dirname, "uploads")));
app.use("/api", uploadRoutes);
app.use('/api/auth', authRoutes);

app.get('/', (req, res) => {
  res.send('Auth System Running');
});

mongoose.connect(process.env.MONGO_URI, {
 
})
.then(() => {
  console.log('✅ MongoDB Connected');
  app.listen(process.env.PORT || 5000, () => {
    console.log(`🚀 Server running on http://localhost:${process.env.PORT || 5000}`);
  });
})
.catch((err) => console.error('❌ DB Connection Error:', err));
