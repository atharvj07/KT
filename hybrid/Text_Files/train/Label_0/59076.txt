import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		
		int[][] e = new int[n][5];
		long sum = 0;
		long dmg = 0;
		boolean flag = false;
		for(int i=0;i<n;i++){
			e[i][0] = sc.nextInt();
			e[i][1] = sc.nextInt() - c;
			if(e[i][1]<=0) e[i][1] = 0;
			e[i][2] = b - sc.nextInt();
			if(e[i][2]<=0) e[i][2] = 0;
			if(e[i][1]>0 && e[i][2]==0) flag = true;
			e[i][3] = sc.nextInt();
			e[i][4] = -1;
			if(e[i][2]!=0){
				e[i][4] = e[i][0]/e[i][2];
				if(e[i][0]%e[i][2]!=0) e[i][4]++;
			}
			sum += e[i][1];
			if(e[i][3]>d) dmg+=e[i][1];
		}
		
		if(flag==false){
			Arrays.sort(e, new Comparator<int[]>(){
				public int compare(int[] o1, int[] o2) {
					if(((double)o2[1]/o2[4])-((double)o1[1]/o1[4])>0) return 1;
					else return -1;
				}
			});	
			
			dmg -= sum;
			for(int i=0;i<n;i++){
				dmg += e[i][4]*sum;
				sum -= e[i][1];
			}
			if(dmg>=a || dmg<0) flag = true;
		}
		
		if(flag==true) System.out.println(-1);
		else System.out.println(dmg);
	}	
}