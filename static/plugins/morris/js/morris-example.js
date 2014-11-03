// Updating
var nReloads = 0;

function data(offset) {
    var ret = [];
    for (var x = 0; x <= 360; x += 10) {
        var v = (offset + x) % 360;
        ret.push({
            x: x,
            y: Math.sin(Math.PI * v / 180).toFixed(4),
            z: Math.cos(Math.PI * v / 180).toFixed(4)
        });
    }
    return ret;
}
var graph = Morris.Line({
    element: 'graph',
    data: data(0),
    xkey: 'x',
    ykeys: ['y', 'z'],
    labels: ['sin()', 'cos()'],
    parseTime: false,
    ymin: -1.0,
    ymax: 1.0,
     lineColors: ['#1ABC9C'],
     pointFillColors: ['#19a88b'],
    hideHover: true
});

// Area as Line

function update() {
    nReloads++;
    graph.setData(data(5 * nReloads));
    $('#reloadStatus').text(nReloads + ' reloads');
}
setInterval(update, 100);

Morris.Area({
    element: 'area-as-line',
    behaveLikeLine: false,
    data: [
        {x: '2014 Q1', y: 3, z: 3},
        {x: '2014 Q2', y: 2, z: 1},
        {x: '2014 Q3', y: 2, z: 4},
        {x: '2014 Q4', y: 3, z: 3}
    ],
    xkey: 'x',
    ykeys: ['y', 'z'],
    labels: ['Y', 'Z'],
    lineColors:['#1ABC9C','#293949']

});

//Donut
Morris.Donut({
    element: 'donut',
    data: [
        {value: 70, label: 'foo', formatted: 'at least 70%' },
        {value: 15, label: 'bar', formatted: 'approx. 15%' },
        {value: 10, label: 'baz', formatted: 'approx. 10%' },
        {value: 5, label: 'A really really long label', formatted: 'at most 5%' }
    ],
    backgroundColor: '#fff',
    labelColor: '#1abc9c',
    colors: [
        '#1abc9c','#2dcc70','#f1c40f','#e84c3d'
    ],
    formatter: function (x, data) { return data.formatted; }
});


// Use Morris.Bar
Morris.Bar({
    element: 'bar',
    data: [
        {x: '2014 Q1', y: 3, z: 2, a: 3},
        {x: '2014 Q2', y: 2, z: null, a: 1},
        {x: '2014 Q3', y: 0, z: 2, a: 4},
        {x: '2014 Q4', y: 2, z: 4, a: 3}
    ],
    xkey: 'x',
    ykeys: ['y', 'z', 'a'],
    labels: ['Y', 'Z', 'A'],
    barColors:['#1abc9c','#2dcc70','#e84c3d']


});
