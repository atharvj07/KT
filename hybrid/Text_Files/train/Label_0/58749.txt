import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		String t = sc.next();
		int min=10000;
		for(int i=0;i<(s.length()-t.length()+1);i++){
			String r=s.substring(i,i+t.length());
			int a=0;
			for(int k=0;k<t.length();k++){
				if(t.charAt(k)!=r.charAt(k)){a++;}
			}
			if(min>a){min=a;}
		}
		System.out.println(""+min);
	}
}