# Netlify CLI Deployment Guide

## Overview

Deploy your Next.js frontend directly from your terminal using Netlify CLI.

## Prerequisites

- Node.js installed
- npm or pnpm installed
- GitHub repo with your code
- Netlify account
- Supabase credentials

## Option 1: Netlify CLI Commands (Recommended)

### Step 1: Install Netlify CLI

```bash
npm install -g netlify-cli
# or
pnpm add -g netlify-cli
```

### Step 2: Authenticate with Netlify

```bash
netlify login
```

This opens your browser to authorize Netlify. Approve it and return to terminal.

### Step 3: Build Your Project

```bash
cd /vercel/share/v0-project
npm run build
# or
pnpm build
```

### Step 4: Deploy to Netlify

```bash
netlify deploy --prod
```

When prompted:
- Publish directory: `.next`
- Build command: `npm run build` or `pnpm build`

### Step 5: Add Environment Variables

After deployment:

```bash
netlify env:set NEXT_PUBLIC_SUPABASE_URL "https://your-project.supabase.co"
netlify env:set NEXT_PUBLIC_SUPABASE_ANON_KEY "your-anon-key-here"
```

### Step 6: Redeploy with Variables

```bash
netlify deploy --prod
```

## Option 2: Python Automation Script

Use this Python script to automate the entire deployment process.

See: `deploy_to_netlify.py`

## Quick Commands Reference

```bash
# Login to Netlify
netlify login

# Build the project
npm run build

# Deploy to production
netlify deploy --prod

# Deploy to preview (testing)
netlify deploy

# Set environment variable
netlify env:set KEY "value"

# View environment variables
netlify env:list

# Check deployment status
netlify status

# View logs
netlify logs
```

## Next.js Configuration

Your project uses:
- Framework: Next.js 16
- Build command: `npm run build`
- Publish directory: `.next`
- Node.js version: 20.10.0

These are already configured in `netlify.toml`.

## Environment Variables Needed

Only 2 variables required:

1. `NEXT_PUBLIC_SUPABASE_URL`
   - Get from: Supabase → Settings → API
   - Example: `https://your-project.supabase.co`

2. `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - Get from: Supabase → Settings → API
   - Example: `eyJhbGciOiJIUzI1NiIs...`

## Troubleshooting

### Build fails
Check the error in terminal output and fix before deploying.

### Environment variables not working
Make sure you used `netlify env:set` and redeployed with `--prod`.

### Still having issues
Run `netlify logs` to see deployment logs.

## Next Steps

After deployment:
1. Update Supabase redirect URLs
2. Test sign up on your live site
3. Monitor Netlify dashboard

Done! Your app is live! 🎉
