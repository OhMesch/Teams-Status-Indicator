if [ -z $(git fetch) ];
then
    echo "Up to date."
    exit 0
else
    echo "Updating..."
    killall -e "python3"
    git merge origin/main --no-edit
    python3 ~/Teams-Status-Indicator/main.py #Restart application
    echo "Update complete."
fi
