#!/usr/bin/env python3
"""
Netlify Frontend Deployment Script for Builden

This script automates the deployment of your Next.js frontend to Netlify.
It handles authentication, building, deploying, and setting environment variables.

Usage:
    python3 deploy_to_netlify.py
    
    Or with custom values:
    python3 deploy_to_netlify.py --supabase-url https://xxx.supabase.co --anon-key xxxxx
"""

import subprocess
import sys
import os
from pathlib import Path


class NetlifyDeployer:
    """Automates Netlify deployment for Next.js projects."""
    
    def __init__(self):
        self.project_dir = Path(__file__).parent
        self.supabase_url = None
        self.anon_key = None
    
    def run_command(self, command, description=""):
        """Run a shell command and handle errors."""
        print(f"\n{'='*70}")
        if description:
            print(f"Step: {description}")
        print(f"Running: {command}")
        print(f"{'='*70}")
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.project_dir,
                check=True,
                capture_output=False
            )
            print(f"✅ Success: {description}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: Command failed - {description}")
            print(f"Error code: {e.returncode}")
            return False
    
    def check_netlify_cli(self):
        """Check if Netlify CLI is installed."""
        print("\nChecking Netlify CLI installation...")
        result = subprocess.run(
            "netlify --version",
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"✅ Netlify CLI found: {result.stdout.strip()}")
            return True
        else:
            print("❌ Netlify CLI not found")
            print("\nInstall it with:")
            print("  npm install -g netlify-cli")
            print("  # or")
            print("  pnpm add -g netlify-cli")
            return False
    
    def check_netlify_login(self):
        """Check if user is logged into Netlify."""
        print("\nChecking Netlify authentication...")
        result = subprocess.run(
            "netlify status",
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Netlify authentication found")
            return True
        else:
            print("❌ Not logged into Netlify")
            print("\nRunning login...")
            return self.run_command("netlify login", "Netlify Login")
    
    def get_environment_variables(self):
        """Get Supabase credentials from user."""
        print("\n" + "="*70)
        print("Environment Variables Setup")
        print("="*70)
        
        # Check if already set in .env.local
        env_file = self.project_dir / ".env.local"
        if env_file.exists():
            print(f"\nFound .env.local file")
            response = input("Use Supabase credentials from .env.local? (y/n): ")
            if response.lower() == 'y':
                self.load_from_env_file()
                return True
        
        print("\nEnter your Supabase credentials:")
        print("(Get these from: Supabase Dashboard → Settings → API)")
        
        self.supabase_url = input("\nNEXT_PUBLIC_SUPABASE_URL: ").strip()
        if not self.supabase_url:
            print("❌ Supabase URL is required")
            return False
        
        self.anon_key = input("NEXT_PUBLIC_SUPABASE_ANON_KEY: ").strip()
        if not self.anon_key:
            print("❌ Supabase anon key is required")
            return False
        
        print("\n✅ Environment variables collected")
        return True
    
    def load_from_env_file(self):
        """Load environment variables from .env.local."""
        env_file = self.project_dir / ".env.local"
        try:
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('NEXT_PUBLIC_SUPABASE_URL='):
                        self.supabase_url = line.split('=', 1)[1].strip('"\'')
                    elif line.startswith('NEXT_PUBLIC_SUPABASE_ANON_KEY='):
                        self.anon_key = line.split('=', 1)[1].strip('"\'')
        except Exception as e:
            print(f"Error reading .env.local: {e}")
    
    def build_project(self):
        """Build the Next.js project."""
        package_manager = "pnpm" if (self.project_dir / "pnpm-lock.yaml").exists() else "npm"
        return self.run_command(
            f"{package_manager} run build",
            "Building Next.js project"
        )
    
    def deploy_to_netlify(self):
        """Deploy to Netlify production."""
        return self.run_command(
            "netlify deploy --prod",
            "Deploying to Netlify Production"
        )
    
    def set_environment_variables(self):
        """Set environment variables in Netlify."""
        print("\n" + "="*70)
        print("Setting Environment Variables")
        print("="*70)
        
        if not self.supabase_url or not self.anon_key:
            print("⚠️  Skipping environment variables (not provided)")
            return True
        
        commands = [
            (
                f'netlify env:set NEXT_PUBLIC_SUPABASE_URL "{self.supabase_url}"',
                "Setting NEXT_PUBLIC_SUPABASE_URL"
            ),
            (
                f'netlify env:set NEXT_PUBLIC_SUPABASE_ANON_KEY "{self.anon_key}"',
                "Setting NEXT_PUBLIC_SUPABASE_ANON_KEY"
            ),
        ]
        
        for command, description in commands:
            if not self.run_command(command, description):
                return False
        
        return True
    
    def redeploy_with_variables(self):
        """Redeploy to apply environment variables."""
        return self.run_command(
            "netlify deploy --prod",
            "Redeploying with environment variables"
        )
    
    def display_summary(self):
        """Display deployment summary."""
        print("\n" + "="*70)
        print("✅ DEPLOYMENT COMPLETE!")
        print("="*70)
        
        print("\nYour Next.js frontend has been deployed to Netlify!")
        
        print("\nNext steps:")
        print("1. Get your Netlify URL from: https://app.netlify.com")
        print("2. Update Supabase redirect URLs:")
        print("   - Go to: Supabase Dashboard → Authentication → URL Configuration")
        print("   - Add these URLs:")
        print("     • http://localhost:3000/auth/callback")
        print("     • https://YOUR-NETLIFY-URL/auth/callback")
        print("     • https://deploy-preview-*.netlify.app/auth/callback")
        print("3. Test your live app!")
        
        print("\nUseful Netlify CLI commands:")
        print("  netlify status          - Check deployment status")
        print("  netlify logs            - View deployment logs")
        print("  netlify env:list        - List environment variables")
        print("  netlify env:set KEY VAL - Set new environment variable")
        print("  netlify deploy --prod   - Deploy again")
        
        print("\n" + "="*70)
    
    def deploy(self):
        """Run the complete deployment process."""
        print("\n" + "="*70)
        print("🚀 NETLIFY DEPLOYMENT FOR BUILDEN")
        print("="*70)
        
        # Step 1: Check CLI
        if not self.check_netlify_cli():
            return False
        
        # Step 2: Check authentication
        if not self.check_netlify_login():
            return False
        
        # Step 3: Get environment variables
        if not self.get_environment_variables():
            return False
        
        # Step 4: Build
        if not self.build_project():
            return False
        
        # Step 5: Deploy
        if not self.deploy_to_netlify():
            return False
        
        # Step 6: Set variables
        if not self.set_environment_variables():
            print("⚠️  Warning: Could not set environment variables")
        
        # Step 7: Redeploy with variables
        if self.supabase_url and self.anon_key:
            if not self.redeploy_with_variables():
                print("⚠️  Warning: Could not redeploy with variables")
        
        # Step 8: Display summary
        self.display_summary()
        return True


def main():
    """Main entry point."""
    deployer = NetlifyDeployer()
    
    try:
        success = deployer.deploy()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Deployment cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
