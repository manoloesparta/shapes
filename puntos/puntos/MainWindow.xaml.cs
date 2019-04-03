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

namespace puntos
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        Random randy = new Random();
        List<Punto> puntos = new List<Punto>();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void CanvasClick(object sender, MouseButtonEventArgs e)
        {
            var clickeo = e.GetPosition(elCanvas);
            Punto p = new Punto(clickeo.X, clickeo.Y);
            p.Dibujate(elCanvas);
            p.Relacionar(elCanvas, puntos);
            puntos.Add(p);
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            puntos.Clear();
            elCanvas.Children.Clear();
        }
    }
}
