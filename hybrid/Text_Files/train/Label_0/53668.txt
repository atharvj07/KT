import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[] simen=new int[1000];
	static int[] kisu_simen=new int[48];
	static int INF=1000000007;
	public static void main(String[] args) {
		for(int i=0; i<200; i++) {
			int tmp=(i+1)*(i+2)*(i+3)/6;
			for(int j=0; j<5; j++) {
				simen[i*5+j]=tmp;
			}
		}
		int num=0;
		int counter=0;
		while(true) {
			if(counter>=47) {
				break;
			}
			else {
				if(num*(num+1)*(num+2)/6%2==1) {
					kisu_simen[counter]=num*(num+1)*(num+2)/6;
					counter++;
				}
			}
			num++;
		}
		int[] pollock=new int[1000002];
		int[] pollock_k=new int[1000002];
		Arrays.fill(pollock,INF);
		Arrays.fill(pollock_k,INF);
		pollock[0]=0;
		pollock_k[0]=0;
		int sum=0;
		for(int i=0; i<1000; i++) {
			for(int j=0; j<=Math.min(sum,1000001); j++) {
				if(pollock[j]<INF) {
					if(j+simen[i]<=1000000) {
						pollock[j+simen[i]]=Math.min(pollock[j+simen[i]], pollock[j]+1);
					}
				}
			}
			sum+=simen[i];
		}
		for(int i=0; i<48; i++) {
			for(int j=0; j<=1000000; j++) {
				if(j-kisu_simen[i]>=0) {
					pollock_k[j]=Math.min(pollock_k[j], pollock_k[j-kisu_simen[i]]+1);
				}
			}
		}
		Scanner sc = new Scanner(System.in);
		while(true) {
			int input=sc.nextInt();
			if(input==0) {
				System.exit(0);
			}
			else {
				System.out.println(pollock[input]+" "+pollock_k[input]);
			}
		}
	}
}
