using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;

namespace figuras
{
    public partial class MainWindow : Window
    {
        List<Figura> figuritas;
        DispatcherTimer elTimer;

        public MainWindow()
        {
            InitializeComponent();
            figuritas = new List<Figura>();
            elTimer = new DispatcherTimer();
            elTimer.Interval = new TimeSpan(10000);
            elTimer.Tick += MueveFiguras;
        }

        private void MueveFiguras(object sender, EventArgs e)
        {
            foreach(var fig in figuritas)
            {
                fig.Animate(theCanvas);
            }
        }

        private void Grid_Loaded(object sender, RoutedEventArgs e)
        {
            var randy = new Random();

            for (int i = 0; i < 100; i++)
            {
                int k = randy.Next(1, 6);

                int canvasWidth = (int)theCanvas.ActualWidth;
                int canvasHeight = (int)theCanvas.ActualHeight;

                int x = randy.Next(canvasWidth / 20, canvasWidth - (canvasWidth / 11));
                int y = randy.Next(canvasHeight / 15, canvasHeight - (canvasHeight / 7));

                switch (k)
                {
                    case 1:
                        figuritas.Add(Circulo.rnd(x, y));
                        break;
                    case 2:
                        figuritas.Add(Diamante.rnd(x, y));
                        break;
                    case 3:
                        figuritas.Add(Triangulo.rnd(x, y));
                        break;
                    case 4:
                        figuritas.Add(Rectangulo.rnd(x, y));
                        break;
                    case 5:
                        figuritas.Add(Trapecio.rnd(x, y));
                        break;
                }

                int temPosX = randy.Next(-3, 4);
                while(temPosX == 0) temPosX = randy.Next(-3, 4);
                figuritas[i].Dx = temPosX;

                int temPosY = randy.Next(-3, 4);
                while (temPosY == 0) temPosY = randy.Next(-3, 4);
                figuritas[i].Dy = temPosY;

                figuritas[i].relleno = new SolidColorBrush(Color.FromRgb((byte)randy.Next(256), (byte)randy.Next(256), (byte)randy.Next(256)));
            }
            DibujaTodas();
            elTimer.Start();
        }

        public void DibujaTodas()
        {
            var randy = new Random();

            foreach (var figura in figuritas)
            {
                figura.dibujate(theCanvas);
            }
        }
    }
}
