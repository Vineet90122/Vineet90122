// controllers/uploadController.js
 
// ✅ Add this
//this code save audio to local storges.
//exports.uploadAudio = (req, res) => {
 // if (!req.file) {
  //  return res.status(400).json({ message: "No audio file uploaded" });
 // }

  //return res.status(200).json({
    //message: "Audio uploaded successfully",
    //filePath: `/uploads/${req.file.filename}`,
  //});
//};

const Audio = require("../models/Audio");  // ✅ Add this

exports.uploadAudio = async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ message: "No audio file uploaded" });
    }

    const filePath = `/uploads/${req.file.filename}`;

    // ✅ Save to MongoDB
    const audio = new Audio({
      filePath,
      // userId: req.user._id, // if using auth middleware
    });

    await audio.save();

    return res.status(200).json({
      message: "Audio uploaded successfully",
      filePath,
    });
  } catch (err) {
    console.error("❌ Upload error:", err);
    return res.status(500).json({ message: "Server error" });
  }
};

