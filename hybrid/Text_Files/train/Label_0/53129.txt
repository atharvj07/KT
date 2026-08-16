import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		while(true){
			int n = stdIn.nextInt();
			if(n==0){
				return;
			}
			String[] l = new String[n];
			double[] eft = new double[n];
			for(int i=0;i<n;i++){
				l[i] = stdIn.next();
				int p = stdIn.nextInt();
				int ac = stdIn.nextInt();
				ac += stdIn.nextInt();
				ac += stdIn.nextInt();
				int d = stdIn.nextInt();
				int e = stdIn.nextInt();
				int f = stdIn.nextInt();
				int s = stdIn.nextInt();
				int m = stdIn.nextInt();
				double sell = f*s*m-p;
				int time = ac+(d+e)*m;
				eft[i] = sell/time;
			}
			for(int i=0;i<n;i++){
				int max = i;
				for(int j=i+1;j<n;j++){
					if(Math.abs(eft[max]-eft[j])<0.0000000001){
						if(l[max].compareTo(l[j])>0){
							max = j;
						}
					}
					else if(eft[max]<eft[j]){
						max = j;
					}
				}
				double tmp1 = eft[i];
				eft[i] = eft[max];
				eft[max] = tmp1;
				String tmp2 = l[i];
				l[i] = l[max];
				l[max] = tmp2;
			}
			for(int i=0;i<n;i++){
				System.out.println(l[i]);
			}
			System.out.println("#");
		}
	}
}