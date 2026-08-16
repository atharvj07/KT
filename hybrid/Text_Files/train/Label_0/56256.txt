import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//Cubes Without Holes
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int X = 501*501;
		int Y = 501;
		while(true){
			int n = sc.nextInt();
			int h = sc.nextInt();
			if((n|h)==0)break;
			Set<Integer> set = new HashSet<Integer>();
			while(h--!=0){
				String s = sc.next();
				int a = sc.nextInt();
				int b = sc.nextInt();
				if("xy".equals(s))for(int z=1;z<=n;z++)set.add(a*X+b*Y+z);
				else if("yz".equals(s))for(int x=1;x<=n;x++)set.add(x*X+a*Y+b);
				else for(int y=1;y<=n;y++)set.add(a*X+y*Y+b);
			}
			System.out.println(n*n*n-set.size());
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}