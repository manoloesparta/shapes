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
    class Trapecio : Figura
    {
        public double basemayor { get; set; }
        public double basemenor { get; set; }
        public double altura { get; set; }
        public double lateral { get; set; }
        private Polygon p { get; set; }

        public Trapecio(double basemayor, double basemenor, double altura, double lateral, int PosX, int PosY) : base(4, "Traepecio", PosX, PosY)
        {
            this.basemayor = basemayor;
            this.basemenor = basemenor;
            this.lateral = lateral;
            this.altura = altura;
            p = new Polygon();
        }

        public static Figura rnd(int x, int y)
        {
            var randy = new Random(Guid.NewGuid().GetHashCode());
            double basemayor = randy.Next(20, 40);
            double basemenor = randy.Next(50, 70);
            double altura = randy.Next(30, 60);
            double lateral = randy.Next(30, 60);
            return new Trapecio(basemayor, basemenor, altura, lateral, x, y);
        }

        public override void dibujate(Canvas miCanvas)
        {
            if (!miCanvas.Children.Contains(p))
            {
                p.Points.Add(new Point(basemenor / 2, altura / 2));
                p.Points.Add(new Point(basemayor / 2, -1 * altura / 2));
                p.Points.Add(new Point(-1 * basemayor / 2, -1 * altura / 2));
                p.Points.Add(new Point(-1 * basemenor / 2, altura / 2));
                p.Stroke = Brushes.Black;
                miCanvas.Children.Add(p);
            }
            p.Fill = relleno;
            Canvas.SetLeft(p, this.PosX);
            Canvas.SetTop(p, this.PosY);
        }

        public override void Animate(Canvas miCanvas)
        {
            base.Animate(miCanvas);
            if (this.PosX > miCanvas.ActualWidth - (this.basemayor)|| this.PosX < this.basemayor)
            {
                this.Dx *= -1;
                this.cambiarColor();
            }
            if(this.PosY > miCanvas.ActualHeight - (this.altura/2) || this.PosY < this.altura/2)
            {
                this.Dy *= -1;
                this.cambiarColor();
            }
            dibujate(miCanvas);
        }
    }
}
