# Bible Verse CLI

*Note*: this tool currently only supports the ESV version using the ESV API.

## Get Started

Make sure you have Python installed with at least version Python 3. Clone this repository.

Open a terminal and navigate to the project directory. At the root, you can run the `main.py` file with `$ python3 main.py`.

You can pass an argument with `--reference` or simply `-r` and then a string containing the verse reference. For example:

`$ python3 main.py -r "John 3:16`

If this is your first time running the script, it willl prompt you to authenticate the ESV API using your auth token.

If you don't have an auth token for the ESV API service yet, sign up for one at https://api.esv.org/docs/.

It is recommended to make the main.py into an executable and assign it an alias in your shell's profile. For example, in bash or zsh, you can make the file executable by running:

`$ chmod +x [pathToYourFile]`

And then you can open your shell profile and assign the command an alias like `bible` to run the script as easily as:

`$ bible -r "John 3:16`

