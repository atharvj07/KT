import java.util.Scanner;

//Goofy Converter
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		for(;;){
			int n = sc.nextInt(), m = sc.nextInt();
			if((n|m)==0)break;
			int[] a = new int[n];
			for(int i=0;i<n;i++)a[i]=sc.nextInt();
			String res = "Goofy";
			for(int S=0;S<1<<m;S++){
				StringBuilder sb = new StringBuilder();
				int s = 0, h = 0;
				boolean f = true;
				for(int k=0;k<m;k++){
					sb.append((S>>k)&1);
					if(((S>>k)&1)>0)s++;
				}
				if(s!=a[0])continue;
				for(int i=1;i<n&&f;i++){
					if(sb.charAt(h++)=='1')s--;
					if(a[i]==s)sb.append("0");
					else if(s+1==a[i]){
						sb.append("1"); s++;
					}
					else f=false;
				}
				if(f){
					res = sb.toString(); break;
				}
			}
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}