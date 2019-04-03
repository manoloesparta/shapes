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
    class Punto
    {

        public double X { get; set; }
        public double Y { get; set; }

        Random randy = new Random();

        public Punto(double X, double Y)
        {
            this.X = X;
            this.Y = Y;
        }

        public void Dibujate(Canvas elCanvas)
        {
            Ellipse e = new Ellipse();
            e.Height = 10;
            e.Width = 10;
            e.Fill = new SolidColorBrush(Color.FromRgb((byte)randy.Next(256), (byte)randy.Next(256), (byte)randy.Next(256)));
            elCanvas.Children.Add(e);
            Canvas.SetTop(e, Y);
            Canvas.SetLeft(e, X);
        }

        public void Relacionar(Canvas elCanvas, List<Punto> puntos)
        {
            foreach(var i in puntos)
            {
                Linea l = new Linea(X + 5, Y + 5, i.X + 5, i.Y + 5);
                l.Dibujate(elCanvas);
            }
        }
    }
}
