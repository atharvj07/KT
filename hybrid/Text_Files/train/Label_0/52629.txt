import java.util.Arrays;
import java.util.Scanner;
public class Main {

	public static void main(String[] args){
		Scanner stdIn=new Scanner(System.in);
		int N=stdIn.nextInt();
		int A[]=new int[N];
		int B[]=new int[N];
		int C[]=new int[N];
		int z=0,y=0,x=0,w=0;
		long m=0;
		while(z<N){
			A[z]=stdIn.nextInt();
			z++;
		}z=0;
		while(z<N){
			B[z]=stdIn.nextInt();
			m+=A[z]-B[z];
			if(A[z]-B[z]>0){
				C[y]=A[z]-B[z];
				y++;
			}
			if(A[z]-B[z]<0){
				x++;
			}
			z++;
		}z=0;
		if(x==0)
			System.out.println(0);
		else
			if(m<0)
				System.out.println(-1);
			else{
				Arrays.sort(C);
				while(z<N){
					m-=C[z];
					if(C[z]!=0)
						w++;
					if(m<=0)
						break;
					z++;
				}
				if(m<0)
					w-=1;
				System.out.println(x+(y-w));
			}
	}
}