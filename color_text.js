function Interpolate(start, end, steps, count) {
    var s = start,
        e = end,
        final = s + (((e - s) / steps) * count);
    return Math.floor(final);
}

function Color(_r, _g, _b) {
    var r, g, b;
    var setColors = function(_r, _g, _b) {
        r = _r;
        g = _g;
        b = _b;
    };

    setColors(_r, _g, _b);
    this.getColors = function() {
        var colors = {
            r: r,
            g: g,
            b: b
        };
        return colors;
    };
}
				console.log("test1");

function myfunction(e) {
        var self = this,
            val = parseFloat(e.getAttribute("value")),
            red = new Color(232, 9, 26),
            white = new Color(255, 255, 255),
            green = new Color(6, 170, 60);
        var start = red;
        var end = white;

// given a number between -1 and 1 map to 0 and 100
        console.log(val);
        val = (val + 1) * 50;
        if(val > 100) {
            val = 100;
        } else if(val < 0) {
            val = 0;
        }

        if (val > 50) {
            start = white;
            end = green;
            val = val % 51;
        }

        var startColors = start.getColors(),
            endColors = end.getColors();
        var r = Interpolate(startColors.r, endColors.r, 50, val);
        var g = Interpolate(startColors.g, endColors.g, 50, val);
        var b = Interpolate(startColors.b, endColors.b, 50, val);

        e.style.backgroundColor = "rgb(" + r + "," + g + "," + b + ")"
    }