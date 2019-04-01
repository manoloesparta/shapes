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
    class Triangulo : Figura
    {
        public double lado { get; set; }
        private Polygon p { get; set; }

        public Triangulo(double lado, int PosX, int PosY) : base(3, "Triangulo Equilatero", PosX, PosY)
        {
            this.lado = lado;
            p = new Polygon();
        }

        public static Figura rnd(int x, int y)
        {
            var randy = new Random(Guid.NewGuid().GetHashCode());
            double lado = randy.Next(30, 60);
            return new Triangulo(lado, x, y);
        }

        public override double area()
        {

            return (lado * altura) / 2; ;
        }

        public override double Perimetro()
        {
            return lado * 3;
        }

        public double altura
        {

            get
            {
                double lado2 = lado / 2;
                double suma = Math.Pow(lado, 2) + Math.Pow(lado2, 2);
                double altura = Math.Sqrt(suma);
                return altura;
            }
        }

        public override void dibujate(Canvas miCanvas)
        {
            if (!miCanvas.Children.Contains(p))
            {
                p.Points.Add(new Point(lado / 2, 0));
                p.Points.Add(new Point(0, altura));
                p.Points.Add(new Point(lado, altura));
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
            if (this.PosX > miCanvas.ActualWidth - this.lado || this.PosX < 0)
            {
                this.Dx *= -1;
                this.cambiarColor();
            }
            if (this.PosY > miCanvas.ActualHeight - this.altura || this.PosY < 0)
            {
                this.Dy *= -1;
                this.cambiarColor();
            }
            dibujate(miCanvas);
        }
    }
}
