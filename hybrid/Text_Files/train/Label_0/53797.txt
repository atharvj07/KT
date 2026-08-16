import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		for(;;){
			int N=Integer.parseInt(cin.nextLine());
			if(N==0)break;
			
			int[][] a = new int[N][2];
			for(int i=0;i<N;i++){
				String[] s =cin.nextLine().split(" ");
				int[] b = new int[s.length-1];
				a[i][0]=Integer.parseInt(s[0]);
				int frame=1;
				for(int j=1;j<s.length;j++){
					b[j-1]=Integer.parseInt(s[j]);
				}
				for(int j=0;j<b.length;){
					if(frame==10){
						a[i][1]+=b[j];
						j++;
						continue;
					}
					a[i][1]+=b[j]+b[j+1];
					if(b[j]==10){
						a[i][1]+=b[j+2];
						j++;
					}
					else{
						if(b[j]+b[j+1]==10){
							a[i][1]+=b[j+2];
						}
						j+=2;

					}
					frame++;
				}
//				System.out.println(a[i][1]);
			}
			Arrays.sort(a,new Comparator<int[]>(){
				public int compare(int[] a,int[] b){
					if(a[1]==b[1]){
						return a[0]-b[0];
					}
					return b[1]-a[1];
				}
			});
			
			for(int i=0;i<N;i++){
				System.out.println(a[i][0]+ " " + a[i][1]);
			}
		}
	}
	
}