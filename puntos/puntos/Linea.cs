using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Shapes;

namespace puntos
{
    class Linea
    {
        double CoorX1 { get; set; }
        double CoorY1 { get; set; }
        double CoorX2 { get; set; }
        double CoorY2 { get; set; }
        SolidColorBrush ColorLine { get; set; }

        Random randy = new Random();

        public Linea(double CoorX1, double CoorY1, double CoorX2, double CoorY2)
        {
            this.CoorX1 = CoorX1;
            this.CoorX2 = CoorX2;
            this.CoorY1 = CoorY1;
            this.CoorY2 = CoorY2;
        }

        public void Dibujate(Canvas elCanvas)
        {
            Line l = new Line();
            l.X1 = CoorX1;
            l.X2 = CoorX2;
            l.Y1 = CoorY1;
            l.Y2 = CoorY2;
            l.StrokeThickness = 2;
            l.Stroke = new SolidColorBrush(Color.FromRgb((byte)randy.Next(256), (byte)randy.Next(256), (byte)randy.Next(256)));
            elCanvas.Children.Add(l);
        }
    }
}
