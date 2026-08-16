import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ

		Scanner sc = new Scanner(System.in);

		//入力表示
		String S = sc.next();
		int count=0;
		int ans =0;
	
		char [] a= S.toCharArray();
		 for(int i=0;i<a.length; i++) {

			 if(a[i]=='A' ||a[i]=='C' ||a[i]=='G'||a[i]=='T') {
				 count++;
			 }else {
				 if(ans<count) {
					 ans=count;
					 count=0;
					 
				 }
			 }
			
		 }
		 if(ans<count) {
			 ans=count;
		 }
		 System.out.println(ans);
	}
}