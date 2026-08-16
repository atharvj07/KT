import java.util.*;

public class Main {


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int d = sc.nextInt();
			long sum=0;
			for(int i=d; i<=600-d; i+=d) sum += d*i*i;
			System.out.println(sum);
		}
	}

}