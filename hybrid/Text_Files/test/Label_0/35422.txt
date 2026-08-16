import java.util.Scanner;

public class Main {
	
	static int d;
	static double EPS=0.00000001;
	static double[] ans=new double[6];
	static double[] v=new double[8];
	
	static boolean check(int ans1, int ans2) {
		double sum1=0, sum2=0;
		int a=0;
		//double[] v=new double[d+3];
		//System.out.println("ans1="+ans1+" ans2="+ans2);
		for(int i=0; i<=d; i++) {
			sum1+=ans[i]*(Math.pow((ans1),(d-i)));
			sum2+=ans[i]*(Math.pow((ans2),(d-i)));
		}
		//System.out.println("sum1="+sum1+" sum2="+sum2);
		if(sum1!=v[ans1] && sum2>=v[ans2]-0.00001 && sum2<=v[ans2]+0.00001) {
			a=ans1;
			System.out.println(a);
			return true;
		}
		if(sum1>=v[ans1]-0.00001 && sum1<=v[ans1]+0.00001 && sum2!=v[ans2]) {
			a=ans2;
			System.out.println(a);
			return true;
		}
		return false;
	}
	
	static boolean gauss(double[][] A) {
		
//		for(int i=0; i<=d; i++) {
//			for(int j=0; j<=d+1; j++) {
//				System.out.print(A[i][j]);
//				if(j!=d+1) System.out.print(" ");
//			}
//			System.out.println();
//		}
		
		for(int i=0; i<=d; i++) {
			int pivot=i;
			for(int j=i; j<=d; j++) {
				if(Math.abs(A[j][i])>Math.abs(A[pivot][i])) {
					pivot=j;
				}
			}
			
			//System.out.println("pivot="+pivot);
			
			for(int j=0; j<=d+1; j++) {
				double a=A[i][j];
				A[i][j]=A[pivot][j];
				A[pivot][j]=a;
			}
			
//			for(int x=0; x<=d; x++) {
//				for(int j=0; j<=d+1; j++) {
//					System.out.print(A[x][j]);
//					if(j!=d+1) System.out.print(" ");
//				}
//				System.out.println();
//			}
			
			if(Math.abs(A[i][i])<EPS) {
				return false;
			}
			
			for(int j=i+1; j<=d+1; j++) {
				A[i][j]/=A[i][i];
			}
			A[i][i]/=A[i][i];//基準値を1にする
			
			for(int j=0; j<=d; j++) {
				if(i!=j) {
					for(int k=i+1; k<=d+1; k++) {
						A[j][k]-=A[j][i]*A[i][k];
						//System.out.println("A["+j+"]["+i+"]="+A[j][i]+"*A["+i+"]["+k+"]="+A[i][k]);
					}
					A[j][i]-=A[j][i]*A[i][i];
				}
			}
			
//			System.out.println();
//			for(int x=0; x<=d; x++) {
//				for(int j=0; j<=d+1; j++) {
//					System.out.print(A[x][j]);
//					if(j!=d+1) System.out.print(" ");
//				}
//				System.out.println();
//			}
			
		}
		
		for(int i=0; i<=d; i++) {
			ans[i]=A[i][d+1];
			//System.out.println("ans["+i+"]="+ans[i]);
		}
		return true;
	}
	
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){
			while(sc.hasNext()) {
				d=sc.nextInt();
				if(d==0) break;
				double[][] B=new double[d+2][d+2];
				int a=0;
				//double[] v=new double[d+3];
				double[] copy=new double[d+1];
				for(int i=0; i<=d+2; i++) {
					v[i]=sc.nextDouble();
				}
				
				int ans1=0, ans2=0;
				boolean tf=false;
				for(int i=0; i<=d+2; i++) {//除く点1つ目
					for(int ii=i+1; ii<=d+2; ii++) {//除く点2つ目
//						System.out.println("------------------------------------");
//						System.out.println("i="+i+" ii="+ii);
						int count=0;
						for(int k=0; k<=d+2; k++) {
							if(k==i || k==ii) continue;
							for(int kk=0; kk<=d; kk++) {
								B[count][kk]=Math.pow(k, (d-kk));
							}
							copy[count++]=v[k];
						}
						for(int j=0; j<=d; j++) {//0～d+2の中からd+1コ選ぶ
							B[j][d+1]=copy[j];
						}
						if(gauss(B)) {
							ans1=i;
							ans2=ii;
							//System.out.println("ans1="+ans1+" ans2="+ans2);
							if(check(ans1, ans2)) {
								tf=true;
								break;
							}
						}
					}
					if(tf) {
						break;
					}
				}
				
			}
			
			
		}
	}
}
