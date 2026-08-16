import java.util.*;

class Main {
	public static void main(String args[]){
		Scanner in = new Scanner(System.in);
		while(true){
			int n = 1000 - in.nextInt();
			if(n==1000) return ;
			int cnt = 0;
			if(n>=500){
				cnt++;
				n -= 500;
			}
			if(n>=100){
				cnt += n/100;
				n %= 100;
			}
			if(n>=50){
				cnt++;
				n -= 50;
			}
			if(n>=10){
				cnt += n/10;
				n %= 10;
			}
			if(n>=5){
				cnt++;
				n -= 5;
			}
			cnt += n;
			System.out.println(cnt);
		}
	}
}