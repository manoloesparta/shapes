using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Media;

namespace figuras
{
    abstract class Figura
    {
        public int lados { get; }
        public string nombre { get; set; }
        public int PosX { get; set; }
        public int PosY { get; set; }
        public int Dx { get; set; }
        public int Dy { get; set; }
        public Brush relleno { get; set; }

        public Figura(int lados, string nombre, int PosX, int PosY)
        {
            this.lados = lados;
            this.nombre = nombre;
            this.PosX = PosX;
            this.PosY = PosY;
        }

        public abstract double Perimetro();
        public abstract double area();
        public abstract void dibujate(Canvas miCanvas);

        public virtual void Animate(Canvas miCanvas)
        {
            PosX += Dx;
            PosY += Dy;
        }

        public void cambiarColor()
        {
            var randy = new Random();
            this.relleno = new SolidColorBrush(Color.FromRgb((byte)randy.Next(256), (byte)randy.Next(256), (byte)randy.Next(256)));
        }
    }
}
