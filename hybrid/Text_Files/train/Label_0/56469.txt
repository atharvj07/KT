import java.util.Scanner;


public class Main {
	
	public static int cal(int cur, int raw, int n, int m){
		int ret = 0;
		
		if(cur > m){
			return 0;
		}else if(!(cur < n)){
			ret += 1;
		}
		
		switch(raw){
		case 2:
			ret += cal(cur*2, 2, n, m);
		case 3:
			ret += cal(cur*3, 3, n, m);
		case 5:
			ret += cal(cur*5, 5, n, m);
		}
		
		return ret;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			final int n = sc.nextInt();
			
			if(n == 0){
				break;
			}
			
			final int m = sc.nextInt();
			
			System.out.println(cal(1,2,n,m));
		}
		
	}

}