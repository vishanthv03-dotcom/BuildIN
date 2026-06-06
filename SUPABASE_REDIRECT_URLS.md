# Supabase Auth Redirect URLs Setup

## What Are Redirect URLs?

Redirect URLs tell Supabase where your app is hosted. When users:
- Sign up with email confirmation
- Click magic links
- Complete OAuth flows
- Reset passwords

...Supabase redirects them back to these URLs.

---

## Step-by-Step: Update Redirect URLs

### Step 1: Get Your Vercel App URL

1. Go to your Vercel Dashboard: https://vercel.com/dashboard
2. Find your Builden project
3. Copy your production URL (e.g., `https://builden-xyz.vercel.app`)

Keep this URL handy - you'll need it in the next steps.

---

### Step 2: Open Supabase Dashboard

1. Go to: https://supabase.com/dashboard
2. Select your Builden project
3. Click: **Authentication** in the left sidebar
4. Click: **URL Configuration** (you'll see this under Authentication)

---

### Step 3: Add Redirect URLs

You should see a section called **"Redirect URLs"** with a text field.

#### Add These URLs:

**For Local Development (already should be there):**
```
http://localhost:3000/auth/callback
```

**For Vercel Production (ADD THIS):**
```
https://your-builden-app.vercel.app/auth/callback
```

**For Vercel Preview Deployments (OPTIONAL but recommended):**
```
https://*.vercel.app/auth/callback
```

**Example - if your Vercel URL is `https://builden-prod.vercel.app`:**
```
http://localhost:3000/auth/callback
https://builden-prod.vercel.app/auth/callback
https://*.vercel.app/auth/callback
```

---

### Step 4: Save Changes

1. Paste all URLs in the "Redirect URLs" field (one per line)
2. Click the **Save** button
3. Wait for the green success message

You should see: ✅ "Redirect URLs updated successfully"

---

## Complete List of URLs to Add

Copy this and paste into Supabase:

```
http://localhost:3000/auth/callback
https://builden-prod.vercel.app/auth/callback
https://*.vercel.app/auth/callback
```

**Replace `builden-prod` with your actual Vercel project name!**

---

## How to Find Your Exact Vercel URL

### Method 1: From Vercel Dashboard
1. Go to https://vercel.com/dashboard
2. Click your project
3. At the top, you'll see your URL (usually: `yourproject.vercel.app`)

### Method 2: After Deployment
1. Your deployment succeeds
2. Vercel shows you the URL automatically
3. Copy that URL and come back to update Supabase

### Method 3: From Visit Deployment Button
1. In Vercel, find your latest deployment
2. Click the domain link at the top
3. That's your production URL

---

## Testing After Updating URLs

Once you've added the redirect URLs:

1. **Test Sign Up:**
   - Go to your app: https://your-vercel-url.vercel.app
   - Click "Get Started Free"
   - Enter email and password
   - You should be redirected to `/auth/sign-up-success`
   - ✅ If you see the success page, it worked!

2. **Test Sign In:**
   - Go to `/auth/login`
   - Enter your credentials
   - You should be redirected to your dashboard
   - ✅ If you see your dashboard, it worked!

3. **Test Email Confirmation (if enabled):**
   - Check your email for confirmation link
   - Click the link
   - Should redirect back to your app
   - ✅ If confirmed, it worked!

---

## Common Issues & Fixes

### Issue: "Redirect URL Not Allowed"

**Error message:** "The redirect_uri is not allowed"

**Solution:**
- Double-check your URL matches exactly (including `https://` and `/auth/callback`)
- Make sure you saved the changes
- Wait 30 seconds, then try again
- Hard refresh your browser (Ctrl+Shift+R or Cmd+Shift+R)

### Issue: Sign Up Page Keeps Reloading

**Cause:** Redirect URL not configured in Supabase

**Solution:**
- Follow Step 1-4 above
- Verify your production URL is added
- Test in an incognito window

### Issue: Works Locally but Not on Vercel

**Cause:** Forgot to add Vercel URL to Supabase

**Solution:**
- Add your Vercel URL following steps above
- Redeploy your app (optional, usually not needed)
- Hard refresh browser

### Issue: Preview Deployments Not Working

**Cause:** Preview URL not added

**Solution:**
- Add `https://*.vercel.app/auth/callback` to accept all Vercel preview URLs
- Or add each specific preview URL manually

---

## Understanding the /auth/callback Path

This is the special route that handles Supabase callbacks. You don't need to create anything - it's already in your code at:

```
app/auth/callback/route.ts
```

This route:
1. Receives the auth code from Supabase
2. Exchanges it for a session
3. Redirects you to the dashboard

You don't need to modify this file.

---

## After Deployment Checklist

- [ ] 1. Deployed app to Vercel
- [ ] 2. Got your Vercel production URL
- [ ] 3. Opened Supabase Dashboard
- [ ] 4. Went to Authentication → URL Configuration
- [ ] 5. Added your Vercel URL with `/auth/callback`
- [ ] 6. Clicked Save
- [ ] 7. Tested sign-up on your Vercel app
- [ ] 8. Tested sign-in on your Vercel app
- [ ] 9. Everything works! ✅

---

## Quick Reference

**Where to update:** Supabase Dashboard → Authentication → URL Configuration

**What to add:** `https://your-vercel-url.vercel.app/auth/callback`

**When to do it:** After deploying to Vercel

**Why it's needed:** So Supabase knows where to redirect users after auth

**Impact:** Without this, sign-up/login will fail with "Redirect URL not allowed"

---

## Need Your Exact URLs?

Run this after deploying to Vercel:

```bash
# Copy your Vercel URL and add to Supabase:
https://YOUR_VERCEL_PROJECT.vercel.app/auth/callback
```

Replace `YOUR_VERCEL_PROJECT` with your actual project name.

---

## Still Stuck?

1. Check Supabase docs: https://supabase.com/docs/guides/auth/redirect-urls
2. Check your browser console for auth errors (F12 → Console tab)
3. Verify your `.env.local` has correct Supabase URL
4. Make sure you're testing after saving changes (give it 30 seconds)

---

**That's it! Your Supabase auth redirects are now configured for production.** ✅
