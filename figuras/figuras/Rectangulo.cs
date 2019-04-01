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
    class Rectangulo : Figura
    {
        public double baseRect { get; set; }
        public double alturaRect { get; set; }
        public Rectangle r { get; set; }

        public Rectangulo(double baseRect, double alturaRect, int PosX, int PosY) : base(4, "Rectangulo", PosX, PosY)
        {
            this.baseRect = baseRect;
            this.alturaRect = alturaRect;
            r = new Rectangle();
        }

        public static Figura rnd(int x, int y)
        {
            var randy = new Random(Guid.NewGuid().GetHashCode());
            double _base = randy.Next(30, 60);
            double altura = randy.Next(30, 60);
            return new Rectangulo(_base, altura, x, y);
        }

        public override double area()
        {
            return baseRect * alturaRect;
        }

        public override double Perimetro()
        {
            return (2 * baseRect) + (2 * alturaRect);
        }

        public override void dibujate(Canvas miCanvas)
        {
            if (!miCanvas.Children.Contains(r))
            {
                r.Height = alturaRect;
                r.Width = baseRect;
                r.Stroke = Brushes.Black;
                miCanvas.Children.Add(r);
            }
            r.Fill = relleno;
            Canvas.SetLeft(r, this.PosX);
            Canvas.SetTop(r, this.PosY);
        }

        public override void Animate(Canvas miCanvas)
        {
            base.Animate(miCanvas);
            if(this.PosX > miCanvas.ActualWidth - this.baseRect || this.PosX < 0)
            {
                this.Dx *= -1;
                this.cambiarColor();
            }
            if(this.PosY > miCanvas.ActualHeight - this.alturaRect || this.PosY < 0)
            {
                this.Dy *= -1;
                this.cambiarColor();
            }
            dibujate(miCanvas);
        }
    }
}
