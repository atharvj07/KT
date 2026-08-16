import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//Searching Constellation
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		long W = 1000001;
		while(true){
			int m = sc.nextInt();
			if(m==0)break;
			long[][] star = new long[m][2];
			for(int i=0;i<m;i++){
				for(int j=0;j<2;j++){
					star[i][j] = sc.nextLong();
					if(i>0)star[i][j]-=star[0][j];
				}
			}
			Set<Long> set = new HashSet<Long>();
			int n = sc.nextInt();
			long[][] a = new long[n][2];
			for(int i=0;i<n;i++){
				for(int j=0;j<2;j++){
					a[i][j]=sc.nextLong();
				}
				set.add(a[i][0]*W+a[i][1]);
			}
			for(int i=0;i<n;i++){
				long bx = a[i][0];
				long by = a[i][1];
				boolean f = true;
				for(int j=1;j<m;j++){
					if(!set.contains((bx+star[j][0])*W+by+star[j][1])){
						f = false;
						break;
					}
				}
				if(f){
					System.out.println((bx-star[0][0])+" "+(by-star[0][1]));
					break;
				}
			}
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}