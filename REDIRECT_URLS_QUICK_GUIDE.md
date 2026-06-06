# Supabase Redirect URLs - Quick Guide

## 3-Minute Setup

### Step 1: Get Your Vercel URL
- Go to: https://vercel.com/dashboard
- Find your Builden project
- Copy the URL (example: `https://builden-xyz.vercel.app`)

### Step 2: Open Supabase
- Go to: https://supabase.com/dashboard
- Select your project
- Click: **Authentication** → **URL Configuration**

### Step 3: Add URLs
Paste this in the "Redirect URLs" field:

```
http://localhost:3000/auth/callback
https://YOUR_VERCEL_URL/auth/callback
https://*.vercel.app/auth/callback
```

Replace `YOUR_VERCEL_URL` with your actual Vercel URL

**Example:**
```
http://localhost:3000/auth/callback
https://builden-prod.vercel.app/auth/callback
https://*.vercel.app/auth/callback
```

### Step 4: Save
Click **Save** button. Wait for ✅ green message.

### Step 5: Test
Go to your app and try signing up. If it works → ✅ Done!

---

## Where to Find Everything

| What | Where |
|------|-------|
| Your Vercel URL | vercel.com/dashboard → your project → top of page |
| Redirect URLs setting | supabase.com/dashboard → your project → Authentication → URL Configuration |
| Your app | https://YOUR_VERCEL_URL.vercel.app |

---

## Common Mistakes (and How to Fix)

| Problem | Solution |
|---------|----------|
| "Redirect URL not allowed" error | Make sure you saved in Supabase and wait 30 sec |
| Sign up works locally but not on Vercel | You forgot to add your Vercel URL to Supabase |
| Can't find URL Configuration | Go to Authentication tab, scroll down, you'll see it |
| Not sure what URL to use | Copy it from your Vercel dashboard (the production URL) |

---

## The Format (Must Be Exact)

```
https://YOUR-PROJECT-NAME.vercel.app/auth/callback
```

**Must include:**
- `https://` (not http - except localhost)
- Your exact Vercel domain
- `/auth/callback` at the end

**Example of CORRECT format:**
```
https://builden-prod.vercel.app/auth/callback
```

**Examples of WRONG format:**
```
https://builden-prod.vercel.app (missing /auth/callback)
builden-prod.vercel.app/auth/callback (missing https://)
https://builden-prod.vercel.app/auth/callback/ (extra slash at end)
```

---

## Three URLs You Need

1. **Local Development** (already there)
   ```
   http://localhost:3000/auth/callback
   ```

2. **Production** (add this with your Vercel URL)
   ```
   https://your-vercel-url.vercel.app/auth/callback
   ```

3. **All Preview Deployments** (optional but helpful)
   ```
   https://*.vercel.app/auth/callback
   ```

---

## Copy-Paste Template

```
http://localhost:3000/auth/callback
https://YOUR_VERCEL_PROJECT_NAME.vercel.app/auth/callback
https://*.vercel.app/auth/callback
```

1. Replace `YOUR_VERCEL_PROJECT_NAME` with your actual project name
2. Copy this entire block
3. Paste into Supabase URL Configuration field
4. Click Save
5. Done! ✅

---

## Testing Checklist

After updating, test these:

- [ ] Go to https://YOUR_VERCEL_URL
- [ ] Click "Get Started Free"
- [ ] Fill in email & password
- [ ] Click Sign Up
- [ ] You should see success page (not error)
- [ ] Try clicking "Sign In" button
- [ ] You should be logged in
- [ ] All working? ✅ You're done!

---

## Still Need Help?

Read the full guide: `SUPABASE_REDIRECT_URLS.md` (in your project)

It has:
- Detailed step-by-step instructions
- Screenshots/descriptions
- Troubleshooting section
- Testing instructions
- Common errors & fixes

---

**That's it! Your auth redirects are now configured.** ✅
