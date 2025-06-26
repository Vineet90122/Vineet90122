

const { Resend } = require('resend');

const resend = new Resend('re_VafX2LoV_48J7pwByqL7h6Ab8gkSxt3kt');

const sendEmail = async (to, subject, text) => {
  try {
    const data = await resend.emails.send({
      from: 'Aaroh AI <onboarding@resend.dev>', // ✅ Use a verified domain or default
      to,
      subject,
      text,
    });

    console.log('📨 Email sent:', data);
  } catch (err) {
    console.error('❌ Email sending failed:', err);
    throw err;
  }
};

module.exports = sendEmail;
