import java.util.Scanner;

public class B_Mancala {
	
	public static long tr(long[] arr, int pos) {
		long cor = arr[pos] / 14;
		long d = arr[pos]%14;
		arr[pos] = 0;
		long sum = 0;
		int i = pos+1;
		while(d>0) {
			if (i==14) {
				i =0;
			}
			arr[i]++;
			d--;
			i++;
		}
		for(int g = 0;g<14;g++) {
			arr[g]+=cor;
			if( arr[g]%2==0) {
				sum+=arr[g];
			}
		}
		return sum;
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		long[] m = new long[14];
		for(int i=0;i<14;i++) {
			m[i] = scan.nextInt();
		}
		scan.close();
		long answ = 0;
		for (int i=0;i<14;i++) {
			if (m[i]==0) continue;
			answ = Math.max(tr(m.clone(),i ),answ);
		}
		System.out.print(answ);
	}
}