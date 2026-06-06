# Netlify Deployment Guide for Builden Frontend

## Overview

This guide provides complete step-by-step instructions to deploy your Builden Next.js frontend to Netlify.

**Total Time:** ~15-20 minutes
**Difficulty:** Easy ✅

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start (5 minutes)](#quick-start-5-minutes)
3. [Detailed Step-by-Step](#detailed-step-by-step)
4. [Environment Variables Setup](#environment-variables-setup)
5. [Update Supabase Redirect URLs](#update-supabase-redirect-urls)
6. [Testing & Verification](#testing--verification)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before starting, make sure you have:

- ✅ GitHub account with your Builden repo
- ✅ Netlify account (free at netlify.com)
- ✅ Supabase project with credentials
- ✅ Your Supabase URL and anon key

**Get your Supabase credentials:**
1. Go to https://supabase.com/dashboard
2. Select your Builden project
3. Click "Settings" → "API"
4. Copy:
   - Project URL (NEXT_PUBLIC_SUPABASE_URL)
   - Anon public key (NEXT_PUBLIC_SUPABASE_ANON_KEY)

---

## Quick Start (5 Minutes)

### Method 1: Connect GitHub (Recommended - Automatic Deploys)

**Step 1:** Push code to GitHub
```bash
cd /vercel/share/v0-project
git add .
git commit -m "Ready for Netlify deployment"
git push origin main
```

**Step 2:** Go to Netlify
- Visit https://netlify.com
- Click "Sign Up" or "Log In"
- Click "New site from Git"

**Step 3:** Connect GitHub
- Click "GitHub"
- Authorize Netlify to access your GitHub
- Select your "BuildIN" repository

**Step 4:** Configure Build Settings
- Build command: `npm run build`
- Publish directory: `.next`
- Click "Deploy site"

**Step 5:** Add Environment Variables
- After deploy starts, go to "Site settings"
- Click "Build & deploy" → "Environment"
- Click "Edit variables"
- Add these 2 variables:
  ```
  NEXT_PUBLIC_SUPABASE_URL = your_supabase_url
  NEXT_PUBLIC_SUPABASE_ANON_KEY = your_supabase_anon_key
  ```
- Click "Save"

**Step 6:** Trigger Rebuild
- Go to "Deployments"
- Click "Trigger deploy" → "Deploy site"

**Step 7:** Test
- Wait 3-5 minutes for build
- Click the site URL
- Test sign up functionality

✅ **Done!** Your app is live on Netlify!

---

## Detailed Step-by-Step

### Part 1: Prepare Your Repository

**Step 1.1:** Ensure all changes are committed
```bash
cd /vercel/share/v0-project

# Check status
git status

# Add all changes
git add .

# Commit
git commit -m "Add Netlify configuration"

# Push to GitHub
git push origin main
```

**Step 1.2:** Verify package.json has correct scripts
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

### Part 2: Create Netlify Account

1. Go to https://netlify.com
2. Click "Sign up"
3. Choose "Sign up with GitHub"
4. Authorize Netlify
5. Verify your email

### Part 3: Create New Site from Git

1. Click "New site from Git"
2. Choose "GitHub"
3. Search for your repository name (e.g., "BuildIN")
4. Click to select it

### Part 4: Configure Build Settings

You should see a form with:

**Build command:** `npm run build`
**Publish directory:** `.next`

These are already configured in `netlify.toml`, so:
- Netlify will auto-detect them ✅
- Or manually enter if prompted

**Node.js version:** (should auto-detect 20.x)

### Part 5: Deploy

Click "Deploy site"

You'll see:
```
✓ Site created
✓ Building...
```

Wait 3-5 minutes for build to complete.

### Part 6: Get Your Netlify URL

After build completes:
- You'll see a URL like: `https://builden-prod.netlify.app`
- This is your live site!

---

## Environment Variables Setup

Your app needs Supabase credentials to work. Two ways to add them:

### Method A: Netlify Dashboard (UI)

1. Go to your Netlify site
2. Click "Site settings"
3. Click "Build & deploy" (left sidebar)
4. Click "Environment"
5. Click "Edit variables"
6. Add these variables:

| Key | Value | Where to get it |
|-----|-------|-----------------|
| `NEXT_PUBLIC_SUPABASE_URL` | Your Supabase URL | Supabase → Settings → API → URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Your anon key | Supabase → Settings → API → Anon Key |

7. Click "Save"

### Method B: netlify.toml (Recommended)

The `netlify.toml` file in your project already has the structure.

Just update these values in `netlify.toml`:

```toml
[context.production.environment]
  NEXT_PUBLIC_SUPABASE_URL = "https://your-project.supabase.co"
  NEXT_PUBLIC_SUPABASE_ANON_KEY = "eyJhbGc..."
```

Then push to GitHub:
```bash
git add netlify.toml
git commit -m "Update Netlify env vars"
git push origin main
```

---

## Update Supabase Redirect URLs

After Netlify gives you a URL, you MUST update Supabase:

1. Get your Netlify site URL:
   - Go to your Netlify site dashboard
   - URL is at the top (e.g., `https://builden-prod.netlify.app`)

2. Go to Supabase Dashboard:
   - https://supabase.com/dashboard
   - Select your project
   - Click "Authentication"
   - Click "URL Configuration"

3. Add these redirect URLs:
   ```
   http://localhost:3000/auth/callback
   https://YOUR_NETLIFY_URL/auth/callback
   https://deploy-preview-*.netlify.app/auth/callback
   ```

4. Replace `YOUR_NETLIFY_URL` with your actual Netlify URL

5. Click "Save"

**Why?** This tells Supabase where to redirect users after sign-up/sign-in.

---

## Testing & Verification

### Test 1: Site Loads
1. Go to your Netlify URL
2. You should see the Builden landing page ✅
3. Logo should be visible ✅

### Test 2: Sign Up Works
1. Click "Get Started Free"
2. Go to sign up page
3. Enter email and password
4. Click "Sign Up"
5. Should redirect to confirmation page ✅

### Test 3: Sign In Works
1. Click "Sign In"
2. Enter your email and password
3. Click "Sign In"
4. Should redirect to dashboard ✅

### Test 4: Dashboard Access
1. After signing in, you should be in dashboard
2. Check that your role-specific dashboard appears ✅

If all tests pass: **You're live! 🎉**

---

## Troubleshooting

### Issue 1: Build fails

**Error message:** "Build failed"

**Solution:**
1. Go to "Deployments"
2. Click the failed deploy
3. Click "Deploy log"
4. Read the error message
5. Common causes:
   - Missing dependencies: Run `npm install`
   - Syntax errors: Check the file listed in error
   - Environment variables: Verify they're set

### Issue 2: "Supabase URL not found" error on live site

**Cause:** Environment variables not set

**Solution:**
1. Go to site settings
2. Build & deploy → Environment
3. Add NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY
4. Trigger rebuild: "Trigger deploy" → "Deploy site"

### Issue 3: Sign up redirects to error page

**Cause:** Supabase redirect URLs not updated

**Solution:**
1. Follow "Update Supabase Redirect URLs" section above
2. Make sure all 3 URLs are added
3. Wait 30 seconds
4. Try sign up again

### Issue 4: Blank page or 404 error

**Cause:** Netlify not configured for Next.js

**Solution:**
1. Verify `netlify.toml` exists in project root
2. Verify publish directory is `.next`
3. Verify build command is `npm run build`
4. Trigger rebuild

### Issue 5: Styling looks broken (CSS not loading)

**Cause:** Next.js assets not loading

**Solution:**
1. Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
2. Clear browser cache
3. Try incognito/private window
4. Check browser console for errors

---

## Useful Links

- **Netlify Dashboard:** https://app.netlify.com
- **Your Site Settings:** app.netlify.com → select your site → Site settings
- **Deploy Logs:** app.netlify.com → select site → Deployments → click deploy
- **Supabase Dashboard:** https://supabase.com/dashboard

---

## Next Steps After Deployment

1. ✅ Test sign up/login
2. ✅ Update Supabase redirect URLs
3. ✅ Test authentication flow
4. ✅ Set up custom domain (optional)
   - Netlify → Site settings → Domain management
   - Add your custom domain
5. ✅ Set up SSL (automatic with Netlify)
6. ✅ Monitor deploy logs
   - Netlify → Deployments → View logs

---

## Important Notes

- **Automatic Deployments:** Every time you push to GitHub, Netlify auto-deploys ✅
- **Build Time:** Usually 2-5 minutes
- **Preview Deployments:** Each pull request gets a preview URL
- **Environment Variables:** Keep your Supabase keys safe!
- **Caching:** Clear cache if you see old content

---

## Support

If you run into issues:

1. **Check Netlify Logs:**
   - Netlify → Deployments → Failed deploy → View logs
   - Read the error message carefully

2. **Check Supabase Status:**
   - Supabase → Project settings → Check if any issues reported

3. **Check Your Code:**
   - Are all imports correct?
   - Are environment variables referenced correctly?

4. **Common Issues:**
   - Missing `netlify.toml` - add it to project root
   - Wrong node version - use Node 20.x
   - Supabase keys wrong - double-check in Supabase dashboard

---

## Deployment Summary

You now have:

✅ Netlify configuration file (`netlify.toml`)
✅ Automatic GitHub deployments
✅ Environment variables configured
✅ Supabase integration ready
✅ Build optimized for production

Your Builden frontend is ready to deploy! 🚀
