
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}

	Scanner sc = new Scanner(System.in);

	void run() {
		for(;;){
			long n = sc.nextLong();
			if(n ==0 ){
				break;
			}
			char[] ch = ("1" + sc.next()).toCharArray();
			long d = decode(ch);
			long e = 0;
			long bound = (1L<<53);
			long now = d;
			long nowd = d;
			long remain = n;
//			System.out.println(encode(e,d));
//			System.out.println(d);
			for(;;){
				if(nowd == 0){
					break;
				}
				long next = (bound - now);
				long times = ((next - 1)/ nowd)+1;
//				System.out.println(bound+" "+next + " "+times);
				if(remain < times){
					now += nowd * remain;
					break;
				}
				
				now += nowd * times;
				now >>= 1;
				nowd >>= 1;
				e++;
				remain -= times;
			}
			System.out.println(encode(e,now));
		}	
	}
	String encode(long e,long now){
		
		String ee = String.format("%012d", 0)+Long.toBinaryString(e);
		String dd = String.format("%052d", 0)+Long.toBinaryString(now);
		ee = ee.substring(ee.length()-12);
		dd = dd.substring(dd.length()-52);
		return ee + dd;
	}
	long decode(char[] ch2){
		long res = 0;
		for(int i =0 ; i < ch2.length;i++){
			res *= 2;
			res += ch2[i] - '0';
		}
		return res;
	}
	
	
}

