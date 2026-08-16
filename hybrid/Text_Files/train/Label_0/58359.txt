import java.util.Scanner;

public class Solution {
	
	public static void main(String[] args) {

		/*
		 * 8
13 -2 -11 5 6 2 -11 -2
		 */
		Solution sl=new Solution();
		Scanner scan = new Scanner(System.in);
		
		//System.out.println(getPows(100, 4)); if(true)return;
		 
		int t = scan.nextInt();
		
		outer:while(t-->0) {
			int n =scan.nextInt();
			int[] arr =new int[n];
			
			for(int i=0;i<n;i++) {
				arr[i]=scan.nextInt();
			}
			boolean flag=false;
			boolean flag2=false;
			for(int i=0;i<n;i++) {
				if(i+1==arr[i]) flag=true;
				
				if(flag && flag2 && i+1!=arr[i]) {
					System.out.println(2);
					continue outer;
				}
				
				if(i+1!=arr[i]) {
					flag2=true;
					flag=false;
				}
			}
			if(!flag2) {
				System.out.println(0);
			}else {
				System.out.println(1);
			}
		}
		
		
		scan.close();
	}
	
	
	/*
	 * static final Random random=new Random();
	 * 
	 * static void ruffleSort(int[] a) { int n=a.length; //shuffle, then sort for
	 * for(int i=0; i<n; i++) { int oi=random.nextInt(n), temp=a[oi]; a[oi]=a[i];
	 * a[i]=temp; } Arrays.sort(a); }
	 */
	 
	
}