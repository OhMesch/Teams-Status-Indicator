if [[ $(git fetch) ]];
then
    echo "Up to date."
    exit 0
else
    echo "Updating..."
    # kill realname
    # pkill -f forrealfigureoutthenamefirst
    git merge origin/main
    python main.py #Restart application
    echo "Update complete."
fi
