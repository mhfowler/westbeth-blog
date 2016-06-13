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
- pages are rendered using jinja (http://jinja.pocoo.org/docs/dev/)
- create a .html file templates/pages for every page of your site
- create layouts in templates/layouts which your pages use 
- write css in /static
- whenever you want to see changes you made to the html of pages, run build.sh
- after you run build.sh, the url to see a page is the relative path to the page from the templates/pages directory