using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Shapes;

namespace figuras
{
    class Diamante : Figura
    {
        public double height { get; set; }
        public double lado { get; set; }
        public double withd { get; set; }
        private Polygon p { get; set; }

        public Diamante(double height, double withd, int PosX, int PosY) : base(4, "Diamante", PosX, PosY)
        {
            this.height = height;
            this.withd = withd;
            lado = Math.Sqrt(Math.Pow(height, 2) + Math.Pow(withd, 2));
            p = new Polygon();
        }
        public static Figura rnd(int x, int y)
        {
            var randy = new Random(Guid.NewGuid().GetHashCode());
            double local_h = randy.Next(30, 60);
            double local_w = randy.Next(30, 60);
            return new Diamante(local_h, local_w, x, y);
        }

        public override void dibujate(Canvas miCanvas)
        {
            if (!miCanvas.Children.Contains(p))
            {
                p.Stroke = Brushes.Black;
                p.Points.Add(new Point(0, this.height / 2));
                p.Points.Add(new Point(this.withd / 2, 0));
                p.Points.Add(new Point(0, -1 * (this.height / 2)));
                p.Points.Add(new Point(-1 * (this.withd / 2), 0));
                miCanvas.Children.Add(p);
            }
            p.Fill = relleno;
            Canvas.SetLeft(p, this.PosX);
            Canvas.SetTop(p, this.PosY);
        }

        public override void Animate(Canvas miCanvas)
        {
            base.Animate(miCanvas);
            if (this.PosX > (miCanvas.ActualWidth - this.withd/2) || this.PosX < this.withd/2)
            {
                this.Dx *= -1;
                this.cambiarColor();
            }
            if(this.PosY > (miCanvas.ActualHeight - this.height/2) || this.PosY < this.height/2)
            {
                this.Dy *= -1;
                this.cambiarColor();
            }
            dibujate(miCanvas);
        }
    }
}
