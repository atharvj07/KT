// OBツ嘉ッツ嘉債宿2011 Day3 I : White Bird

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const double EPS = 1e-8;

int main(){
	int N, V, X, Y;
	int L[50], B[50], R[50], T[50];
	while(cin >> N >> V >> X >> Y){
		vector<double> vd;
		int low = Y, high = 1000000007;
		for(int i=0;i<N;i++){
			cin >> L[i] >> B[i] >> R[i] >> T[i];
			L[i] = min(L[i], X);
			R[i] = min(R[i], X);
			if(L[i]<=X&&X<=R[i]&&B[i]>=high) high = min(high, B[i]);
		}
		bool clear = false;
		for(int i=1;i<900000;i++){
			double angle = (double)i/10000/180*acos(-1);
			double vx = V*cos(angle);
			double vy = V*sin(angle);
			bool ok = true;
			for(int j=0;j<N;j++){
				double my = vy*(L[j]/vx) - 4.9*(L[j]/vx)*(L[j]/vx);
				double My = vy*(R[j]/vx) - 4.9*(R[j]/vx)*(R[j]/vx);
				if(my > My) swap(my, My);
				if(L[j]+EPS < vx*vy/9.8 && vx*vy/9.8 < R[j]-EPS)
					My = vy*(vy/9.8) - 4.9*(vy/9.8)*(vy/9.8);
				if(min(My, (double)T[j]) - max(my, (double)B[j]) > EPS) ok = false;
			}
			if(!ok) continue;
			double y = vy*(X/vx) - 4.9*(X/vx)*(X/vx);
			if(low-EPS < y && y < high+EPS) clear = true;			
		}
		cout << (clear ? "Yes" : "No") << endl;
	}
}