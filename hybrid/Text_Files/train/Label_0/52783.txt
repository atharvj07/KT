import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	
	static int n;
	static String [] s;
	static int[] c;
	static ArrayList<Character> list=new ArrayList<>();
	static boolean[] used;
	static boolean[] begin;
	
	static int dfs(int now) {
		int count=0;
		if(now==list.size()) {
			int sum=0;
			int[] sumn=new int[n];
			for(int i=0; i<n-1; i++) {
				for(int j=0; j<s[i].length(); j++) {
					sumn[i]+=c[s[i].charAt(j)-'A'];
					sumn[i]*=10;
				}
				sumn[i]/=10;
			}
			for(int i=0; i<n-1; i++) {
				//System.out.println(s[i]+" "+sumn[i]);
				sum+=sumn[i];
			}
			int ans=0;
			for(int j=0; j<s[n-1].length(); j++) {
				ans+=c[s[n-1].charAt(j)-'A'];
				ans*=10;
			}
			//System.out.println(s[n-1]+" "+ans/10);
			if(sum==ans/10) return 1;
			else return 0;
		}
		for(int i=0; i<=9; i++) {
			if(i==0 && begin[list.get(now)-'A']) continue;
			if(used[i]) continue;
			used[i]=true;
			c[list.get(now)-'A']=i;
			count+=dfs(now+1);
			used[i]=false;
		}
		return count;
	}
	
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){
			while(sc.hasNext()) {
				n=sc.nextInt();
				if(n==0) break;
				s=new String[n];
				c=new int[27];
				used=new boolean[10];
				begin=new boolean[27];
				boolean[] t=new boolean[27];
				for(int i=0; i<n; i++) {
					s[i]=sc.next();
					if(s[i].length()>1) begin[s[i].charAt(0)-'A']=true;
					for(int j=0; j<s[i].length(); j++) {
						if(! t[s[i].charAt(j)-'A']) {
							t[s[i].charAt(j)-'A']=true;
							list.add(s[i].charAt(j));
						}
					}
				}
				System.out.println(dfs(0));
				list.clear();
			}
			

		}
	}
}
