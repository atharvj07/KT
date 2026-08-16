import  java.util.*;
public class my {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in=new Scanner(System.in);
		int n=in.nextInt();
		String f[]=new String[n];
		for (int i = 0; i < f.length; i++) {
			f[i]=in.next();
		}
		int a=0;
		boolean b=true;
		for (int i = 0; i < f[0].length(); i++){
		for (int j = 0; j < f.length; j++) 
			
			if(f[j].charAt(i)!=f[0].charAt(i)) b=false;
		    if(b)a++;
		
		}
		System.out.print(a);
	}

}
