# CommonComment

This Sublime Text 2/3  plugin adds some convenient commands to write file/block comments.

## Commands

* **Add Current Datetime**

```
Example:
2019-03-20 21:10:54
```

* **Add Code Block Comment**

support c/c++/go/python/shell/markdown file

```
Example:
/** {write comments here} (Alan 2019-03-21 18:00:30) **/
```

* **Add File Comment**

support c/c++/go/python/shell/markdown file

```
Example:
/**
 * Author:       Alan (gchinaran@gmail.com)
 * Created Time: 2019-03-21 18:02:56
 * File Name:    foo.go
 * Description:  {write file description}
 */
```

## Manual Install

Git clone this repository and place the `CommonComment` directory into your `Packages` directory.

OSX:

```
# Install the plugin
git clone https://github.com/chinaran/enjoy-life.git {your/dir}
cp -r {your/dir}/enjoy-life/sublime_text/CommonComment ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
```

Linux:

```
# Install the plugin
git clone https://github.com/chinaran/enjoy-life.git {your/dir}
cp -r {your/dir}/enjoy-life/sublime_text/CommonComment ~/.config/sublime-text-3/Packages/CommonComment
```

## Settings

You need set your own `name` and `email` at `CommonComment.sublime-settings`

```
{
	"author_name": "Your Name",
	"author_email": "yours@email.com"
}
```


## Key Bindings

No need to use key binding

You can use sublime text's COMMAND PALETTE
