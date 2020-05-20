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
	imagen = cv::imread(NombreImagen);
	if (!imagen.data) {
		cout << "Error al cargar la imagen: " << NombreImagen << endl;
		exit(1);
	}

	//drawRec(imagen);
	int sum = suma(2, 3);
	cout << "Error al cargar la imagen: " << sum << endl;
	//Esperar a pulsar una tecla
	cv::waitKey(0);
	return 0;
}

int suma(int a, int b) {
	return a + b;
}

void drawRec(Mat image) {
	int i, j;
	for (i = image.rows / 4; i < 3 * image.rows / 4; ++i) {
		for (j = image.cols / 4; j < 3 * image.cols / 4; ++j) {
			image.at<Vec3b>(Point(j, i)) = Vec3b(0, 0, 0);
		}
	}

	//Mostrar la imagen
	namedWindow("Original", WINDOW_AUTOSIZE);
	imshow("Original", image);

	//Guardar el resultado
	imwrite("Resultado.jpg", image);
}

