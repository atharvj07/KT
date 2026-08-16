import java.util.Arrays;
import java.util.Scanner;


public class C551 {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		int[] a = new int[n];
				
		for(int i=0;i<n;++i){
			a[i]=in.nextInt();					
		}
		
		long high = (long) 1e15;
		long low = 0;
		while(high>=low){
//			System.out.println(low+" "+high);
			long mid = (low+high)/2;
			if(canSolve(Arrays.copyOf(a, a.length),mid,m)){
				high = mid-1;
			}else{
				low = mid+1;
			}
			
		}
											
		System.out.println(""+low);				
	}
	
	public static boolean canSolve(int[] a, long t, int m){
		int i = 0;
		for(int s=0;s<m;++s){						
			long curT= t-(i+1);
			while(curT>0&&i<a.length){
				if(curT>=a[i]){					
					curT-=a[i];
					a[i]=0;
					++i;
					curT--;
				}else{
					a[i]-=curT;
					curT = 0;
				}
			}
		}
		for(i=0;i<a.length;++i){
			if(a[i]!=0){
				return false;
			}
		}
//		System.out.println("can solve for "+t);
		return true;
	}

}
