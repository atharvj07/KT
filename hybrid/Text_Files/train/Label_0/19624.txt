// AOJ 0115
#include <iostream>
#include <cmath>

using namespace std;

typedef double Real;
const Real EPS = 1e-5;

struct plane{
	Real a, b, c, d;
	plane() {}
	plane(Real a, Real b, Real c, Real d) : a(a), b(b), c(c), d(d) {}
};

struct vect {
	Real x, y, z;
	vect(Real x = 0, Real y = 0, Real z = 0) : x(x), y(y), z(z) {}
	void add(vect& a){
		x += a.x;
		y += a.y;
		z += a.z;
	}
	void sub(vect& a){
		x -= a.x;
		y -= a.y;
		z -= a.z;
	}
	void mul(Real a){
		x *= a;
		y *= a;
		z *= a;
	}
	void div(Real a){
		x /= a;
		y /= a;
		z /= a;
	}
	Real dot(vect& a){
		return (x * a.x + y * a.y + z * a.z);
	}
	Real dot(plane a){
		return (x * a.a + y * a.b + z * a.c);
	}
	Real length(){
		return sqrt(x * x + y * y + z * z);
	}
	Real dist(vect& a){
		vect c = *this;
		c.sub(a);
		return c.length();
	}
	Real& access(int a){
		a %= 3;
		if (a == 0) return x;
		if (a == 1) return y;
		if (a == 2) return z;
		return x;
	}
	vect cross(vect& a){
		vect ret;
		vect u = *this, v = a;
		ret.x = u.y * v.z - u.z * v.y;
		ret.y = u.z * v.x - u.x * v.z;
		ret.z = u.x * v.y - u.y * v.x;
		return ret;
	}
	bool eq(vect& a){
		return x == a.x && y == a.y && z == a.z;
	}
};
ostream &operator<<(ostream &os, const vect &a) { os << "(" << a.x << ", " << a.y << ", " << a.z << ")"; return os; }

struct tri{
	vect p0, p1, p2;
	tri(vect a, vect b, vect c) : p0(a), p1(b), p2(c) {}
	vect normal(){
		Real a = ((p1.y - p0.y) * (p2.z - p0.z)) - ((p2.y - p0.y) * (p1.z - p0.z));
		Real b = ((p1.z - p0.z) * (p2.x - p0.x)) - ((p2.z - p0.z) * (p1.x - p0.x));
		Real c = ((p1.x - p0.x) * (p2.y - p0.y)) - ((p2.x - p0.x) * (p1.y - p0.y));
		vect ret(a, b, c);
		// cout << "ret : " << ret << ", length = " << ret.length() << endl;
		ret.div(ret.length());
		return ret;
	}
	Real area(){
		Real a, b, c, s;
		a = p0.dist(p1), b = p1.dist(p2), c = p2.dist(p0);
		s = (a + b + c) / 2;
		return sqrt(s * (s - a) * (s - b) * (s - c));
	}
};

bool intersect(vect n, vect A, vect B, vect v1, vect *ret)
{
	vect AP = v1; AP.sub(A);
	vect BP = v1; BP.sub(B);
	Real dot_APN = AP.dot(n), dot_BPN = BP.dot(n);

	if (abs(dot_APN) < EPS && abs(dot_BPN) < EPS){
		// cout << "double zero" << endl;
		return false;
	}
	else if ((dot_APN - EPS <= 0.0 && 0.0 <= dot_BPN + EPS) || (dot_BPN - EPS <= 0.0 && 0.0 <= dot_APN + EPS)){
		// RINPANA
	}
	else {
		// cout << "same side" << endl;
		return false;
	}

	vect AB = B; AB.sub(A);
	Real h = abs(dot_APN) / (abs(dot_APN) + abs(dot_BPN));
	// cout << "AP : " << AP << " BP : " << BP << endl;
	// cout << "dot_APN = " << dot_APN << ", dot_BPN = " << dot_BPN << endl;
	// cout << "AB : " << AB << endl;

	ret->x = A.x + (AB.x * h);
	ret->y = A.y + (AB.y * h);
	ret->z = A.z + (AB.z * h);

	return true;
}

int main()
{
	Real x, y, z;

	while (cin >> x){
		if (cin.eof()) break;
		cin >> y >> z;			vect uaz_(x, y, z);
		cin >> x >> y >> z;		vect enemy_(x, y, z);
		cin >> x >> y >> z;		vect v1_(x, y, z);
		cin >> x >> y >> z;		vect v2_(x, y, z);
		cin >> x >> y >> z;		vect v3_(x, y, z);

		tri barrier(v1_, v2_, v3_);

		vect n = barrier.normal();
		vect uaz = uaz_, v1 = v1_;
		vect v = uaz_;

		v.sub(enemy_);
		uaz.sub(v1);

		// cout << n << endl;

		bool ok = true;
		if (abs(v.dot(n)) < EPS){
			// cout << "zero" << endl;
		}
		else {
			// Real t = (uaz.dot(n)) / (v.dot(n));
			// // cout << "DEBUG ***" << t << " " << dst << endl;
			// if (t < 0){
			// 	// cout << "back" << endl;
			// 	ok = false;
			// }
			// else if (dst < t + EPS){
			// 	// cout << "over" << endl;
			// 	ok = false;
			// }

			vect inter;
			if (!intersect(n, uaz_, enemy_, v1_, &inter)){
				// NIKOMAKI
				// cout << "empty" << endl;
			}
			else {
				// cout << "intersect point : " << inter << endl;
				// Q, v1, v2
				Real a, b, c, s;
				a = inter.dist(v1_), b = v1_.dist(v2_), c = v2_.dist(inter);
				s = (a + b + c) / 2;
				Real T1 = sqrt(s * (s - a) * (s - b) * (s - c));
				// Q, v2, v3
				a = inter.dist(v2_), b = v2_.dist(v3_), c = v3_.dist(inter);
				s = (a + b + c) / 2;
				Real T2 = sqrt(s * (s - a) * (s - b) * (s - c));
				// Q, v3, v1
				a = inter.dist(v3_), b = v3_.dist(v1_), c = v1_.dist(inter);
				s = (a + b + c) / 2;
				Real T3 = sqrt(s * (s - a) * (s - b) * (s - c));
				// cout << T1 << " " << T2 << " " << T3 << " " << barrier.area() << endl;
				if ((T1 + T2 + T3) < barrier.area() + EPS){
					// inside
					ok = false;
				}
			}
		}
		if (ok){
			cout << "HIT" << endl;
		}
		else {
			cout << "MISS" << endl;
		}
	}

	return 0;
}