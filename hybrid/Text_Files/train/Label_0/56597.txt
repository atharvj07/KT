import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			int m = sc.nextInt();
			if(m==0)break;
			int[] a = new int[m+1];
			int[] b = new int[m+1];
			for(int i=1;i<=m;i++){
				a[i] = sc.nextInt();
				b[i] = sc.nextInt();
			}
			int[][] p = new int[m+1][1001];
			p[0][0] = 1;
			for(int i=1;i<=m;i++){
				for(int k=0;k<1001;k++){
					for(int s=0;s<=b[i];s++){
						if(k-a[i]*s<0)break;
						p[i][k] += p[i-1][k-s*a[i]];
					}
				}
			}
			int g = sc.nextInt();
			while(g--!=0)System.out.println(p[m][sc.nextInt()]);
		}
	}
}