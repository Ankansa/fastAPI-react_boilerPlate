import React from 'react';
import { useState } from 'react';
import {
  Box,
  Typography,
  TextField,
  Button,
  Card,
  CardContent,
  Checkbox,
  FormControlLabel,
  Link,
} from '@mui/material';

import { postRequest } from '../../services/api'; // Adjust the import path as necessary


export default function SigninPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  return (
    <Box sx={{ minHeight: '100vh', p: 4, backgroundColor: '#fff', borderColor: '#003f88', borderWidth: 2, borderStyle: 'solid', borderRadius: 2, paddingLeft: 20 }}>
      {/* Logo */}
      <Box mb={4}>
        <img src="/logos/product_logo1.svg" alt="Logo" style={{ height: 50 }} /> {/* Replace with your logo */}
      </Box>

      {/* Layout */}
      <Box sx={{ display: 'flex', flexDirection: { xs: 'column', md: 'row' }, gap: 4, paddingLeft: 2, paddingRight: 5 }}>
        {/* Left Section - Features */}
        <Box sx={{ width: { xs: '100%', md: '70%' }, flexDirection: 'column', display: 'flex', justifyContent: 'center', gap: 2 }}>
          <Typography variant="h4" gutterBottom>Welcome Back!</Typography>
          <Typography variant="body1" gutterBottom>eazzquote helps businesses run their day-to-day operations better. Close more deals, build lasting customer relationships and grow your business effortlessly.</Typography>
          <FeatureCard title="All In One" description="Everything you need to manage your business in one place." />
          <FeatureCard title="Easy To Use" description="Easy to learn to use, even for CRM beginners. Just sign up and start." />
          <FeatureCard title="Expert Help" description="Team comes with support that will set you up and help you make the most of the platform." />
          <FeatureCard title="Secure Technology" description="Built on a solid stack, so your data is in good hands - safe, available at all times." />
        </Box>

        {/* Right Section - Sign In */}
        <Card sx={{ width: { xs: '100%', md: '30%' }, display: 'flex', justifyContent: 'center', alignItems: 'center', padding: 4, backgroundColor: '#f5f5f5' }}>
          <CardContent>
            <Typography variant="h5" gutterBottom align="center">Sign In</Typography>
            <Box component="form" noValidate autoComplete="off">
              <TextField fullWidth label="User Name" margin="normal" value={username}
                onChange={(e) => setUsername(e.target.value)} />
              <TextField fullWidth label="Password" type="password" margin="normal" value={password}
                onChange={(e) => setPassword(e.target.value)} />
              <FormControlLabel control={<Checkbox />} label="Remember Me" />
              <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
                <Link href="#">Forgot Password?</Link>
              </Box>
              <Button onClick={() => {
                LoginApi(username, password)
                  .then((response) => {
                    console.log('Login successful:', response);
                    // Handle successful login (e.g., redirect to dashboard)
                    localStorage.setItem('token', response.access_token); // Store token in local storage
                    window.location.href = '/dashboard'; // Redirect to dashboard
                  })
                  .catch((error) => {
                    console.error('Login failed:', error);
                    // Handle login failure (e.g., show error message)
                  });
              }} fullWidth variant="contained" sx={{ backgroundColor: '#007bff' }}>
                Sign In
              </Button>
              <Typography variant="body2" mt={2} textAlign="center">
                New on our platform? <Link href="#">Create an account</Link>
              </Typography>
            </Box>
          </CardContent>
        </Card>
      </Box>
    </Box>
  );
}

function FeatureCard({ title, description }) {
  return (
    <Box
      sx={{
        p: 2,
        borderRadius: 2,
        backgroundColor: '#003f88',
        color: '#fff',
        boxShadow: 1,
      }}
    >
      <Typography variant="h6">{title}</Typography>
      <Typography variant="body2">{description}</Typography>
    </Box>
  );
}

const LoginApi = async (username, password) => {
  console.log('LoginApi called with:', username, password);
  const data = {
    "username": username,
    "password": password,
  };
  try {
    const response = await postRequest('/v1/login', data, 'form_data', null);
    return response;
  } catch (error) {
    console.error('Login failed:', error);
    throw error;
  }
};