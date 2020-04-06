#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
	//Nombre de la imagen que se va a cargar
	char NombreImagen[] = "ivvi.jpg";
	Mat imagen;
	int i, j;

	//Cargamos la imagen y se comprueba que lo ha hecho correctamente
	imagen = cv::imread(NombreImagen);
	if (!imagen.data) {
		cout << "Error al cargar la imagen: " << NombreImagen << endl;
		exit(1);
	}

	for (i = imagen.rows / 4; i < 3 * imagen.rows / 4; ++i) {
		for (j = imagen.cols / 4; j < 3 * imagen.cols / 4; ++j) {
			imagen.at<Vec3b>(Point(j, i)) = Vec3b(0, 0, 0);
		}
	}

	//Mostrar la imagen
	namedWindow("Original", WINDOW_AUTOSIZE);
	imshow("Original", imagen);

	//Guardar el resultado
	imwrite("Resultado.jpg", imagen);

	//Esperar a pulsar una tecla
	cv::waitKey(0);
	return 0;
}