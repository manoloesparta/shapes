using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Shapes;

namespace figuras
{
    class Circulo : Figura
    {
        public double radio { get; set; }
        private Ellipse c { get; set; }

        public Circulo(double radio, int PosX, int PosY) : base(1, "Circulo", PosX, PosY)
        {
            this.radio = radio;
            c = new Ellipse();
            c.Width = 2 * radio;
            c.Height = 2 * radio;
        }

        public static Figura rnd(int x, int y)
        {
            var randy = new Random(Guid.NewGuid().GetHashCode());
            double radio = randy.Next(15, 30);
            return new Circulo(radio, x, y);
        }

        public override void dibujate(Canvas miCanvas)
        {
            if (!miCanvas.Children.Contains(c))
            {
                c.Stroke = Brushes.Black;
                miCanvas.Children.Add(c);
            }

            c.Fill = relleno;
            Canvas.SetLeft(c,this.PosX);
            Canvas.SetTop(c, this.PosY);
        }

        public override void Animate(Canvas miCanvas)
        {
            base.Animate(miCanvas);
            var randy = new Random();
            if (this.PosX > miCanvas.ActualWidth - (this.radio * 2) || this.PosX < 0)
            {
                this.Dx *= -1;
                this.cambiarColor();
            }
            if (this.PosY > miCanvas.ActualHeight - (this.radio) * 2 || this.PosY < 0)
            {
                this.Dy *= -1;
                this.cambiarColor();
            }
            dibujate(miCanvas);
        }
    }
}
