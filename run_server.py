#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple web2py development server for testing the hotel administration application.
This is a minimal setup to run the application.
"""

import os
import sys

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    # Try to import web2py
    from gluon.main import wsgibase
    from gluon.main import save_password
    from gluon import DAL, Field, validators
    print("Web2py modules found")
except ImportError:
    print("Web2py not found. Installing web2py...")
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'web2py'])
    from gluon.main import wsgibase
    from gluon.main import save_password

def main():
    """Run the development server"""
    import subprocess
    import time
    
    # Change to the application directory
    os.chdir(current_dir)
    
    # Start web2py server
    cmd = [
        sys.executable, '-c',
        '''
import os, sys
try:
    from gluon.main import main
    main()
except ImportError:
    print("Please install web2py first: pip install web2py")
    sys.exit(1)
        ''',
        '-a', 'admin',  # admin password
        '-i', '0.0.0.0',  # bind to all interfaces
        '-p', '8000',  # port
        '--nogui'  # no GUI
    ]
    
    print("Starting web2py server...")
    print("Application will be available at: http://localhost:8000/hotel_admin")
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    main()