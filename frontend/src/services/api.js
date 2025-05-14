// src/services/api.js

import axios from 'axios';

const API_BASE = 'http://127.0.0.1:8000/api';

/**
 * Reusable POST request function
 * @param {string} endpoint - API endpoint (e.g., '/login')
 * @param {object} data - Payload for the POST request
 * @param {string} token - Optional JWT token for protected routes
 * @param {string} contentType - Content type for the request (default: 'json' for form data parameter pass "form_data" in string format)
 * @returns {Promise<any>}
 */
export const postRequest = async (endpoint, data, contentType = "json", token = null) => {
  try {
    const headers = token
      ? { Authorization: `Bearer ${token}` }
      : {};
    const contentType_formData = token ? 'application/json' : 'application/x-www-form-urlencoded';
    const contentType_json = token ? 'application/json' : 'application/json';
    if (contentType === "form_data"){
      headers['Content-Type'] = contentType_formData;
    }
    else {
      headers['Content-Type'] = contentType_json;
    }

    const response = await axios.post(`${API_BASE}${endpoint}`, data, {
      headers,
    });

    return response.data;
  } catch (error) {
    console.error(`POST ${endpoint} failed:`, error);
    throw error;
  }
};
