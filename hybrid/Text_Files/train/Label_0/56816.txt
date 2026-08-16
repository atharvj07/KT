import static java.lang.Math.*;
import java.util.Scanner;

//Tetrahedra
public class Main{

	double EPS = 1e-10;
	double det(double[][] A){
		int n = A.length;
		double res = 1;
		for(int i=0;i<n;i++){
			int pivot = i;
			for(int j=i+1;j<n;j++)if(abs(A[j][i])>abs(A[pivot][i]))pivot = j;
			swap(A, pivot, i);
			res *= A[i][i] * (i!=pivot?-1:1);
			if(abs(A[i][i])<EPS)break;
			for(int j=i+1;j<n;j++)for(int k=n-1;k>=i;k--)A[j][k]-=A[i][k]*A[j][i]/A[i][i];
		}
		return res;
	}
	void swap(double[][] A, int a, int b){
		int n = A[a].length;
		for(int i=0;i<n;i++){
			double t = A[a][i];
			A[a][i] = A[b][i];
			A[b][i] = t;
		}
	}
	
	int[] l;
	boolean tri(int a, int b, int c){
		int m = max(l[a], max(l[b], l[c]));
		return m < l[a]+l[b]+l[c]-m;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt();
			if(n==0)break;
			l = new int[n];
			for(int i=0;i<n;i++)l[i]=sc.nextInt();
			double max = 0;
			for(int a=0;a<n;a++){
				for(int b=0;b<n;b++){
					if(a==b)continue;
					for(int c=0;c<n;c++){
						if(a==c||b==c)continue;
						for(int p=0;p<n;p++){
							if(a==p||b==p||c==p||!tri(a, b, p))continue;
							for(int q=0;q<n;q++){
								if(a==q||b==q||c==q||p==q||!tri(a, c, q))continue;
								for(int r=0;r<n;r++){
									if(a==r||b==r||c==r||p==r||q==r||!tri(b, c, r)||!tri(p, q, r))continue;
									double[][] A = {{0, l[p]*l[p], l[q]*l[q], l[a]*l[a], 1},
											{l[p]*l[p], 0, l[r]*l[r], l[b]*l[b], 1},
											{l[q]*l[q], l[r]*l[r], 0, l[c]*l[c], 1},
											{l[a]*l[a], l[b]*l[b], l[c]*l[c], 0, 1},
											{1, 1, 1, 1, 0}
									};
									max = Math.max(max, det(A)/288);
								}
							}
						}
					}
				}
			}
			System.out.printf("%.8f\n", Math.sqrt(max));
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}