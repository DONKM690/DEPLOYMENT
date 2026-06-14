import React, { useState } from "react";
import "./App.css";

function App() {
  const [responseMessage, setResponseMessage] = useState("");

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  // Local testing
  const API = "http://127.0.0.1:8000/api";

  // Deployment kazhinjal:
  // const API = "https://donkm.pythonanywhere.com/api";

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`${API}/contact/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setResponseMessage("✅ Message Sent Successfully");

        setFormData({
          name: "",
          email: "",
          message: "",
        });
      } else {
        setResponseMessage("❌ Something went wrong");
      }
    } catch (error) {
      setResponseMessage("❌ Server Error");
    }
  };

  return (
    <div className="container">
      <h1>Contact Management System</h1>

      <form onSubmit={handleSubmit} className="form">
        <input
          type="text"
          name="name"
          placeholder="Enter Name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Enter Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <textarea
          name="message"
          placeholder="Enter Message"
          value={formData.message}
          onChange={handleChange}
          required
        />

        <button type="submit">
          Send Message
        </button>
      </form>

      {responseMessage && (
        <p className="success-message">
          {responseMessage}
        </p>
      )}
    </div>
  );
}

export default App;