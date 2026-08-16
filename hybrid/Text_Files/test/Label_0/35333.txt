import java.util.*;
public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}
	public Main() {
		while(true){
			int x = in.nextInt();
			int y = in.nextInt();
			if(x+y==0)break;
			new AOJ1072().doIt(x,y);
		}
	}

	class AOJ1072{
		void doIt(int x,int y){
			if((x*y)%2==0)System.out.println("yes");
			else System.out.println("no");
		}
	}
}