import java.util.Scanner;
public class Main{
	public static void main(String[] args){
        new Main().run();
    }
	public void run(){
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()){
			int n = scan.nextInt();
			if(n == -1){
				break;
			}else if(n == 0){
				System.out.println(0);
				continue;
			}
			String ans = "";
			while(n != 0){
				ans = n%4 + ans;
				n /= 4;
			}
			System.out.println(ans);
		}
	}
}