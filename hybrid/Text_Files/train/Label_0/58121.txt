import java.util.Scanner;

public class Walking {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc =new Scanner(System.in);
		int n=Integer.parseInt(sc.nextLine());
		while(n--!=0) {
			StringBuffer s1=new StringBuffer(sc.nextLine());
			StringBuffer s2=new StringBuffer(sc.nextLine());
			System.out.println(isRight(s1,s2)?"YES":"NO");
			
		}
	}
	private static boolean isRight(StringBuffer s1, StringBuffer s2) {
		// TODO Auto-generated method stub
		int i=0,j=0;
		if(s1.charAt(i)!=s2.charAt(j)||s1.length()>s2.length()) {
			return false;
		}
		for(;j<s2.length()&&i<s1.length();) {
			if(s1.charAt(i)==s2.charAt(j)) {
				j++;i++;continue;
			}
			if(i!=0&&s1.charAt(i-1)==s2.charAt(j)) {
				j++;
			}else {
				break;
			}
		}
		if(j!=s2.length()) {
			for(int ii=j;j<s2.length();j++) {
				if(s2.charAt(ii-1)!=s2.charAt(j)) {
					return false;
				}
			}
		}
		if(i==s1.length()&&j==s2.length()) {
			return true;
		}else {
			return false;
		}
	}

}
