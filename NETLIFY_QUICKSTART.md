# Netlify Deployment - Quick Reference (5 Minutes)

## Copy-Paste Quick Deploy

### Step 1: Push to GitHub
```bash
cd /vercel/share/v0-project
git add .
git commit -m "Deploy to Netlify"
git push origin main
```

### Step 2: Connect to Netlify
1. Go to https://netlify.com
2. Click "New site from Git"
3. Choose GitHub
4. Select your repository
5. Click "Deploy site"

### Step 3: Add Environment Variables
In Netlify dashboard:
- Site settings → Build & deploy → Environment
- Click "Edit variables"
- Add these:

```
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGc...
```

### Step 4: Trigger Rebuild
- Deployments → "Trigger deploy" → "Deploy site"
- Wait 3-5 minutes

### Step 5: Update Supabase Redirect URLs
Go to Supabase dashboard:
1. Authentication → URL Configuration
2. Add these URLs:
```
http://localhost:3000/auth/callback
https://YOUR-NETLIFY-DOMAIN.netlify.app/auth/callback
https://deploy-preview-*.netlify.app/auth/callback
```

### Step 6: Test
- Visit your Netlify URL
- Test sign up
- Test sign in

✅ Done!

---

## netlify.toml (Already in your project)

```toml
[build]
  command = "npm run build"
  publish = ".next"
  node_version = "20.10.0"

[context.production.environment]
  NEXT_PUBLIC_SUPABASE_URL = "your_url_here"
  NEXT_PUBLIC_SUPABASE_ANON_KEY = "your_key_here"
```

---

## Environment Variables Needed

| Variable | Value | Where to get |
|----------|-------|--------------|
| `NEXT_PUBLIC_SUPABASE_URL` | Your Supabase URL | Supabase → Settings → API |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Anon public key | Supabase → Settings → API |

---

## Important Links

- Netlify Dashboard: https://app.netlify.com
- Your Site: app.netlify.com → select site
- Supabase Dashboard: https://supabase.com/dashboard
- GitHub: https://github.com

---

## Troubleshooting Quick Fixes

| Problem | Fix |
|---------|-----|
| Build fails | Check deploy log for errors |
| Can't sign up | Add environment variables |
| Sign up redirects to error | Update Supabase redirect URLs |
| Page is blank | Hard refresh (Ctrl+Shift+R) |
| Styling broken | Clear cache & hard refresh |

---

## Verify Build Settings

Netlify should auto-detect:
- **Build command:** `npm run build`
- **Publish directory:** `.next`
- **Node version:** 20.x

If not, manually set them in:
Site settings → Build & deploy → Build settings

---

That's it! Your frontend is now deployed on Netlify. 🚀
