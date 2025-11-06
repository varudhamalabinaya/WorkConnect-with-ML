# Profile Upload Troubleshooting Guide

## Issues Identified and Fixed

### 1. **Hardcoded Backend URL**
- **Problem**: The frontend was hardcoded to `http://localhost:5000`, causing issues when accessing from different hosts or networks
- **Fix**: Implemented dynamic URL detection that uses the request origin and environment detection
- **Impact**: Now works from any hostname/IP address, both development and production

### 2. **Missing File Save Validation**
- **Problem**: Backend didn't verify if the file was actually saved to disk successfully
- **Fix**: Added validation check after file save operation
- **Impact**: Better error reporting if file system operations fail

### 3. **Inadequate CORS Headers on File Serving**
- **Problem**: Uploaded files might not have proper CORS headers when served back to the client
- **Fix**: Added comprehensive CORS headers to the `/uploads/<filename>` endpoint
- **Impact**: Files can now be loaded from any origin and domain

### 4. **Poor Error Logging**
- **Problem**: Generic exception handling without detailed error information
- **Fix**: Added detailed logging with traceback for debugging
- **Impact**: Server logs now show exactly what went wrong during uploads

### 5. **No Retry Logic**
- **Problem**: Single network failure would fail the entire upload
- **Fix**: Implemented automatic retry logic with exponential backoff (up to 3 retries)
- **Impact**: Transient network issues are automatically recovered

### 6. **Vite Development Server Not Proxying Requests**
- **Problem**: When running `npm run dev`, requests go directly to the backend without proper routing
- **Fix**: Added Vite proxy configuration for `/api` and `/uploads` endpoints
- **Impact**: Development server now properly forwards requests to the backend

---

## Backend Improvements (routes.py & app.py)

### ProfilePictureUploadResource Changes
```python
- Dynamic URL construction: origin = request.origin or request.host_url.rstrip('/')
- File existence validation after save
- Enhanced error logging with traceback
- Graceful handling of old file deletion failures
```

### File Serving Endpoint Changes
```python
- Added Access-Control-Allow-Origin: '*'
- Added Access-Control-Allow-Methods: 'GET, HEAD, OPTIONS'
- Added Access-Control-Allow-Headers: 'Content-Type, Authorization'
- Added Cache-Control headers for performance
```

---

## Frontend Improvements (ProfilePictureUpload.tsx)

### 1. **Dynamic Backend URL Detection**
- Automatically detects if running in development mode
- Uses Vite proxy in development
- Falls back to proper URL construction in production

### 2. **Enhanced Error Handling**
- Specific error messages for different failure scenarios
- Differentiation between auth errors, file size errors, network errors
- Clear guidance for user actions

### 3. **Automatic Retry Logic**
- Handles AbortError (timeouts) with retries
- Handles network failures with exponential backoff
- Displays retry status to user

### 4. **Improved Validation**
- Stricter file type validation using proper MIME types
- File read error detection
- Token presence validation before upload

### 5. **Better User Feedback**
- Detailed toast messages for each error type
- Progress feedback during retries
- Success confirmation

---

## Vite Configuration (vite.config.ts)

### Proxy Setup
```typescript
server: {
  proxy: {
    "/api": {
      target: "http://localhost:5000",
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, "/api"),
    },
    "/uploads": {
      target: "http://localhost:5000",
      changeOrigin: true,
    },
  },
}
```

This ensures:
- API requests are routed through the dev server
- CORS issues are eliminated in development
- Files are served from the correct location

---

## Additional Troubleshooting Steps

### If uploads still fail:

#### 1. **Check Backend Server Status**
```bash
# Verify backend is running
curl http://localhost:5000/health

# Should return:
# {"status": "healthy", "message": "WorkConnect API is running"}
```

#### 2. **Verify Upload Folder Permissions**
```bash
# Check if uploads folder exists and is writable
ls -la backend/uploads/

# If permission issues:
chmod 755 backend/uploads/
```

#### 3. **Check Browser Developer Tools**
- Open F12 → Network tab
- Try uploading a profile picture
- Check the failed request details:
  - **Status Code**: 
    - 401 = Auth token missing/expired
    - 413 = File too large
    - 500 = Server error
  - **Response**: See exact error message
  - **Headers**: Verify CORS headers are present

#### 4. **MongoDB Connection**
- Ensure MongoDB is running
- Check connection string in backend/.env
- Verify user can be created/updated

#### 5. **File System Issues**
- Check disk space: `df -h`
- Verify no file permission errors in backend logs
- Check if antivirus is blocking file writes

#### 6. **Network Issues**
- Test backend connectivity: `ping localhost:5000`
- Check if firewall is blocking port 5000
- Verify CORS is not blocked by browser extensions
- Try disabling VPN/proxy if using one

#### 7. **Backend Logs**
Run backend with more verbose output:
```bash
cd backend
python app.py > backend.log 2>&1
# Watch for detailed error messages during upload attempts
```

#### 8. **Test Upload with cURL**
```bash
# First get a token (login)
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'

# Then test upload
curl -X POST http://localhost:5000/api/users/profile-picture \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "profile_picture=@/path/to/image.jpg"
```

---

## Configuration Checklist

- [ ] Backend running on port 5000
- [ ] Frontend running on port 8080
- [ ] MongoDB connection working
- [ ] `backend/uploads` folder exists and is writable
- [ ] `UPLOAD_FOLDER` is correctly set in config.py
- [ ] JWT token is properly generated and stored in localStorage
- [ ] CORS is properly configured on backend
- [ ] No firewall blocking ports 5000/8080
- [ ] File size under 5MB
- [ ] File format is PNG/JPG/GIF/WebP
- [ ] Browser developer tools showing no CORS errors

---

## Performance Optimization Tips

1. **Compress Images Before Upload**
   - Reduce file size to speed up uploads
   - Target: under 2MB for best performance

2. **Use Lazy Loading for Images**
   - Load profile pictures only when needed
   - Reduces initial page load time

3. **Implement Image Resizing**
   - Consider server-side image resizing
   - Generate thumbnails for faster loading

4. **Add Upload Progress**
   - Use XMLHttpRequest or modern fetch with ReadableStream
   - Show progress bar to users

5. **Cache Uploaded Files**
   - Use Cache-Control headers (already implemented)
   - Browser will cache images for faster subsequent loads

---

## Expected Behavior After Fixes

1. ✅ Upload starts immediately when file is selected
2. ✅ Loading indicator shows during upload
3. ✅ File is validated before upload
4. ✅ Success message appears after upload
5. ✅ Profile picture updates immediately
6. ✅ Image is stored on server at `/uploads/{filename}`
7. ✅ Image is accessible from all browsers/networks
8. ✅ Previous image is deleted when new one is uploaded
9. ✅ Network failures are automatically retried
10. ✅ Proper error messages guide user to fix issues

---

## Support Information

If the upload still fails after following all steps:

1. Check the browser console (F12) for JavaScript errors
2. Check the backend console for Python errors
3. Verify all files in this guide have been updated correctly
4. Ensure backend was restarted after code changes
5. Clear browser cache and localStorage if needed

The implementation now includes comprehensive error handling, retry logic, and proper CORS configuration to handle the upload issues you were experiencing.
