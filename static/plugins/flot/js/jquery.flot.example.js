

(function($)
{

sales_chart =
  {
    data:
    {
      d1: []
    },

    plot: null,

    options:
    {
      grid:
      {
        autoHighlight: false,
        backgroundColor: null,
        color: '#c6f4eb',
        borderWidth: 0,
        borderColor: "transparent",
        clickable: true,
        hoverable: true
      },
      series: {
        lines: {
          show: true,
          fill: false,
          lineWidth: 2,
          steps: false
        },
        points: {
          show:true,
          radius: 3,
          lineWidth: 2,
          fill: true,
          fillColor: "#000"
        }
      },
      xaxis: {
         tickLength: 0,
      tickDecimals: 0,
      min:1,
      ticks: [[1,"JAN"], [2, "FEB"], [3, "MAR"], [4, "APR"], [5, "MAY"], [6, "JUN"], [7, "JUL"], [8, "AUG"], [9, "SEP"], [10, "OCT"], [11, "NOV"], [12, "DEC"]]
      },
      yaxis: {
        tickSize: 500,
        tickColor: '#F1F2F7'
      },
      legend: { show:false },
      shadowSize: 0,
      tooltip: true,
      tooltipOpts: {
        content: "%s : %y.3",
        shifts: {
          x: -30,
          y: -50
        },
        defaultTheme: false
      }
    },

    placeholder: "#sales-chart",

    init: function()
    {
      this.options.colors = ["#1abc9c"];
      this.options.grid.backgroundColor = null;

      var that = this;

      if (this.plot == null)
      {
        this.data.d1 = [ [1, 200], [2, 320], [3, 640], [4, 820], [5, 980], [6, 1000], [7, 1200], [8, 1600], [9, 1900], [10, 2100], [11, 2300], [12, 2500]];

      }
        var months = ["January", "February", "March", "April", "May", "Juny", "July", "August", "September", "October", "November", "December"];
      this.plot = $.plot(
        $(this.placeholder),
        [{
          label: "Data 1",
          data: this.data.d1,
          lines: { fill: 0.00 },
          points: { fillColor: "#fff" }
        }], this.options);
    }
  };


  function showTooltip(x, y, contents) {
    $('<div class="chart-tooltip">' + contents + '</div>').css( {
      position: 'absolute',
      display: 'none',
      top: y + 5,
      left: x + 5,
      opacity: 0.80
    }).appendTo("body").fadeIn(200);
  }


  $('#sales-chart').bind("plothover", function (event, pos, item) {
    $("#x").text(pos.x.toFixed(2));
    $("#y").text(pos.y.toFixed(2));

    if (item) {
      if (previousPoint != item.dataIndex) {
        previousPoint = item.dataIndex;

        $(".chart-tooltip").remove();
        var x = item.datapoint[0].toFixed(2),
          y = item.datapoint[1].toFixed(2);

        showTooltip(item.pageX, item.pageY, y);
      }
    }
    else {
      $(".chart-tooltip").remove();
      previousPoint = null;
    }
  });


   sales_chart.init();


})(jQuery);