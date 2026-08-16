import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			int m=sc.nextInt();
			int n1=sc.nextInt();
			int n2=sc.nextInt();
			if((n1==0&&n2==0)&&m==0) break;
			int[] data = new int[m];
			for(int i=0;i<m;++i){
				data[i]=sc.nextInt();
			}
			int num=n2-n1+1;
			int[] data2 = new int[num];
			for(int i=0;i<num;++i){
				data2[i]=data[n1-1+i]-data[n1+i];
			}
			int max=0,ans=0;
			for(int i=0;i<num;++i){
				if(max<=data2[i]){
					max=data2[i]; ans=i+n1;
				}
			}
			System.out.println(ans);
		}
	}
}
