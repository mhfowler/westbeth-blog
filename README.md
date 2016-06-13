# westbeth-blog

# setup

```
cd ~/Desktop
git clone <your forked repository> 
cd ~/Desktop/westbeth
pip install -r requirements.txt
```

# how to use

### build the site
```cd ~/Desktop/westbeth; ./build.sh```

### run a local server to view your site
```cd ~/Desktop/westbeth; ./run.sh```

### deploy code to github pages
```cd ~/Desktop/westbeth; ./deploy.sh```

### how to make changes
- create a .html file templates/pages for every page of your site
- create layouts in templates/layouts which your pages use 
- write css in /static

The url to see your pages is the relative path to your page from the templates/pages directory.