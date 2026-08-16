import java.io.IOException;
import java.util.Scanner;


public class Main{


	public static void main(String args[]) throws IOException{
		Scanner stdin = new Scanner(System.in);
		int tyo = 0;
		int hishi = 0;
		while(stdin.hasNext()){

			String tmp = stdin.nextLine();
			String[] str = tmp.split(",");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			int c = Integer.parseInt(str[2]);

			if(a == b) {
				hishi++;
			} else if((a * a) + (b * b) == (c * c)) {
				tyo++;
			} 
		}
		System.out.println(tyo);
		System.out.println(hishi);
	}
}