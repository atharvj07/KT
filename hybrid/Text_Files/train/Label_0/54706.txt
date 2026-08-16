import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[] a=new int[4801];
		int[] flag= {0,0,0,0,0,0,0,0,0};
		int cnt=0;
		for(int i=0;i<n;i++) {
			a[i]=sc.nextInt();
			if(3200<=a[i]) {
				flag[8]++;
				continue;
			}
			else if(2800<=a[i]) {
				flag[7]=1;
				continue;
			}
			else if(2400<=a[i]) {
				flag[6]=1;
				continue;
			}
			else if(2000<=a[i]) {
				flag[5]=1;
				continue;
			}
			else if(1600<=a[i]) {
				flag[4]=1;
				continue;
			}
			else if(1200<=a[i]) {
				flag[3]=1;
				continue;
			}
			else if(800<=a[i]) {
				flag[2]=1;
				continue;
			}
			else if(400<=a[i]) {
				flag[1]=1;
				continue;
				
			}
			else if(1<=a[i]) {
				flag[0]=1;
				continue;
			}
		}
		for(int i=0;i<8;i++) {
			if(flag[i]==1)	cnt++;
		}
		
		if(flag[8] == 0)	System.out.println(cnt+" "+cnt);	
		else if(cnt==0) {
			if(flag[8]+cnt <=8)	System.out.println(1 +" "+(cnt+flag[8]));
			else		System.out.println(1 + " " + 8);
		}
		else {
			System.out.println(cnt+" "+(cnt+flag[8]));
		}
		
	}

}