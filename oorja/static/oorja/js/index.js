'use strict';

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var c,
    cx,
    width,
    height,
    balls,
    numBalls = 80,
    separationThreshold = 220,
    tau = Math.PI * 2,
    resetSwitch = document.getElementById('reset');

resetSwitch.onclick = function (e) {
    e.preventDefault();
    init();
};

function newColours() {
    var r = Math.floor(Math.random() * 32) + 64;
    var g = Math.floor(Math.random() * 32) + 64;
    var b = Math.floor(Math.random() * 32) + 64;
    return { r: r, g: g, b: b };
}

var Ball = function () {
    function Ball(id, x, y, radius, speed) {
        _classCallCheck(this, Ball);

        this.id = id;
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.colours = newColours();
        this.speed = speed;
        var initialVector = { x: Math.random() * 2 - 1, y: Math.random() * 2 - 1 };
        var vectorX = initialVector.x / Math.sqrt(initialVector.x * initialVector.x + initialVector.y * initialVector.y);
        var vectorY = initialVector.y / Math.sqrt(initialVector.x * initialVector.x + initialVector.y * initialVector.y);
        this.vector = { x: vectorX, y: vectorY };
    }

    Ball.prototype.draw = function draw() {
        cx.beginPath();
        cx.arc(this.x, this.y, this.radius, 0, tau);
        cx.fillStyle = 'rgba(' + this.colours.r + ',' + this.colours.g + ',' + this.colours.b + ', 1)';
        cx.fill();
    };

    Ball.prototype.step = function step() {
        this.x += this.vector.x * this.speed;
        this.y += this.vector.y * this.speed;
        this.checkBounds();
    };

    Ball.prototype.checkBounds = function checkBounds() {
        if (this.x - this.radius <= 0) {
            this.vector.x *= -1;
        }
        if (this.x + this.radius >= width) {
            this.vector.x *= -1;
        }
        if (this.y - this.radius <= 0) {
            this.vector.y *= -1;
        }
        if (this.y + this.radius >= height) {
            this.vector.y *= -1;
        }
    };

    return Ball;
}();

function run() {
    window.requestAnimationFrame(run);
    cx.clearRect(0, 0, width, height);
    for (var b = 0; b < balls.length; b++) {
        var ball = balls[b];
        ball.draw();
        ball.step();
        doLinks(ball);
    }
}

function doLinks(srcBall) {
    for (var b = 0; b < balls.length; b++) {

        if (b + 1 != srcBall.id) {

            var ball = balls[b];
            var separation = distance(srcBall, ball);

            if (separation < separationThreshold) {
                var colours = newColours();
                var opacity = 1;
                var _width = 1;
                if (separation > separationThreshold / 2) {
                    opacity = Math.abs(separation / separationThreshold - 1);
                }
                cx.beginPath();
                cx.moveTo(srcBall.x, srcBall.y);
                cx.lineTo(ball.x, ball.y);
                cx.lineWidth = _width;
                cx.strokeStyle = 'rgba(' + colours.b + ',' + colours.b + ',' + colours.b + ', ' + opacity + ')';
                cx.stroke();
            }
        }
    }
}

function distance(ball1, ball2) {
    var xDiff = ball1.x - ball2.x;
    var yDiff = ball1.y - ball2.y;
    return Math.sqrt(xDiff * xDiff + yDiff * yDiff);
}

function createBall(id) {
    var x = Math.random() * (width / 2) + width / 4;
    var y = Math.random() * (height / 2) + height / 4;
    var radius = Math.random() * 5 + 5;
    var speed = Math.random() * 1 + 1;
    return new Ball(id, x, y, radius, speed);
}

function init() {
    c = document.querySelector('canvas');
    width = c.width = window.innerWidth;
    height = c.height = window.innerHeight;
    cx = c.getContext('2d');
    window.addEventListener('resize', function () {
        width = c.width = window.innerWidth;
        height = c.height = window.innerHeight;
    }, false);
    cx.globalCompositeOperation = 'lighter';
    balls = [];
    for (var m = 0; m < numBalls; m++) {
        balls.push(createBall(m + 1));
    }
}

init();

run();