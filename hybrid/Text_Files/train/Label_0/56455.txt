import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int maxpri = 10000;
		
		int[] pri = new int[maxpri + 10000];
		for(int i=2;i<=maxpri;i++){
			pri[i] = i;
		}
		for(int i=2;i<=maxpri;i++){
			for(int j=i+i;j<=maxpri;j+=i){
					pri[j]=0;
			}
		}

		while(sc.hasNext()){
			int n = sc.nextInt();
			int count=0;
			for(int i=2;i<n;i++){
				if(pri[i]>0 && pri[n+1-i]>0) count++;
			}
			System.out.println(count);
		}
	}
	
}