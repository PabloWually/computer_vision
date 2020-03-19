
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
	//Nombre de la imagen que se va a cargar
	char NombreImagen[] = "ivvi.jpg";
	Mat imagen;

	//Cargamos la imagen y se comprueba que lo ha hecho correctamente
	imagen = imread(NombreImagen);
	if (!imagen.data) {
		cout << "Error al cargar la imagen: " << NombreImagen << endl;
		exit(1);
	}

	//Mostrar la imagen
	namedWindow("Original", WINDOW_AUTOSIZE);
	imshow("Original", imagen);

	//Esperar a pulsar una tecla
	waitKey(0);

	return 0;
}