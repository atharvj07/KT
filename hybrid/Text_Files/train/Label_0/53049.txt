import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		
		int p, q;
		for(int i=0;i<s.length();i+=2){
			p = s.codePointAt(i) - 48;
			q = s.codePointAt(i+1);
			if(p==0 && q==85){
				System.out.print("nn");
			}else{
				if(p==2) System.out.print("k");
				else if(p==3) System.out.print("s");
				else if(p==4) System.out.print("t");
				else if(p==5) System.out.print("n");
				else if(p==6) System.out.print("h");
				else if(p==7) System.out.print("m");
				else if(p==8) System.out.print("y");
				else if(p==9) System.out.print("r");
				else if(p==0) System.out.print("w");
				
				if(q==84) System.out.print("a");
				else if(q==76) System.out.print("i");
				else if(q==85) System.out.print("u");
				else if(q==82) System.out.print("e");
				else if(q==68) System.out.print("o");
			}
		}
		System.out.println();
	
	}	
}