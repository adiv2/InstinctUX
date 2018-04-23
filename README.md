# InstinctUX
Voice based desktop user interaction and personal assistant.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them


### Installing

To set it up on your local machine here is what you need to do. Install Python. Clone this repo using the following command:

```
git clone https://github.com/adiv2/InstinctUX
mkdir ~/.local/share/gnome-shell/extensions/instinct@vedant.example.com/InstinctUX/
mv  -v ~/InstinctUX/* ~/.local/share/gnome-shell/extensions/instinct@vedant.example.com/
```

Once installed you might have to restart your gnome-shell. You can do this by

```
press alt+f2
type r into the dialog that opens up
```



## Enabling InstinctUX
To activate the extension. Go to gnome-tweak-tool( If you haven't installed it, install now using
```
pacman -S gnome-tweak-tool
```
Then in gnome-tweak-tool go to "Shell Extensions" and turn on your extension. 

##Runing InstinctUX
Clicking on the microphone Icon at the top will allow you to talk to instinctUX.


## Built With

* [Gnome Shell](https://github.com/GNOME/gnome-shell/) - The UI Framework Used
* [Selenium](https://www.seleniumhq.org) - For browser automation
* [Nltk](https://www.nltk.org/) 


## Authors

* **Aditya Gholba** - *Automation Script*
* **Mohit Motwani** - *Intent Detection*
* **Soumik Malas** - *Black Book and Documentation*
* **Vedant Shetty** - *Voice to text and UI*



