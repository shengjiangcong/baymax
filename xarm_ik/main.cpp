#include <iostream>
#include "robcprobot_arm6DOFik.h"

using namespace std;

int main()
{
	const double PI = 3.141592653;
	float alength[6] = { 53, 284.5, 80, 0, 0, 77 };//DH Table -a
	float alpha[6] = { PI / 2, 0, PI / 2, -PI / 2, PI / 2, 0 };//DH Table -alpha
	float dlength[6] = { 267, 0, 0, 342, 0, 96.5 };//DH Table -d
	float theta0[6] = { 0 };//DH Table -theta
	float angleOffset[6] = { 0, 0, -PI / 2, 0, -PI / 2, 0};
	float highlim[6] = { 2 * PI, 2 * PI, 2 * PI, 2 * PI, 2 * PI, 2 * PI };
	float lowlim[6] = { -2 * PI, -2 * PI, -2 * PI, -2 * PI, -2 * PI, -2 * PI };
	float JointWeight[6] = { 1, 0.6, 0.6, 0.3, 0.3, 0.3 };

	robc_ARM6DOF_set_geometry(alength, alpha, dlength, theta0);
	robc_ARM6DOF_set_angleoffset(angleOffset);
	robc_ARM6DOF_set_movelim(highlim, lowlim);
	robc_ARM6DOF_set_modle(0);
	robc_ARM6DOF_set_jointweight(JointWeight);
	float dest[6] = { 0.8, -0.44, -1.23, 2.24, 2.25, 0};//0  0  -1.58  0  1.57  0
	dest[1] = -1 * dest[1];
	dest[2] = -1 * dest[2] - 1.58;
	dest[4] = -1 * dest[4] + 1.57;


	//d1 = j1
	//d2 = -j2
	//d3 = -1.58 - j3
	//d4 = j4
	//d5 = 1.57 - j5
	robc_ARM6DOF_Anno_kicalc(dest);
	/*float dest1[6] = { 225, 0, 460, 0, 0, -3.1415926 };

	robc_ARM6DOF_set_jointval(dest);
	robc_ARM6DOF_set_modle(0);

	cout << robc_ARM6DOF_Anno_ikcalc(dest1) << endl;*/

	return 0;
}