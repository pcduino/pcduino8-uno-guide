# Johnny-Five on pcDuino platform

[Johnny-Five](http://johnny-five.io/) is the original JavaScript Robotics programming framework. Released by Bocoup in 2012, Johnny-Five is maintained by a community of passionate software developers and hardware engineers. Over 75 developers have made contributions towards building a robust, extensible and composable ecosystem.

This tutorial will tell you how to use Johnny-Five JavaScript programming framework to control GPIO on pcDuino3/pcDuino8 Uno.

## Prerequisites
**Hardware**
- pcDuino3/3B or pcDuino8 Uno

## Steps
### 1. Install a compatible version of node/npm
```sh
wget http://nodejs.org/dist/v0.10.24/node-v0.10.24-linux-arm-pi.tar.gz
tar xvzf node-v0.10.24-linux-arm-pi.tar.gz
cd node-v0.10.24-linux-arm-pi
sudo cp -R * /usr/local
```

### 2. Install Johnny-five and pcDuino-IO

Create a directory for your project, `cd` into the directory and run the following: 
```sh
npm init # follow the prompts
npm config set strict-ssl false
npm install johnny-five pcduino-io --save
```

### 3. "Blink" with Johnny-Five
Create a new JavaScript file.
```sh
vim blink.js
```
**Source code is :**
```js
var five = require("johnny-five");
var pcDuino = require("pcduino-io");
var board = new five.Board({
  io: new pcDuino()
});

board.on("ready", function() {
  var led = new five.Led(13);
  led.blink();
});
```

### 4. Run 

```sh
node blink.js
```
Take pcDuino8 Uno as example, please check the LED1, is it blinking?

## More information

* [Johnny-Five's API](http://johnny-five.io/api/)
* [Johnny-Five's examples](http://johnny-five.io/examples/)
* [Johnny-Five's Github repository](https://github.com/rwaldron/johnny-five)
* [Platform Support](http://johnny-five.io/platform-support/#pcduino3-dev-board)

